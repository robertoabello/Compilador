from tkinter import*
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog
import  mini_c_parser
import sys


class FandY(object):
  """docstring for IDE-FandY"""
  def __init__(self):
    

       self.root = Tk()
       self.root.title('IDE-FandY')
       self.root.geometry('400x400')
       self.root.geometry('900x900')

       self.root.config(bg="silver")

       self.area_texto = Text(bg="white",font=("Time new roman",14),selectbackground="green",fg="black")
       self.area_texto.pack(expand=True,fill=BOTH,padx=10,pady=50)
              

       self.menubar = Menu(self.root)
       self.filemenu = Menu(self.menubar,tearoff=0)

       self.filemenu.add_command(label = "Nuevo archivo")
       self.filemenu.add_command(label = "Abrir archivo",command=self.Abrir)
       self.filemenu.add_command(label = "Guardar como...",command=self.Guardar_como)
       self.filemenu.add_command(label = "Guardar",command=self.Guardar)
       self.filemenu.add_command(label = "Salir",command = self.Salir)
       self.menubar.add_cascade(label="Archivo",menu=self.filemenu)

       self.Corrermenu = Menu(self.menubar,tearoff=0)
       self.Corrermenu.add_command(label = "Correr",command=self.Correr)
       self.menubar.add_cascade(label="Ejecutar",menu=self.Corrermenu)
       

       self.Ayudamenu = Menu(self.menubar,tearoff=0)
       self.Ayudamenu.add_command(label = "Aceca de IDE-FandY",command=self.Acerca_de)
       self.Ayudamenu.add_command(label = "Ayuda")
       self.menubar.add_cascade(label="Ayuda",menu=self.Ayudamenu)
       self.Mensaje = Text(self.root)
       self.Mensaje.pack(fill=BOTH,padx=1,pady=5)

       self.root.config(menu=self.menubar)
       self.root.mainloop()  
      
       self.abrir_Archivo = "No_archivo"

  def Correr(self):

      mini_c_parser.VERBOSE = 1     
      mini_c_parser.parser.parse(self.area_texto.get(1.0,END), tracking=True)

      print(mini_c_parser.mensaje)

  def Acerca_de(self):
	
	    messagebox.showinfo(title="Acerca de",message="\tIDE-FandY\n\nCreador: Fredys Marquez Duque")
	    
  def Salir(self):
   
      salir = messagebox.askokcancel(title="Salir",message ="¿Estàs seguro?" )
   
      if salir>0:
         self.root.destroy()


  def Guardar_como(self):

       _archivo = filedialog.asksaveasfile(mode="w", defaultextension=".FandY")


       if _archivo is None:
    	   return

       auxiliarsalvar = self.area_texto.get(1.0,END)

       self.abrir_Archivo = _archivo.name
    
       _archivo.write(auxiliarsalvar)
       _archivo.close()


  def Abrir(self):

      
      abrir = filedialog.askopenfile(initialdir="/",title="Selecionar archivo",filetypes=(("Archivo de textos","*.FandY"),("todos los archivos","*.*"))) 
      if abrir!=None:

            self.area_texto.delete(1.0,END)

           
            for x in abrir:
               self.area_texto.insert(END,x)
                           
            self.abrir_Archivo = abrir.name
            abrir.close()
  
  def Guardar(self):

    
      if self.abrir_Archivo == "No archivo":
          self.Guardar_como()
      else:
         _archivo = open(self.abrir_Archivo,"w+")
         _archivo.write(self.area_texto.get(1.0,END))
         _archivo.close()   



 
if __name__ == '__main__':
    Editor = FandY()


