import json
import os
from json2html import *

# Caminho para o arquivo de favoritos
bookmarks_path = '/home/eduardo/Documentos/projetos/ConverterHTML/Bookmarks'

# Verifique se o arquivo de favoritos existe
if not os.path.exists(bookmarks_path):
    print(f'Erro: O arquivo {bookmarks_path} não existe.')
else:
    # Leia o arquivo de favoritos
    try:
        with open(bookmarks_path, 'r', encoding='utf-8') as file:
            bookmarks_data = json.load(file)
            print('Arquivo de favoritos carregado com sucesso.')
    except Exception as e:
        print(f'Erro ao ler o arquivo de favoritos: {e}')

    # Converter os favoritos para HTML
    try:
        bookmarks_html = json2html.convert(json=bookmarks_data)
        print('Conversão para HTML concluída com sucesso.')
    except Exception as e:
        print(f'Erro ao converter para HTML: {e}')

    # Caminho de saída para o arquivo HTML
    output_path = '/home/eduardo/Documentos/projetos/ConverterHTML/bookmarks.html'
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(bookmarks_html)
            print(f'Arquivo HTML criado com sucesso em: {output_path}')
    except Exception as e:
        print(f'Erro ao escrever o arquivo HTML: {e}')
