import tkinter as tk
from tkinter import ttk, messagebox


class PlantPopulationApp:
    def __init__(self, root):
        self.root = root
        root.title("Estimador de Población de Plantas")

        # --- Notebook para las pestañas ---
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(pady=10, padx=10, expand=True, fill="both")

        # --- Pestaña de Calculadora ---
        self.calculator_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.calculator_frame, text='Calculadora')

        # --- Variables para almacenar los inputs y resultados ---
        self.row_spacing_var = tk.DoubleVar()
        self.plant_spacing_var = tk.DoubleVar()
        # Variable para la longitud de hilera (opcional)
        self.row_length_var = tk.DoubleVar(value=0.0)
        self.unit_var = tk.StringVar()  # Variable para la unidad (metros o cm)

        self.population_hectare_var = tk.StringVar()
        # Nuevo: Plantas por metro de hilera
        self.plants_per_meter_row_var = tk.StringVar()
        # Nuevo: Plantas por la longitud de hilera especificada
        self.plants_per_row_length_var = tk.StringVar()

        # Establecer valor por defecto para la unidad
        self.unit_var.set("metros")  # Por defecto, unidades en metros

        # --- Configuración de la Interfaz de la Calculadora ---
        self.calculator_frame.columnconfigure(0, weight=1)

        # Sección de Entradas
        input_frame = ttk.LabelFrame(
            self.calculator_frame, text="Espaciamientos y Longitud", padding="10")
        input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5, padx=5)
        # Permitir que las entradas se expandan
        input_frame.columnconfigure(1, weight=1)

        ttk.Label(input_frame, text="Espaciamiento entre Hileras:").grid(
            row=0, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.row_spacing_var).grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        ttk.Label(input_frame, text="Espaciamiento entre Plantas:").grid(
            row=1, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.plant_spacing_var).grid(
            row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Nueva entrada para la longitud de hilera
        ttk.Label(input_frame, text="Longitud de Hilera (Opcional):").grid(
            row=2, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Entry(input_frame, textvariable=self.row_length_var).grid(
            row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Selección de Unidades
        ttk.Label(input_frame, text="Unidades:").grid(
            row=3, column=0, sticky=tk.W, padx=5, pady=5)
        unit_combobox = ttk.Combobox(input_frame, textvariable=self.unit_var, values=[
                                     "metros", "centímetros"], state="readonly")
        unit_combobox.grid(row=3, column=1, sticky=(
            tk.W, tk.E), padx=5, pady=5)
        unit_combobox.current(0)  # Seleccionar "metros" por defecto

        # Botón de Cálculo
        calculate_button = ttk.Button(
            self.calculator_frame, text="Calcular Población", command=self.calculate_population)
        calculate_button.grid(row=1, column=0, pady=10)

        # Sección de Resultados
        results_frame = ttk.LabelFrame(
            self.calculator_frame, text="Resultados", padding="10")
        results_frame.grid(row=2, column=0, sticky=(
            tk.W, tk.E), pady=5, padx=5)
        # Permitir que la etiqueta de resultado se expanda
        results_frame.columnconfigure(1, weight=1)

        ttk.Label(results_frame, text="Población Estimada por Hectárea:").grid(
            row=0, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(results_frame, textvariable=self.population_hectare_var).grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Nuevo resultado: Plantas por metro de hilera
        ttk.Label(results_frame, text="Plantas por Metro de Hilera:").grid(
            row=1, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(results_frame, textvariable=self.plants_per_meter_row_var).grid(
            row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        # Nuevo resultado: Plantas por longitud de hilera especificada
        ttk.Label(results_frame, text="Plantas por Hilera (Longitud Espec.):").grid(
            row=2, column=0, sticky=tk.W, padx=5, pady=5)
        ttk.Label(results_frame, textvariable=self.plants_per_row_length_var).grid(
            row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        # --- Pestaña de Información ---
        self.info_frame = ttk.Frame(self.notebook, padding="10")
        self.notebook.add(self.info_frame, text='Información')

        self.info_frame.columnconfigure(0, weight=1)
        self.info_frame.rowconfigure(0, weight=1)

        info_content = """
        **Estimador de Población de Plantas**

        Esta aplicación calcula la población estimada de plantas por hectárea y por longitud de hilera basándose en los espaciamientos.

        **Cómo usar:**

        1. Ingresa el espaciamiento promedio entre las hileras de tu cultivo.
        2. Ingresa el espaciamiento promedio entre las plantas dentro de una misma hilera.
        3. **Opcional:** Ingresa una longitud específica de hilera si deseas calcular cuántas plantas habría en ese tramo.
        4. Selecciona las unidades en las que ingresaste los espaciamientos y la longitud de hilera (metros o centímetros).
        5. Haz clic en "Calcular Población".

        **Resultados:**

        * **Población Estimada por Hectárea:** Cantidad estimada de plantas en una hectárea (10,000 m²).
        * **Plantas por Metro de Hilera:** Cantidad estimada de plantas en un metro lineal de hilera.
        * **Plantas por Hilera (Longitud Espec.):** Cantidad estimada de plantas en la longitud de hilera que especificaste (si la ingresaste).

        **Fórmulas utilizadas:**

        * Área por planta (m²) = (Espaciamiento entre Hileras en metros) * (Espaciamiento entre Plantas en metros)
        * Población por hectárea = 10,000 m² / Área por planta (m²)
        * Plantas por metro de hilera = 1 / (Espaciamiento entre Plantas en metros)
        * Plantas por Hilera = (Longitud de Hilera en metros) / (Espaciamiento entre Plantas en metros)

        *Nota: Estos son cálculos teóricos. La población real puede variar debido a la germinación, fallas en la siembra, etc.*

        ---
        Desarrollado por By LuisFarming.
        """
        self.info_text = tk.Text(
            self.info_frame, wrap="word", state="disabled", padx=10, pady=10)
        self.info_text.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        self.info_scrollbar = ttk.Scrollbar(
            self.info_frame, orient="vertical", command=self.info_text.yview)
        self.info_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.info_text.configure(yscrollcommand=self.info_scrollbar.set)
        self.info_text.config(state="normal")
        self.info_text.insert(tk.END, info_content)
        self.info_text.config(state="disabled")

    def calculate_population(self):
        """Realiza el cálculo de la población de plantas."""
        try:
            row_spacing = self.row_spacing_var.get()
            plant_spacing = self.plant_spacing_var.get()
            row_length = self.row_length_var.get()  # Obtener la longitud de hilera
            unit = self.unit_var.get()

            # Validar entradas básicas
            if row_spacing <= 0 or plant_spacing <= 0:
                messagebox.showwarning(
                    "Entrada Inválida", "Por favor, ingrese valores positivos mayores que cero para los espaciamientos.")
                # Limpiar resultados si la entrada es inválida
                self.population_hectare_var.set("")
                self.plants_per_meter_row_var.set("")
                self.plants_per_row_length_var.set("")
                return

            # Convertir espaciamientos a metros si la unidad es centímetros
            if unit == "centímetros":
                row_spacing_m = row_spacing / 100.0
                plant_spacing_m = plant_spacing / 100.0
            else:  # Asumir metros
                row_spacing_m = row_spacing
                plant_spacing_m = plant_spacing

            # --- Cálculos ---

            # 1. Población por Hectárea
            area_per_plant_sq_m = row_spacing_m * plant_spacing_m
            if area_per_plant_sq_m <= 0:  # Evitar división por cero
                population_per_hectare = 0
                messagebox.showwarning(
                    "Error de Cálculo", "El área por planta es cero o negativa, no se puede calcular la población por hectárea.")
                self.population_hectare_var.set("")
            else:
                population_per_hectare = 10000.0 / area_per_plant_sq_m
                # Formato sin decimales y con separador de miles
                self.population_hectare_var.set(
                    f"{population_per_hectare:,.0f}")

            # 2. Plantas por Metro de Hilera
            if plant_spacing_m <= 0:  # Evitar división por cero
                plants_per_meter_row = 0
                messagebox.showwarning(
                    "Error de Cálculo", "El espaciamiento entre plantas es cero, no se puede calcular las plantas por metro de hilera.")
                self.plants_per_meter_row_var.set("")
            else:
                plants_per_meter_row = 1.0 / plant_spacing_m
                self.plants_per_meter_row_var.set(
                    f"{plants_per_meter_row:.2f}")  # Formato con 2 decimales

            # 3. Plantas por Longitud de Hilera especificada (si se ingresó una longitud válida)
            if row_length > 0:
                # Convertir longitud de hilera a metros si la unidad es centímetros
                if unit == "centímetros":
                    row_length_m = row_length / 100.0
                else:  # Asumir metros
                    row_length_m = row_length

                if plant_spacing_m <= 0:  # Evitar división por cero
                    plants_per_row_length = 0
                    messagebox.showwarning(
                        "Error de Cálculo", "El espaciamiento entre plantas es cero, no se puede calcular las plantas por longitud de hilera.")
                    self.plants_per_row_length_var.set("")
                else:
                    plants_per_row_length = row_length_m / plant_spacing_m
                    self.plants_per_row_length_var.set(
                        # Formato sin decimales
                        f"{plants_per_row_length:.0f}")
            else:
                # Limpiar el resultado si no se ingresó una longitud de hilera válida
                self.plants_per_row_length_var.set("")

        except ValueError:
            messagebox.showwarning(
                "Entrada Inválida", "Por favor, ingrese valores numéricos válidos para los espaciamientos y la longitud de hilera.")
            # Limpiar resultados si la entrada es inválida
            self.population_hectare_var.set("")
            self.plants_per_meter_row_var.set("")
            self.plants_per_row_length_var.set("")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")


# --- Ejecutar la Aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = PlantPopulationApp(root)
    root.mainloop()
