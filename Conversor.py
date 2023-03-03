#App para convertir pies a metros usando tkinter.
#Carlos Samuel Enriquez Plascencia.
#23 de febrero 2023

from tkinter import * #importar libreria tkinter
from tkinter import ttk

class Conversor:
    def __init__(self, raiz):
        #init sirve como constructor de la clase(), self que hace referencia a los elementos de la misma clase.
        raiz.title("Pies a metros")
        #la raiz es nuestra ventana base #self da a conocer los atributos.
        self.pies = StringVar()
        self.metros = StringVar()
        
        mainFrame=ttk.Frame(raiz) #Widgets transparentes #Instancia de raiz
        mainFrame.grid(column=0, row=0)
        
        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies)
        piesEntry.grid()
        piesEntry.grid(column=1,row=0)
        
        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0) #Objeto
        ttk.Label(mainFrame, text="Son equivalenes a").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)
        
        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2)
        raiz.bind("<Return>", self.calcular)   #Buscar tablas de estandares de las letras.
        
    def calcular(self, *args): #Agregar en evento calcular el args arreglo de parametros
        print("Boton presionado: ")
        piesUsuario=self.pies.get() #Siempre devuelve una cadena
        print("Pies ingresados: ", piesUsuario) 
        piesFlotante =float(piesUsuario) #Conversio de cadena a flotante
        metros=piesFlotante * 0.3048
        print("Metros:",metros)
        self.metros.set(metros)
            
            
if __name__=="__main__":
    print("Nada mas se mostrara si es el principal.")     
    print("Nada mas se mostrara esto si es el principal.")
    
 
 