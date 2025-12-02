import pandas as pd

# Cargar el dataset
df = pd.read_csv('premio_mayor_loteria_medellin.csv')

# Mostrar información general
print("=" * 80)
print("INFORMACIÓN GENERAL DEL DATASET")
print("=" * 80)
print(f"\nDimensiones del dataset: {df.shape[0]} filas x {df.shape[1]} columnas")
print(f"\nPrimeras 5 filas:")
print(df.head())
print(f"\nÚltimas 5 filas:")
print(df.tail())

# Información de tipos de datos
print("\n" + "=" * 80)
print("TIPOS DE DATOS")
print("=" * 80)
print(df.info())

# Estadísticas descriptivas
print("\n" + "=" * 80)
print("ESTADÍSTICAS DESCRIPTIVAS - VARIABLES NUMÉRICAS")
print("=" * 80)
print(df.describe())

# Análisis de valores únicos por columna
print("\n" + "=" * 80)
print("VALORES ÚNICOS POR COLUMNA")
print("=" * 80)
for col in df.columns:
    print(f"\n{col}:")
    print(f"  - Valores únicos: {df[col].nunique()}")
    print(f"  - Valores nulos: {df[col].isnull().sum()}")
    print(f"  - Tipo de dato: {df[col].dtype}")

# Análisis de la columna FECHA
print("\n" + "=" * 80)
print("ANÁLISIS DE LA COLUMNA FECHA")
print("=" * 80)
# Convertir a datetime
df['FECHA'] = pd.to_datetime(df['FECHA'])
print(f"Fecha mínima: {df['FECHA'].min()}")
print(f"Fecha máxima: {df['FECHA'].max()}")
print(f"Rango de años: {df['FECHA'].dt.year.min()} - {df['FECHA'].dt.year.max()}")

# Análisis de números ganadores
print("\n" + "=" * 80)
print("ANÁLISIS DE NÚMEROS GANADORES")
print("=" * 80)
print(f"Número mínimo: {df['NÚMERO'].min()}")
print(f"Número máximo: {df['NÚMERO'].max()}")
print(f"Número promedio: {df['NÚMERO'].mean():.2f}")
print(f"Mediana: {df['NÚMERO'].median():.2f}")

# Análisis de series
print("\n" + "=" * 80)
print("ANÁLISIS DE SERIES")
print("=" * 80)
print(f"Serie mínima: {df['SERIE'].min()}")
print(f"Serie máxima: {df['SERIE'].max()}")
print(f"Serie promedio: {df['SERIE'].mean():.2f}")

# Top 10 números más ganadores
print("\n" + "=" * 80)
print("TOP 10 NÚMEROS MÁS REPETIDOS")
print("=" * 80)
print(df['NÚMERO'].value_counts().head(10))

# Top 10 series más ganadoras
print("\n" + "=" * 80)
print("TOP 10 SERIES MÁS REPETIDAS")
print("=" * 80)
print(df['SERIE'].value_counts().head(10))

# Análisis por año
print("\n" + "=" * 80)
print("ANÁLISIS POR AÑO")
print("=" * 80)
df['AÑO'] = df['FECHA'].dt.year
print(df['AÑO'].value_counts().sort_index())

# Análisis por mes
print("\n" + "=" * 80)
print("ANÁLISIS POR MES")
print("=" * 80)
df['MES'] = df['FECHA'].dt.month
print(df['MES'].value_counts().sort_index())

print("\n" + "=" * 80)
print("ANÁLISIS COMPLETADO")
print("=" * 80)
