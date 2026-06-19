import os

EXCLUDE_DIRS = {'.quarto', '_site', '.git', '__pycache__', 'node_modules'}
EXCLUDE_FILES = {'listar_estructura.py'}

def print_directory_tree(startpath):
    """
    Recorre el directorio de forma recursiva imprimiendo una estructura de árbol
    limpia y legible para entornos bilingües de Quarto.
    """
    for root, dirs, files in os.walk(startpath):
        # Filtrar directorios excluidos sobre la marcha
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        # Calcular el nivel de profundidad para la indentación
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * level
        
        # Obtener el nombre de la carpeta actual
        folder_name = os.path.basename(root)
        if folder_name == '':
            folder_name = os.path.abspath(root).split(os.sep)[-1]
            
        print(f"{indent}📁 {folder_name}/")
        
        subindent = ' ' * 4 * (level + 1)
        for file in sorted(files):
            if file not in EXCLUDE_FILES:
                print(f"{subindent}📄 {file}")

if __name__ == '__main__':
    print("====================================================")
    print("      ESTRUCTURA ACTUAL DE TU PROYECTO (LIMPIA)      ")
    print("====================================================\n")
    
    print_directory_tree('.')
    print("\n====================================================")



