from medical_data_visualizer import draw_cat_plot, draw_heat_map
import matplotlib.pyplot as plt

# Llamadas a las funciones para generar los gráficos
print("Generating categorical plot...")
cat_plot_fig = draw_cat_plot()
plt.show()  # Mostrar el gráfico categórico

print("Generating heatmap...")
heatmap_fig = draw_heat_map()
plt.show()  # Mostrar el heatmap

print("Categorical plot and heatmap have been generated and displayed.")
