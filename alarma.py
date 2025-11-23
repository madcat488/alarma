import tkinter as tk
import time
from time import strftime
from datetime import datetime
#from pygame import mixer # pip  install pygame
from tkinter import messagebox, Label,Tk,ttk
# se debe instalar la biblioteca
# pip install tkcalendar
import pytz
from tkcalendar import Calendar
# Esto mostraría la fecha en español.
import locale
locale.setlocale(locale.LC_TIME, 'es_AR.UTF-8')

def print_date():
    # aca deberiamos tomar la fecha para agregar una alarma ese dia
    print(cal.selection_get())
    #print(strftime('%Y-%m-%d'))
    alarma_dia = cal.selection_get()
    #hora_actual = now.strftime('%H:%M:%S')
    alarma()


def alarma():
    alarma_hora = combobox_horas.get()
    alarma_minutos = combobox_minutos.get()
    alarma_dia = strftime('%Y-%m-%d')
    hora_actual1 = strftime('%H')
    hora_actual2 = strftime('%M')
    hora_actual3 = strftime('%S')
    if int(hora_actual3)== 0:
        if int(hora_actual1) == int(alarma_hora):
            if int(hora_actual2) == int(alarma_minutos):
                #mixer.music.load("alarma.mp3")
                #mixer.music.play(loops=1)
                messagebox.showinfo(message='alarma sonando',title="Alarma")
    
ZONAS_HORARIAS = {
    "Argentina (Buenos Aires)": "America/Argentina/Buenos_Aires",
    "España (Madrid)": "Europe/Madrid",
    "México (Ciudad de México)": "America/Mexico_City",
    "Estados Unidos (Nueva York)": "America/New_York",
    "Reino Unido (Londres)": "Europe/London",
    "Japón (Tokio)": "Asia/Tokyo",
    "Australia (Sídney)": "Australia/Sydney",
    "Alemania (Berlín)": "Europe/Berlin",
}

zona_horaria_seleccionada = "America/Argentina/Buenos_Aires" 
# para actializar el diccionario deberiamos:
# ZONAS_HORARIAS[nombre_mostrar] = id_zona
# print(f"Se agregó '{nombre_mostrar}' a la lista.")
# print("-" * 20)

# la funcion que actualiza la zona horaria
def actualizar_zona(seleccion):
    global zona_horaria_seleccionada
    # Busca el valor de la zona horaria (ej: 'America/New_York') a partir del nombre (ej: 'Estados Unidos...')
    zona_horaria_seleccionada = ZONAS_HORARIAS[seleccion]
    # Imprime la nueva zona seleccionada (opcional, para depuración)
    print(f"Zona horaria actualizada a: {zona_horaria_seleccionada}")
    # Llama a actualizar_reloj inmediatamente para refrescar la hora
    actualizar_reloj()

def actualizar_reloj():
    alarma()
    try:
        # 1. Obtener el objeto de zona horaria de pytz
        tz = pytz.timezone(zona_horaria_seleccionada)
        # 2. Obtener la hora actual en esa zona horaria
        now = datetime.now(tz)
        # 3. Formatear la hora
        hora_actual = now.strftime('%H:%M:%S')
        # 4. Formatear la fecha
        fecha_actual = now.strftime('%A, %d de %B de %Y')
        # 5. Actualizar los widgets
        etiqueta_reloj.config(text=hora_actual)
        etiqueta_fecha.config(text=fecha_actual)

    except Exception as e:
        print(f"Error al actualizar el reloj: {e}")
        etiqueta_reloj.config(text="ERROR")
    # Programar la función para que se vuelva a llamar después de 1000 ms (1 segundo)
    etiqueta_reloj.after(1000, actualizar_reloj)

# 1. Configuración de la Ventana Principal

###

# root se llama la ventana principal hay que cambiar el nombre es muy feo
root = tk.Tk()
# root.geometry('1000x1000')
# el titulo que tiene la ventana
root.title('Reloj simple GRUPO 4')
# para poner el dia actual
root.configure(bg="#000000")
#mixer.init()

# Dividimos la pantalla para mostrar el calendario a un lado.
frame_izq = tk.Frame(root, bg="#000000")
frame_der = tk.Frame(root, bg="#000000")
frame_izq.pack(side=tk.LEFT, padx=20, pady=10)
frame_der.pack(side=tk.RIGHT, padx=20, pady=10)

