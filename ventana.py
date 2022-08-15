from array import array
from ast import Delete
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud import *


class Ventana(Frame):

    paises = CRUD()

    def __init__(self, master=None):
        super().__init__(master, width=865, height=260)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatos()
        self.habilitarCajas("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disabled")
        self.id = -1

    def habilitarCajas(self, estado):
        self.txtISO.configure(state=estado)
        self.txtCiu.configure(state=estado)
        self.txtMCE.configure(state=estado)
        self.txtPais.configure(state=estado)

    def limpiarCajas(self):
        self.txtCiu.delete(0, END)
        self.txtMCE.delete(0, END)
        self.txtISO.delete(0, END)
        self.txtPais.delete(0, END)

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def habilitarBtnOper(self, estado):
        self.btnAgregar.configure(state=estado)
        self.btnEditar.configure(state=estado)
        self.btnBorrar.configure(state=estado)

    def habilitarBtnGuardar(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def llenaDatos(self):
        datos = self.paises.consulta_paises()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(
                row[1], row[2], row[3], row[4]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def fAgregar(self):

        self.habilitarCajas("normal")
        self.habilitarBtnOper("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()
        self.txtISO.focus()

    def fEditar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')

        if clave == '':
            messagebox.showwarning("Editar", "Debes seleccionar un elemento")
        else:
            self.id = clave
            valores = self.grid.item(selected, 'values')
            self.habilitarCajas("normal")
            self.limpiarCajas()
            self.txtISO.insert(0, valores[0])
            self.txtPais.insert(0, valores[1])
            self.txtCiu.insert(0, valores[2])
            self.txtMCE.insert(0, valores[3])

            self.habilitarBtnOper("disabled")
            self.habilitarBtnGuardar("normal")
            self.txtISO.focus()

    def fBorrar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')

        if clave == '':
            messagebox.showwarning("Eliminar", "Debes seleccionar un elemento")
        else:
            valores = self.grid.item(selected, 'values')
            data = str(clave) + ", " + valores[0] + ", " + valores[1]
            r = messagebox.askquestion(
                "Eliminar", "Estas seguro que quieres eliminar el registro seleccionado?\n" + data)
            if r == messagebox.YES:
                n = self.paises.elimina_pais(clave)
                if n == 1:
                    messagebox.showinfo(
                        "Eliminar", "Elemento eliminado correctamente.")
                    self.limpiaGrid()
                    self.llenaDatos()
            else:
                messagebox.showwarning(
                    "Eliminar", "No fue posible eliminar el elemento.")

    def fGuardar(self):
        if self.id == -1:
            self.paises.inserta_pais(self.txtISO.get(), self.txtPais.get(
            ), self.txtCiu.get(), self.txtMCE.get())
            messagebox.showinfo(
                "Insertar", "Elemento insertado correctamente.")
        else:
            self.paises.modifica_pais(self.id, self.txtISO.get(
            ), self.txtPais.get(), self.txtCiu.get(), self.txtMCE.get())
            messagebox.showinfo(
                "Modificar", "Elemento modificado correctamente.")
            self.id = -1
        self.limpiaGrid()
        self.llenaDatos()
        self.limpiarCajas()
        self.habilitarBtnGuardar("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")

    def fCancelar(self):
        self.limpiarCajas()
        self.habilitarBtnGuardar("disabled")
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="#17224D")
        frame1.place(x=0, y=0, width=93, height=259)

        self.btnAgregar = Button(frame1, text="Agregar",
                                 command=self.fAgregar, bg="#4AB19D", fg="white")
        self.btnAgregar.place(x=5, y=40, width=80, height=30)

        self.btnEditar = Button(frame1, text="Editar",
                                command=self.fEditar, bg="#334E5C", fg="white")
        self.btnEditar.place(x=5, y=80, width=80, height=30)

        self.btnBorrar = Button(frame1, text="Borrar",
                                command=self.fBorrar, bg="#E17A47", fg="white")
        self.btnBorrar.place(x=5, y=120, width=80, height=30)

        frame2 = Frame(self, bg="#FFC872")
        frame2.place(x=93, y=0, width=150, height=259)

        lbl1 = Label(frame2, text="ISO30: ", bg="#FFC872")
        lbl1.place(x=2, y=5)

        self.txtISO = Entry(frame2)
        self.txtISO.place(x=3, y=25, width=50, height=20)

        lbl2 = Label(frame2, text="Nombre pais: ", bg="#FFC872")
        lbl2.place(x=2, y=45)

        self.txtPais = Entry(frame2)
        self.txtPais.place(x=3, y=65, width=120, height=20)

        lbl3 = Label(frame2, text="Capital: ", bg="#FFC872")
        lbl3.place(x=2, y=85)

        self.txtCiu = Entry(frame2)
        self.txtCiu.place(x=3, y=105, width=120, height=20)

        lbl4 = Label(frame2, text="Moneda Corriente: ", bg="#FFC872")
        lbl4.place(x=2, y=125)

        self.txtMCE = Entry(frame2)
        self.txtMCE.place(x=3, y=145, width=120, height=20)

        self.btnGuardar = Button(frame2, text="Guardar",
                                 command=self.fGuardar, bg="#4AB19D", fg="white")
        self.btnGuardar.place(x=10, y=210, width=60, height=30)

        self.btnCancelar = Button(frame2, text="Cancelar",
                                  command=self.fCancelar, bg="#E17A47", fg="white")
        self.btnCancelar.place(x=80, y=210, width=60, height=30)

        frame3 = Frame(self, bg="#FFC872")
        frame3.place(x=245, y=0, width=860, height=259)

        self.grid = ttk.Treeview(frame3, columns=(
            "col1", "col2", "col3", "col4"))

        self.grid.column("#0", width=80, anchor=CENTER)
        self.grid.column("col1", width=80, anchor=CENTER)
        self.grid.column("col2", width=165, anchor=CENTER)
        self.grid.column("col3", width=165, anchor=CENTER)
        self.grid.column("col4", width=126, anchor=CENTER)

        self.grid.heading("#0", text="id", anchor=CENTER)
        self.grid.heading("col1", text="ISO30", anchor=CENTER)
        self.grid.heading("col2", text="Nombre pais", anchor=CENTER)
        self.grid.heading("col3", text="Ciudad", anchor=CENTER)
        self.grid.heading("col4", text="Moneda corriente", anchor=CENTER)

        self.grid.pack(side=LEFT, fill=Y)

        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode'] = 'browse'
