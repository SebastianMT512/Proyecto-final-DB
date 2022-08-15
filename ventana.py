from tkinter import *
from tkinter import ttk


class Ventana(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=865, height=260)
        self.master = master
        self.pack()
        self.create_widgets()

    def fAgregar(self):
        pass

    def fEditar(self):
        pass

    def fBorrar(self):
        pass

    def fGuardar(self):
        pass

    def fCancelar(self):
        pass

    def create_widgets(self):
        frame1 = Frame(self, bg="#17224D")
        frame1.place(x=0, y=0, width=93, height=259)

        self.btnAgregar = Button(frame1, text="Agregar",
                                 command=self.fAgregar, bg="#4AB19D", fg="white")
        self.btnAgregar.place(x=5, y=40, width=80, height=30)

        self.btnEditar = Button(frame1, text="Editar",
                                command=self.fAgregar, bg="#334E5C", fg="white")
        self.btnEditar.place(x=5, y=80, width=80, height=30)

        self.btnBorrar = Button(frame1, text="Borrar",
                                command=self.fAgregar, bg="#E17A47", fg="white")
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
        self.txtPais.place(x=3, y=65, width=50, height=20)

        lbl3 = Label(frame2, text="Capital: ", bg="#FFC872")
        lbl3.place(x=2, y=85)

        self.txtCap = Entry(frame2)
        self.txtCap.place(x=3, y=105, width=50, height=20)

        lbl4 = Label(frame2, text="Moneda Corriente: ", bg="#FFC872")
        lbl4.place(x=2, y=125)

        self.txtMCE = Entry(frame2)
        self.txtMCE.place(x=3, y=145, width=50, height=20)

        self.btnGuardar = Button(frame2, text="Guardar",
                                 command=self.fGuardar, bg="#4AB19D", fg="white")
        self.btnGuardar.place(x=10, y=210, width=60, height=30)

        self.btnCancelar = Button(frame2, text="Cancelar",
                                  command=self.fCancelar, bg="#E17A47", fg="white")
        self.btnCancelar.place(x=80, y=210, width=60, height=30)

        self.grid = ttk.Treeview(self, columns=(
            "col1", "col2", "col3", "col4"))

        self.grid.column("#0", width=50)
        self.grid.column("col1", width=60, anchor=CENTER)
        self.grid.column("col2", width=90, anchor=CENTER)
        self.grid.column("col3", width=90, anchor=CENTER)
        self.grid.column("col4", width=60, anchor=CENTER)

        self.grid.heading("#0", text="id")
        self.grid.heading("col1", text="ISO30", anchor=CENTER)
        self.grid.heading("col2", text="Nombre pais", anchor=CENTER)
        self.grid.heading("col3", text="Capital", anchor=CENTER)
        self.grid.heading("col4", text="Moneda corriente", anchor=CENTER)

        self.grid.place(x=244, y=0, width=620, height=259)

        self.grid.insert("", END, text="1", values=(
            "ARG", "Argentina", "Buenos aires", "ARS"))
