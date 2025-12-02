# Actividad 2: Comprensión de Datos con Pandas

## Dataset Utilizado

**Archivo:** `premio_mayor_loteria_medellin.csv`  
**Ruta:** `c:\Users\juand\Downloads\fdoc_cd_act2-main\premio_mayor_loteria_medellin.csv`

## Descripción General del Dataset

El dataset contiene información histórica sobre los premios mayores de la Lotería de Medellín, Colombia. Incluye **975 registros** que abarcan desde el **5 de enero de 2007** hasta el **17 de octubre de 2025**, representando aproximadamente 18 años de sorteos semanales.

### Características principales:
- **Dimensiones:** 975 filas × 5 columnas
- **Periodo:** 2007-2025
- **Frecuencia:** Sorteos semanales (aproximadamente 52 sorteos por año)
- **Valores faltantes:** Mínimos (solo 972 valores nulos en columna irrelevante `Unnamed: 4`)

## Clasificación de Columnas por Tipo

### 1. **Columnas de Fecha**
| Columna | Tipo Original | Tipo Convertido | Descripción |
|---------|---------------|-----------------|-------------|
| `FECHA` | object (texto) | datetime64 | Fecha del sorteo en formato YYYY-MM-DD |

**Análisis:**
- Fecha mínima: 2007-01-05
- Fecha máxima: 2025-10-17
- Rango: 18 años de datos históricos

### 2. **Columnas Numéricas Enteras**

| Columna | Tipo | Valores Únicos | Descripción |
|---------|------|----------------|-------------|
| `SORTEO` | int64 | 975 | Número consecutivo del sorteo (ID único) |
| `NÚMERO` | int64 | 922 | Número ganador del premio mayor (rango: 34-9993) |
| `SERIE` | int64 | 346 | Serie del billete ganador (rango: 0-659) |

**Estadísticas de `NÚMERO`:**
- Mínimo: 34
- Máximo: 9,993
- Promedio: 5,090.46
- Mediana: 5,208

**Estadísticas de `SERIE`:**
- Mínimo: 0
- Máximo: 659
- Promedio: 159.60
- Mediana: 152

### 3. **Columnas Categóricas**
*No hay columnas puramente categóricas en este dataset. Las columnas numéricas tampoco representan categorías.*

### 4. **Columnas de Texto**
| Columna | Descripción | Valores Nulos |
|---------|-------------|---------------|
| `Unnamed: 4` | Columna sin nombre, aparentemente errónea | 972 de 975 (99.7%) |

**Nota:** Esta columna debe ser eliminada en un análisis más profundo por carecer de información relevante.

### 5. **Columnas Booleanas**
*No hay columnas booleanas (True/False) en este dataset.*

## Transformaciones Aplicadas

Según el contenido permitido, se aplicaron las siguientes transformaciones básicas:

### 1. **Conversión de Tipos de Datos**
```python
# Convertir columna FECHA de tipo object a datetime
df['FECHA'] = pd.to_datetime(df['FECHA'])
```
**Justificación:** Permite realizar análisis temporales y extraer componentes de fecha.

### 2. **Extracción de Componentes Temporales**
```python
# Extracción del año
df['AÑO'] = df['FECHA'].dt.year

# Extracción del mes
df['MES'] = df['FECHA'].dt.month
```
**Justificación:** Facilita el análisis de tendencias por año y por mes.

### 3. **Métodos de Inspección y Resumen Utilizados**
- `df.head()` - Primeras 5 filas
- `df.tail()` - Últimas 5 filas
- `df.info()` - Información de tipos y valores nulos
- `df.describe()` - Estadísticas descriptivas
- `df.shape` - Dimensiones del dataset
- `df[columna].nunique()` - Conteo de valores únicos
- `df[columna].isnull().sum()` - Conteo de valores nulos
- `df[columna].value_counts()` - Frecuencia de valores
- `df[columna].min()`, `max()`, `mean()`, `median()` - Estadísticos básicos

## Resúmenes y Análisis

### Análisis de Números Ganadores

**Top 10 números más repetidos:**
| Número | Frecuencia |
|--------|------------|
| 2570 | 3 veces |
| 539 | 3 veces |
| 2416 | 2 veces |
| 4637 | 2 veces |
| 7630 | 2 veces |

**Observación:** De 922 números únicos en 975 sorteos, la mayoría de números solo aparecen una vez (94.4%), lo que indica una distribución muy dispersa y aleatoria.

### Análisis de Series

**Top 10 series más repetidas:**
| Serie | Frecuencia |
|-------|------------|
| 53 | 10 veces |
| 73 | 8 veces |
| 218 | 7 veces |
| 166 | 7 veces |
| 120 | 7 veces |
| 169 | 7 veces |
| 164 | 7 veces |

**Observación:** Con 346 series únicas en 975 sorteos, hay una repetición más notoria que en los números (frecuencia promedio: 2.8 veces por serie).

