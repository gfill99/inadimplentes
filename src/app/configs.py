import sys
import os

def mapeia_pastas():
    pastas = ['utils','database']
    # Adicionar o caminho da pasta onde está o módulo
    for p in pastas:
        sys.path.append(os.path.abspath(f"../{p}"))