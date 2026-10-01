import unicodedata

def promedio(valores: list[float]) -> float | None:#primero generamos la funcion que revice una lista de valores numericos y devuelve el promedio de esos valores1 en tipo de dato float
    if not valores:#si la lista de valores esta vacia, devuelve None, para no fallar
        return None

    return sum(valores) / len(valores)#cado contrario devuelve el promedio de los valores de la lista


def contar_frecuencias(valores: list) -> dict:# esta funcion recibe una lista de valores y devuelve un diccionario con la frecuencia de cada valor en la lista
    frecuencias = {}#generas un diccion para almacenar los valores y sus frecuencias
    for valor in valores:
        frecuencias[valor] = frecuencias.get(valor, 0) + 1 #generas un ciclo for para recorrer la lista de valores y contar cuantas veces aparece cada valor en la lista, si el valor no esta en el diccionario, se agrega con un valor de 0 y se le suma 1
    return frecuencias


def clasificar_ingreso(ingreso: float) -> str:#esta funcion recibe un valor numerico y devuelve una cadena de texto que indica si el ingreso es bajo, medio o alto
   
    try:
        ingreso = float(ingreso)#se determina si el valor se puede trandormar a valor tipo float
    except (TypeError, ValueError):#si no se puede transformar a float, devuelve "invalido"
        return "invalido"

    if ingreso < 500:#si se cumple la condicion ingresa a la condicional if para ser evaluado
        return "bajo"
    if ingreso < 1500:
        return "medio"
    return "alto"


def resumen(registros: list) -> dict:
    edades = [registro["edad"] for registro in registros]#permite generar una lista de edades a partir de la lista de registros, donde cada registro es un diccionario que contiene la clave "edad"
    return {
        "minimo": min(edades),
        "maximo": max(edades),
        "promedio": promedio(edades),
    }


if __name__ == "__main__":
    assert promedio([10, 20, 30]) == 20.0
    assert promedio([]) is None
    assert contar_frecuencias(["a", "b", "a"]) == {"a": 2, "b": 1}
    assert clasificar_ingreso(300) == "bajo"
    assert clasificar_ingreso(800) == "medio"
    assert clasificar_ingreso(2000) == "alto"
    assert clasificar_ingreso("abc") == "invalido"
    assert resumen([{"edad": 20}, {"edad": 30}, {"edad": 40}]) == {
        "minimo": 20,
        "maximo": 40,
        "promedio": 30.0,
    }
    print("Todas las pruebas pasaron")


#Tarea martes 22/09
def limpiar_nombres_columnas(df):
    df.columns = [
        "_".join(unicodedata.normalize("NFD", str(columna).strip())
                 .encode("ascii", "ignore").decode("ascii").lower().split())
        for columna in df.columns
    ]
    return df


def reporte_nulos(df):
    reporte = df.isna().sum().rename("nulos").reset_index()# Suma columna a columna los valores nulos y genera un DataFrame con el resultado, convierte la primera columna en un indice y renombra la columna de nulos como "nulos"
    reporte.columns = ["columna", "nulos"]#renombra las columnas del DataFrame para que sean más descriptivas
    reporte["porcentaje_nulos"] = (reporte["nulos"] / len(df)) * 100#calcula el porcentaje de valores nulos en cada columna y lo agrega como una nueva columna en el DataFrame
    return reporte.sort_values("nulos", ascending=False, ignore_index=True)#ordena el DataFrame por la columna "nulos" en orden descendente y reinicia el índice del DataFrame resultante, devolviendo un informe de valores nulos en el DataFrame original



def normalizar_texto(serie):
    return serie.str.strip().str.lower().str.replace(r"\s+", " ", regex=True)#elimina los espacios en blanco al inicio y al final de cada cadena, convierte todas las letras a minúsculas y reemplaza múltiples espacios en blanco consecutivos con un solo espacio


def limites_iqr(serie, k=1.5):
    primer_cuartil = serie.quantile(0.25)
    tercer_cuartil = serie.quantile(0.75)
    rango_intercuartil = tercer_cuartil - primer_cuartil
    return (
        primer_cuartil - k * rango_intercuartil,
        tercer_cuartil + k * rango_intercuartil,
    )



