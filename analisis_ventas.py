import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

#Cargar el archivo excel
df= pd.read_excel('C:/Users/U-0393/Desktop/S.MORALES/PRACTICAS GITHUB/DATA SCIENCE/ventas_productos.xlsx')

#Mostrar los primeros registros
print(df.head())

#Agrupar por producto y sumar las ventas
ventas_por_producto = df.groupby('Producto')['Ventas'].sum().reset_index()

#Ordenar los productos por cantidad de ventas
ventas_por_producto = ventas_por_producto.sort_values(by='Ventas', ascending=False)

#Mostrar los productos más vendidos
print(ventas_por_producto)

#Crear un gr´rafico de barras
sns.barplot(x='Producto', y='Ventas', data=ventas_por_producto)
plt.title('Ventas Totales Por Producto')
plt.show()
