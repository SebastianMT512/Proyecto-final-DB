import mysql.connector


class CRUD:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root",
                                           passwd="Ingenieria2020", database="final")

    def __str__(self):
        datos = self.consulta_tablas()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_tablas(self):
        cur = self.cnn.cursor()
        cur.execute("SHOW TABLES")
        datos = cur.fetchall()
        cur.close()
        return datos

    def consulta_paises(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM pais")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_pais(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM pais WHERE id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def inserta_pais(self, ISO3, NombrePais, Ciudad, Moneda):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO pais (ISO3, nombre_pais, ciudad_id, moneda_corriente) 
        VALUES('{}', '{}', '{}', '{}')'''.format(ISO3, NombrePais, Ciudad, Moneda)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def elimina_pais(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM pais WHERE id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_pais(self, Id, ISO3, NombrePais, Ciudad, Moneda):
        cur = self.cnn.cursor()
        sql = '''UPDATE pais SET ISO3='{}', nombre_pais='{}', ciudad_id='{}',
        moneda_corriente='{}' WHERE Id={}'''.format(ISO3, NombrePais, Ciudad, Moneda, Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
