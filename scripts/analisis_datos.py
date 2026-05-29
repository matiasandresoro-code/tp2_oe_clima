import pandas as pd
import matplotlib.pyplot as plt

# 1. Leemos el archivo. Al ser de ancho fijo (fwf) utilizamos read_fwf. Con skiprows salteamos la linea de guiones.
df = pd.read_fwf('datos/dataset.txt', skiprows=[1], encoding="latin1")

# 2. Limpiamos espacios extra en los nombres de las ciudades y filtramos por Rosario
df['NOMBRE'] = df['NOMBRE'].str.strip()
df_rosario = df[df['NOMBRE'] == 'ROSARIO AERO'].copy()

# 3. Convertimos la fecha a formato fecha real para el grafico, ya que en el dataset viene en formato 27052026
df_rosario['FECHA'] = pd.to_datetime(df_rosario['FECHA'], format='%d%m%Y')
df_rosario = df_rosario.sort_values('FECHA')

# 4. Forzamos la conversión a numérico y manejamos errores ----
df_rosario['TMAX'] = pd.to_numeric(df_rosario['TMAX'], errors='coerce')
df_rosario['TMIN'] = pd.to_numeric(df_rosario['TMIN'], errors='coerce')

# 5. Calcular promedios, maximas y minimas
tmax_promedio = df_rosario['TMAX'].mean()
tmin_promedio = df_rosario['TMIN'].mean()
tmax_absoluta = df_rosario['TMAX'].max()
tmin_absoluta = df_rosario['TMIN'].min()

print("--- RESULTADOS ROSARIO ---")
print(f"Temp. Máxima Promedio: {tmax_promedio:.2f} °C")
print(f"Temp. Mínima Promedio: {tmin_promedio:.2f} °C")
print(f"Pico de Calor (Maxima): {tmax_absoluta} °C")
print(f"Pico de Frio (Minima): {tmin_absoluta} °C")

# 6. Generamos el grafico
plt.figure(figsize=(10, 5))
plt.plot(df_rosario['FECHA'], df_rosario['TMAX'], color='red', label='Temp. Maxima')
plt.plot(df_rosario['FECHA'], df_rosario['TMIN'], color='blue', label='Temp. Minima')

plt.title('Evolucion de Temperaturas en Rosario (Últimos 365 dias)')
plt.xlabel('Fecha')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)

# 7. Guardamos el grafico generado en la carpeta de resultados
plt.savefig('resultados/grafico_resultados.png')
print("\n Grafico guardado en 'resultados/grafico_resultados.png'")