# Esto se verá en la parte izquierda del reloj. 
cal = Calendar (frame_izq, selectmode='day', 
                year=int(time.strftime('%Y')), 
                month = int(time.strftime('%m')), 
                day = int(time.strftime('%d')),
                font= ("Times New Roman", 20))
# el pady es el espacio hay entre el calendario y los demas objetos en este caso son todos los pady el de abajo el de arriba y el de los costados
cal.pack(pady=1)

#coloca el boton en la ventana
tk.Button(frame_izq, text='Seleccionar Fecha y hora de alarma', command=print_date).pack(pady=1)

lista_horas=[]
lista_minutos=[]
for i in range(0,24):
    lista_horas.append(i)
for i in range(0,60):
    lista_minutos.append(i)

texto_tiempo= Label(root,text= 'alarma',bg='black',fg='magenta',font=('Arial',12,'bold'))
texto_tiempo.pack(side=tk.LEFT,padx=1, pady=1)

combobox_horas = ttk.Combobox(root, values = lista_horas, style= "TCombobox", justify='center', width='5', font='Arial')
combobox_horas.pack(side=tk.LEFT,padx=10, pady=10)
combobox_horas.current(0)
texto_tiempo1= Label(root,text= ':',bg='black',fg='magenta',font=('Arial',12,'bold'))
texto_tiempo1.pack(side=tk.LEFT,padx=1, pady=1)
combobox_minutos = ttk.Combobox(root, values = lista_minutos, style= "TCombobox", justify='center', width='5', font='Arial')
combobox_minutos.pack(side=tk.LEFT,padx=10, pady=10)
combobox_minutos.current(0)

# Esto va en la parte derecha.
# 5. Etiqueta para la Fecha
etiqueta_fecha = tk.Label(
    frame_der,
    font=('Times New Roman', 20, 'bold italic'),
    background='#000000',
    foreground='#EEEEEE'
)
# buscar como se hace para poner en español puede ser con un metodo segun o ir a la funcion
etiqueta_fecha.pack(pady=20)

## ....................................... actualizar zona horaria del proyecto de braian

# le da un color de fondo
root.configure(bg="#000000")
# 2. Crear la variable para el menú desplegable
pais_var = tk.StringVar(root)
# Establecer el valor inicial (Argentina)
pais_var.set(list(ZONAS_HORARIAS.keys())[0])
# boton menu

# 3. Creación del Menú Desplegable (OptionMenu)
menu_desplegable = tk.OptionMenu(
    frame_der, 
    pais_var, 
    *ZONAS_HORARIAS.keys(), # Desempaqueta las claves (nombres de los países)
    command = actualizar_zona) # La función a llamar cuando se cambia la selección
menu_desplegable.config(
    font=('Arial', 14), 
    bg="#393E46", 
    fg="#EEEEEE",
    width=20)
menu_desplegable.pack(pady=10)

# 4. Etiqueta para la Hora
etiqueta_reloj = tk.Label(frame_der,
                          font=('Digital-7', 70, 'bold'),
                          background='#000000',
                          foreground='#00ADB5',
                          padx=10, pady=10)
etiqueta_reloj.pack(padx=10, pady=10)

entrada_nombre = tk.Entry(frame_der, font=("Helvetica", 14), fg="gray")
entrada_nombre.insert(0, "Ej: Perú (Lima)")
entrada_nombre.pack(pady=5)

entrada_zona = tk.Entry(frame_der, font=("Helvetica", 14), fg="gray")
entrada_zona.insert(0, "Ej: America/Lima")
entrada_zona.pack(pady=5)

# 5. para gregar una nueva zona horaria
def agregar_zona():
    # Toma los datos que se ingresen y los agrega al diccionario "ZONAS HORARIAS"
    nombre = entrada_nombre.get().strip()
    zona = entrada_zona.get().strip() 
    # Agrega al diccionario y al menú desplegable
    ZONAS_HORARIAS[nombre] = zona
    menu_desplegable['menu'].add_command(label=nombre, 
                                         command=tk._setit(pais_var, nombre, actualizar_reloj))
    print(f"Zona agregada: {nombre} -> {zona}")

# Botón para ejecutar la función anterior
tk.Button(
    frame_der,
    text="Agregar Zona Horaria",
    command=agregar_zona,
    bg="#00ADB5",
    fg="white",
    font=("Arial", 12, "bold")
).pack(pady=10)

# 6. Iniciar el Reloj
actualizar_reloj()



# para que la ventana se muestre siempre
root.mainloop()