### Análisis Temporal

**Distribución por año:**
- La mayoría de años tienen 52 sorteos (coincide con sorteos semanales)
- 2020 tiene solo 45 sorteos (posible interrupción por pandemia COVID-19)
- 2025 tiene 42 sorteos hasta octubre (año incompleto)

**Distribución por mes:**
- Distribución bastante uniforme a lo largo de todos los meses
- Rango: 76-85 sorteos por mes
- No hay una estacionalidad marcada

## Conclusiones

1. **Calidad de los datos:** El dataset está mayormente completo con solo una columna irrelevante (`Unnamed: 4`) que puede ser descartada. No hay valores faltantes en las columnas principales.

2. **Aleatoriedad de resultados:** La baja repetición de números ganadores (94.4% aparecen solo una vez) confirma la naturaleza aleatoria de los sorteos, como es esperado en un juego de lotería.

3. **Consistencia temporal:** La regularidad de aproximadamente 52 sorteos por año indica una operación consistente y sistemática de la lotería, con la excepción notable de 2020.

4. **Rango de valores:** Los números ganadores varían entre 34 y 9,993, lo que sugiere un rango amplio de combinaciones posibles. Las series van de 0 a 659, con un rango más limitado.

5. **Patrón de series:** Las series muestran mayor repetición que los números, lo que podría indicar un número limitado de series disponibles en circulación.

## 5 Preguntas Relevantes sobre Problemas Reales

### 1. **¿Se puede predecir el próximo número ganador basándose en patrones históricos?**

**Evaluación:** ❌ **No, los datos NO son suficientes**

**Justificación:** La lotería es un evento aleatorio por diseño. Aunque tenemos 975 sorteos históricos, la altísima dispersión de números (94.4% aparecen solo una vez) confirma que no hay patrones predecibles. Cualquier aparente "patrón" sería producto del azar y no predictivo. Además, predecir loterías violenta el principio de aleatoriedad que las rige legalmente.

---

### 2. **¿Se puede identificar si ciertas series tienen mayor probabilidad de ganar para optimizar la compra de billetes?**

**Evaluación:** ⚠️ **Parcialmente, pero no es útil en la práctica**

**Justificación:** Los datos muestran que la serie 53 ha ganado 10 veces en 975 sorteos (1.03%), mientras que el promedio es 2.8 veces (0.29%). Sin embargo, esta diferencia puede ser producto del azar y no indica una ventaja estadística real. Con solo 975 observaciones, no hay suficiente evidencia para afirmar que alguna serie es "más afortunada". Se requeriría un análisis estadístico más riguroso (pruebas de hipótesis) que está fuera del alcance permitido.

---

### 3. **¿Se puede analizar el impacto de eventos externos (como la pandemia COVID-19) en la frecuencia de sorteos?**

**Evaluación:** ✅ **Sí, los datos SON suficientes**

**Justificación:** El dataset incluye la columna `FECHA` que permite identificar anomalías temporales. Ya observamos que 2020 tuvo solo 45 sorteos en lugar de los típicos 52, coincidiendo con la pandemia. Podemos calcular la frecuencia de sorteos por año, identificar años atípicos y correlacionarlos con eventos históricos conocidos. El análisis temporal básico con `value_counts()` por año es suficiente para este propósito.

---

### 4. **¿Se puede diseñar un sistema de alerta para notificar a jugadores cuando aparezcan números con ciertos dígitos o características (ej. números capicúa, múltiplos de 100)?**

**Evaluación:** ✅ **Sí, los datos SON suficientes**

**Justificación:** Aunque no predice ganadores, el dataset permite analizar la frecuencia histórica de diferentes patrones numéricos:
- Números capicúa (ej. 1221, 3443)
- Números múltiplos de 100, 500, 1000
- Números con dígitos repetidos
- Rangos específicos (0-1000, 1000-5000, etc.)

Con operaciones básicas de Pandas podemos filtrar y contar estos patrones, lo cual es útil para análisis estadístico descriptivo o sistemas de información, aunque no para predicción.

---

### 5. **¿Se puede realizar un análisis de recaudación y distribución geográfica de premios para la planificación presupuestaria de la lotería?**

**Evaluación:** ❌ **No, los datos NO son suficientes**

**Justificación:** El dataset actual solo contiene información sobre los premios mayores (número, serie, fecha), pero carece de información crítica para este análisis:
- Valor monetario del premio
- Cantidad de billetes vendidos por sorteo
- Ubicación geográfica donde se vendió el billete ganador
- Costos operativos de la lotería
- Información sobre premios menores

Para responder esta pregunta, se necesitaría un dataset complementario con información financiera y geográfica, que no está presente en los datos actuales.

---

## Autor
Análisis realizado con Pandas utilizando métodos básicos de exploración y manipulación de datos.

**Fecha de análisis:** Diciembre 2025  
**Dataset:** Premio Mayor Lotería de Medellín (2007-2025)
