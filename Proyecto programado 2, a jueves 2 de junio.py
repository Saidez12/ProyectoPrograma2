# Proyecto programado 2, a sábado 28 de mayo
# Rubén David Abarca Ramírez - 2022017072
# Saimon Hernández Venegas - 2022090508
# Daniel Rubén Arce Madriz


from asyncio.windows_events import NULL
import tkinter as tk
import pickle
from tkinter import *
from tkinter import messagebox
from typing import Any, Hashable,Iterable,Optional

cantidadEquiposVentana = tk.Tk()

cantidadEquiposVentana.resizable(False, False)
cantidadEquiposVentana.geometry("275x125")
cantidadEquiposVentana.title("Equipos")

def ingresoEquipos (event):
    infoEquiposVentana= tk.Toplevel(cantidadEquiposVentana)
    infoEquiposVentana.protocol("WM_DELETE_WINDOW", on_closing)
    infoEquiposVentana.resizable(False, False)
    infoEquiposVentana.geometry("430x225")
    infoEquiposVentana.title("Información de los equipos")
    x = cantidadEquiposVentana.winfo_x()
    y = cantidadEquiposVentana.winfo_y()
    infoEquiposVentana.geometry("+%d+%d" % (x+75, y+75))

    def obtenerYGuardar():
        cantidadJugadores = int(entCantidadJugadores.get())
        procedencia = entLugarProcedencia.get()
        nombre = entNombreEquipo.get()
        valorPlanilla = int(entValorPlanilla.get())
        entCantidadJugadores.delete (0,"end")
        entLugarProcedencia.delete (0,"end")
        entNombreEquipo.delete (0,"end")
        entValorPlanilla.delete (0,"end")
        guardarDiccionario(cantidadJugadores,procedencia, nombre, valorPlanilla)

    def agregarEquipo(event):
        indice  = estadoActual["indice"]
        indice+=1
        estadoActual["indice"] = indice
        if(indice < cantidadEquipos):
            obtenerYGuardar()
            if(indice == cantidadEquipos-1):
                intermedio()
        else:
            intermedio()

    def editarEquipo(event):
        almacenarModificaciones()
        intermedio()

    def guardarDiccionario (cantidadJugadores,procedencia, nombre, valorPlanilla):
        equipos = estadoActual["equipos"]
        codigo = estadoActual["codigo"]
        if(codigo < cantidadEquipos):
            equipos[codigo] = {"Cantidad de jugadores": cantidadJugadores, "Lugar de procedencia": procedencia, "Nombre del equipo": nombre, "Valor de la planilla":valorPlanilla}
            estadoActual["codigo"] = estadoActual["codigo"]+1
        with open("data.json","wb") as fp:
            pickle.dump(equipos,fp)
        with open("data.json","rb") as fp:
            data = pickle.load(fp)
        print(data)

    def intermedio():
        winVentana3= tk.Toplevel(infoEquiposVentana)
        winVentana3.resizable(False, False)
        winVentana3.geometry("300x150")
        winVentana3.title("Modificar un equipo")
        x = infoEquiposVentana.winfo_x()
        y = infoEquiposVentana.winfo_y()
        winVentana3.geometry("+%d+%d" % (x+75, y+75))
        #.withdraw a winVentana4 en la "segunda corrida"
        infoEquiposVentana.withdraw()
        winVentana3.protocol("WM_DELETE_WINDOW", on_closing)
        lblEquiposGuardados = tk.Label(
            winVentana3, text="Los equipos se han guardado satisfactoriamente")
        lblEquiposGuardados.place(x=15, y=25)
        btnIniciar = tk.Button(
            winVentana3, text="INICIAR CAMPEONATO", bg="#926359", fg="#FFFFFF")
        btnModificar = tk.Button(
            winVentana3, text="MODIFICAR", bg="#926359", fg="#FFFFFF")
        btnModificar.place(x=25, y=75)
        btnModificar.bind("<Button-1>", modificarDiccionario)
        btnIniciar.place(x=125, y=75)
        #btnIniciar.bind("<Button-1>", campeonato)

    def almacenarModificaciones():
        codigo = estadoActual["codigo"]
        equipos = estadoActual["equipos"]
        cantidadJugadores = int(entCantidadJugadores.get())
        procedencia = entLugarProcedencia.get()
        nombre = entNombreEquipo.get()
        valorPlanilla = int(entValorPlanilla.get())
        equipos[codigo] = {"Cantidad de jugadores": cantidadJugadores, "Lugar de procedencia": procedencia, "Nombre del equipo": nombre, "Valor de la planilla":valorPlanilla}
        with open("data.json","wb") as fp:
            pickle.dump(equipos,fp)
        with open("data.json","rb") as fp:
            data = pickle.load(fp)
        print(data)

    def modificarDiccionario(event):
        winVentana4= tk.Toplevel(cantidadEquiposVentana)
        winVentana4.resizable(False, False)
        winVentana4.geometry("375x125")
        winVentana4.title("Modificar un equipo")
        x = 100
        y = 200
        winVentana4.geometry("+%d+%d" % (x+75, y+75))
        winVentana4.protocol("WM_DELETE_WINDOW", on_closing)
        #winVentana3.withdraw()
        lblEquipoAModificar = tk.Label(
            winVentana4, text="Indique el nombre del equipo que desea modificar la información: ")
        lblEquipoAModificar.place(x=10, y=25)
        entEquipoAModificar = tk.Entry(
            winVentana4, fg="White", bg="Black", width=15)
        entEquipoAModificar.place(x=125, y=55)
        btnModificarEquipo = tk.Button(
            winVentana4, text="MODIFICAR", bg="#926359", fg="#FFFFFF")
        btnModificarEquipo.place(x=25, y=75)


        def buscarEquipo (event):
            nombreEquipoAModificar = entEquipoAModificar.get()
            estadoActual["equipos"] = equipos
            for y in range(len(equipos)):
                codigo = y
                equipoAModificar=list(equipos[codigo].values())
                equipo = equipoAModificar[2]
                if(equipo == nombreEquipoAModificar):
                    print(equipos[codigo])
                    estadoActual["equipoActual"] = equipos[codigo]
                    estadoActual["codigo"] = codigo
                    ingresoEquipos(event)
                    break
                else:
                    continue
        btnModificarEquipo.bind("<Button-1>", buscarEquipo)

    entNombreEquipo = tk.Entry(
        infoEquiposVentana, fg="White", bg="Black", width=10)
    entLugarProcedencia = tk.Entry(
        infoEquiposVentana, fg="White", bg="Black", width=10)
    entCantidadJugadores = tk.Entry(
        infoEquiposVentana, fg="White", bg="Black", width=10)
    entValorPlanilla = tk.Entry(
        infoEquiposVentana, fg="White", bg="Black", width=10)
    lblNombreEquipo = tk.Label(
        infoEquiposVentana, text="Indique el nombre del equipo: ")
    lblLugarProcedencia = tk.Label(
        infoEquiposVentana, text="Indique el lugar de procedencia del equipo: ")
    lblCantidadJugadores = tk.Label(
        infoEquiposVentana, text="Indique la cantidad de jugadores: ")
    lblValorPlanilla = tk.Label(
        infoEquiposVentana, text="Indique el valor de la planilla: ")
    lblNombreEquipo.place(x=10, y=25)
    entNombreEquipo.place(x=330, y=25)
    lblLugarProcedencia.place(x=10, y=50)
    entLugarProcedencia.place(x=330, y=50)
    lblCantidadJugadores.place(x=10, y=75)
    entCantidadJugadores.place(x=330, y=75)
    lblValorPlanilla.place(x=10, y=100)
    entValorPlanilla.place(x=330, y=100)
    btnContinuarIngreso = tk.Button(
        infoEquiposVentana, text="CONTINUAR", bg="#926359", fg="#FFFFFF")
    btnContinuarIngreso.place(x=175, y=175)
    btnContinuarIngreso.unbind("<Button-1>")
    equipoActual  = estadoActual["equipoActual"]

    if(equipoActual == NULL):
        cantidadEquipos = int(entCantidadEquipos.get())
        equipos = {}
        estadoActual["equipos"] = equipos
        cantidadEquiposVentana.withdraw()
        btnContinuarIngreso.bind("<Button-1>", agregarEquipo)
    else:
        entNombreEquipo.insert(0, equipoActual["Nombre del equipo"])
        entValorPlanilla.insert(0, equipoActual["Valor de la planilla"])
        entLugarProcedencia.insert(0, equipoActual["Lugar de procedencia"])
        entCantidadJugadores.insert(0, equipoActual["Cantidad de jugadores"])
        btnContinuarIngreso.bind("<Button-1>", editarEquipo)


def on_closing():
    if messagebox.askokcancel("Salir", "Desea salir de la aplicación?"):
        cantidadEquiposVentana.quit()


estadoActual = {"indice" : -1,"equipos" : NULL, "equipoActual": NULL, "codigo": 0}


cantidadEquiposVentana.title("Ingreso al campeonato")
cantidadEquiposVentana.eval("tk::PlaceWindow . center")
entCantidadEquipos = tk.Entry(
    cantidadEquiposVentana, fg="White", bg="Black", width=10,text="2")
lblCantidadEquipos = tk.Label(
    cantidadEquiposVentana, text="Indique la cantidad de equipos: ")
btnContinuar = tk.Button(
    cantidadEquiposVentana, text="Continuar...", bg="#926359", fg="#FFFFFF")
lblCantidadEquipos.place(x=10, y=25)
entCantidadEquipos.place(x=190, y=25)
btnContinuar.place(x=100, y=75)
btnContinuar.bind("<Button-1>", ingresoEquipos)
cantidadEquiposVentana.protocol("WM_DELETE_WINDOW", on_closing)
cantidadEquiposVentana.mainloop()
