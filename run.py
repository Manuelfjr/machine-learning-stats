import os
import nbformat as nbf

# A estrutura do seu TOC
toc = {
    "parts": [
        {
            "caption": "Introdução",
            "chapters": [
                {"file": "ml-book/01.guide/o_que_e_ml"},
                {"file": "ml-book/01.guide/o_que_e_estatistica"},
                {"file": "ml-book/01.guide/relacao_ml_estatistica"},
                # {"file": "ml-book/01.guide/markdown"},
                {"file": "ml-book/01.guide/notebooks"},
                {"file": "ml-book/01.guide/exercicios"},
            ],
        },
        {
            "caption": "Fundamentos de Estatística",
            "chapters": [
                {"file": "ml-book/02.stats/variaveis_distribuicoes"},
                {"file": "ml-book/02.stats/medidas_centralidade_dispersao"},
                {"file": "ml-book/02.stats/probabilidade"},
                {"file": "ml-book/02.stats/inferencia_estatistica"},
                {"file": "ml-book/02.stats/testes_hipoteses"},
                {"file": "ml-book/02.stats/regressao_linear"},
                {"file": "ml-book/02.stats/exercicios"}
            ]
        }
    ]
}

# Para cada parte do TOC
for part in toc["parts"]:
    # Para cada capítulo na parte
    for chapter in part["chapters"]:
        # Obtenha o caminho do arquivo
        file_path = chapter["file"]
        name = file_path.split("/")[-1].replace("_", " ").title()
        # Adicione a extensão .ipynb ao caminho do arquivo
        notebook_path: str = f"{file_path}.ipynb"
        # Crie o diretório para o arquivo, se ele não existir
        if os.path.exists(path=notebook_path):
            continue
        os.makedirs(name=os.path.dirname(notebook_path), exist_ok=True)
        # Crie um novo notebook
        nb = nbf.v4.new_notebook()
        # Adicione uma célula de markdown com o nome da seção
        nb.cells.append(nbf.v4.new_markdown_cell(f"# {name}"))
        # Salve o notebook no caminho especificado
        with open(file=notebook_path, mode="w") as f:
            nbf.write(nb, f)