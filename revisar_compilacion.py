# rhysis-web/revisar_compilacion.py
import os

def mapear_site():
    ruta_site = "./_site"
    
    if not os.path.exists(ruta_site):
        print("❌ Error: La carpeta _site no existe. Ejecuta 'quarto render' primero.")
        return

    print("====================================================")
    print("      MAPA REAL DE LA CARPETA DE SALIDA (_site)     ")
    print("====================================================")
    
    for raiz, dirs, archivos in os.walk(ruta_site):
        nivel = raiz.replace(ruta_site, '').count(os.sep)
        indentacion = ' ' * 4 * nivel
        sub_carpeta = os.path.basename(raiz)
        
        if sub_carpeta and sub_carpeta != '_site':
            print(f"{indentacion}📁 {sub_carpeta}/")
            
        sub_indentacion = ' ' * 4 * (nivel + 1)
        for archivo in archivos:
            if archivo.endswith('.html') or archivo == '_redirects':
                print(f"{sub_indentacion}📄 {archivo}")

if __name__ == "__main__":
    mapear_site()