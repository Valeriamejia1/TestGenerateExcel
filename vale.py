import openpyxl

def generar_excel():
    # Crea un nuevo libro de trabajo
    wb = openpyxl.Workbook()

    # Selecciona la hoja activa (por defecto, es la primera hoja creada)
    hoja_activa = wb.active

    # Escribe "Hello World" en la celda A1
    hoja_activa['A1'] = "Hello World"

    # Obtiene el nombre del archivo (sin la extensión) para guardarlo con el mismo nombre
    nombre_archivo = "HelloWorld.xlsx"

    # Guarda el archivo
    wb.save(nombre_archivo)

    print(f"Se ha generado el archivo {nombre_archivo}")

if __name__ == "__main__":
    generar_excel()
