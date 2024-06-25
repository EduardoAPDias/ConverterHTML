import json
import os

# Caminho para o arquivo de favoritos recuperado
bookmarks_path = '/home/eduardo/Documentos/projetos/ConverterHTML/Bookmarks'

# Verifique se o arquivo de favoritos existe
if not os.path.exists(bookmarks_path):
    print(f'Erro: O arquivo {bookmarks_path} não existe.')
else:
    try:
        # Leia o arquivo de favoritos
        with open(bookmarks_path, 'r', encoding='utf-8') as file:
            bookmarks_data = json.load(file)
            print('Arquivo de favoritos carregado com sucesso.')

        # Função para converter os dados JSON para o formato NETSCAPE
        def convert_to_netscape(bookmarks, level=0):
            html = ''
            indent = ' ' * (4 * level)
            if isinstance(bookmarks, list):
                for item in bookmarks:
                    html += convert_to_netscape(item, level)
            elif isinstance(bookmarks, dict):
                if 'children' in bookmarks:
                    html += f'{indent}<DT><H3 ADD_DATE="{bookmarks.get("date_added", 0)}" LAST_MODIFIED="{bookmarks.get("date_modified", 0)}">{bookmarks.get("name")}</H3>\n'
                    html += f'{indent}<DL><p>\n'
                    html += convert_to_netscape(bookmarks['children'], level + 1)
                    html += f'{indent}</DL><p>\n'
                elif 'url' in bookmarks:
                    html += f'{indent}<DT><A HREF="{bookmarks["url"]}" ADD_DATE="{bookmarks.get("date_added", 0)}">{bookmarks["name"]}</A>\n'
            return html

        # Raízes dos favoritos
        roots = bookmarks_data['roots']
        bookmark_bar = roots.get('bookmark_bar', {})

        # Converter os favoritos para o formato NETSCAPE
        bookmarks_html_content = convert_to_netscape(bookmark_bar.get('children', []))

        # Criação de um HTML completo no formato NETSCAPE
        html_content = f"""<!DOCTYPE NETSCAPE-Bookmark-file-1>
<!-- This is an automatically generated file.
     It will be read and overwritten.
     DO NOT EDIT! -->
<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">
<TITLE>Bookmarks</TITLE>
<H1>Bookmarks</H1>
<DL><p>
{bookmarks_html_content}
</DL><p>
"""

        # Caminho de saída para o arquivo HTML
        output_path = '/home/eduardo/Documentos/projetos/ConverterHTML/bookmarks.html'
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(html_content)
            print(f'Arquivo HTML criado com sucesso em: {output_path}')
    except Exception as e:
        print(f'Erro: {e}')
