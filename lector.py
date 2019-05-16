import json
import glob
import mysql.connector

conexion = mysql.connector.connect(
    port='33065',
    user='root',
    password='',
    database='divec'
)

cursor = conexion.cursor()

files = glob.glob('*.json')

periodo={'16/01/19 - 31/05/19': 1}

def existe_detalle_materia(clave):
    select = 'SELECT * FROM detalle_materia WHERE clave=%s'
    cursor.execute(select,(clave, ))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insert_detalle_materia(reg):
    insert = 'INSERT INTO detalle_materia(clave,nombre,creditos,id_periodo) VALUES(%s, %s, %s, %s)'
    cursor.execute(insert, (reg['clave'],reg['materia'],reg['creditos'],1) )
    conexion.commit()
    id_detalle = cursor.lastrowid
    return id_detalle

def get_id_detalle_m(clave):
    select = 'SELECT id FROM detalle_materia WHERE clave=%s'
    cursor.execute(select,(clave, ))
    rows = cursor.fetchall()
    return rows[0][0]

def existe_carrera(nombre):
    select = 'SELECT * FROM carrera WHERE nombre=%s'
    cursor.execute(select,(nombre, ))

    rows = cursor.fetchall()
    if len(rows)> 0:
        return True
    else:
        return False

def insertar_carrera(nombre):
    insert = 'INSERT INTO carrera(nombre) VALUES(%s)'
    cursor.execute(insert,(nombre, ))
    conexion.commit()
    id = cursor.lastrowid
    return id

def get_id_carrera(nombre):
    select = 'SELECT id FROM carrera WHERE nombre=%s'
    cursor.execute(select, (nombre, ))

    rows = cursor.fetchall()
    return rows[0][0]

def existe_profesor(profesor):
    select = "SELECT id FROM profesor WHERE nombre=%s"
    cursor.execute(select, (profesor, ))

    rows = cursor.fetchall()
    if len(rows)>0:
        return True
    else:
        return False

def insert_profesor(profesor):
    insert = "INSERT INTO profesor(nombre) VALUES(%s)"
    cursor.execute(insert, (profesor, ))
    conexion.commit()

    id_profesor = cursor.lastrowid
    return id_profesor

def get_id_profesor(profesor):
    select = "SELECT id FROM profesor WHERE nombre=%s"
    cursor.execute(select, (profesor, ))

    rows = cursor.fetchall()
    return rows[0][0]


def existe_edificio(nombre):
    select = "SELECT id FROM edificio WHERE edificio=%s"
    cursor.execute(select, (nombre, ))

    rows = cursor.fetchall()
    if len(rows)> 0:
        return True
    else:
        return False


def insertar_edificio(nombre):
    insert = "INSERT INTO edificio(edificio) VALUES(%s)"
    cursor.execute(insert, (nombre, ))
    conexion.commit()
    id_edificio = cursor.lastrowid
    return  id_edificio

def get_id_edificio(nombre):
    select = "SELECT id FROM edificio WHERE edificio = %s"
    cursor.execute(select, (nombre, ))

    rows = cursor.fetchall()
    return rows[0][0]

def existe_dia(dia):
    select ="SELECT id FROM dia WHERE dia=%s"
    cursor.execute(select, (dia, ))


    rows = cursor.fetchall()
    if len(rows)>0:
        return True
    else:
        return  False

def insertar_dia(dia):
    insert = "INSERT INTO dia(dia) values(%s)"
    cursor.execute(insert, (dia, ))
    conexion.commit()

    id_dia = cursor.lastrowid
    return id_dia

def get_id_dia(dia):
    select = "SELECT id FROM dia WHERE dia=%s"
    cursor.execute(select, (dia, ))


    rows = cursor.fetchall()
    return rows[0][0]

def existe_horas(hora):
    select = "SELECT id FROM hora WHERE hora=%s"
    cursor.execute(select, (hora, ))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_hora(hora):
    insert = "INSERT INTO hora(hora) values(%s)"
    cursor.execute(insert, (hora,))
    conexion.commit()

    id_hora = cursor.lastrowid
    return id_dia

def get_id_hora(hora):
    select = "SELECT id FROM hora WHERE hora=%s"
    cursor.execute(select, (hora, ))


    rows = cursor.fetchall()
    return rows[0][0]


def existe_aula(aula):
    select = "SELECT id FROM aula WHERE numero=%s"
    cursor.execute(select, (aula,))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False
def insertar_aula(aula):
    insert = "INSERT INTO aula(numero) VALUES(%s)"
    cursor.execute(insert, (aula, ))
    conexion.commit()

    id_aula = cursor.lastrowid
    return id_aula

def get_id_aula(aula):
    select = "SELECT id FROM aula WHERE numero=%s"
    cursor.execute(select, (aula, ))

    rows = cursor.fetchall()
    return rows[0][0]

def insertar_materia(materia,id_profesor,id_dia,id_hora,id_aula,id_edificio,id_detalle_materia):

    insert = "INSERT INTO materia(nrc,cupos,disponibles,id_profesor,id_dia,id_hora,id_aula,id_edificio,id_detalle_materia) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(insert, (materia['nrc'],
                            materia['cupos'],
                            materia['disponible'],
                            id_profesor,
                            id_dia,
                            id_hora,
                            id_aula,
                            id_edificio,
                            id_detalle_materia,))
    conexion.commit()
    id_materia = cursor.lastrowid
    return id_materia


def insertar_carrera_materia(id_materia,id_carrera):
    insert = "INSERT INTO carrera_materia VALUES(%s,%s)"
    cursor.execute(insert, (id_materia,id_carrera, ))
    conexion.commit()

def existe_reg_in_carrera(id_detalle_materia):
    select = "SELECT id_carrera FROM carrera_materia WHERE id_detalle_materia =%s"
    cursor.execute(select, (id_detalle_materia, ))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def insertar_reg(id_detalle,id_carrera):
    insert = "INSERT INTO carrera_materia(id_detalle_materia,id_carrera) VALUES(%s,%s)"
    cursor.execute(insert, (id_detalle,id_carrera))
    conexion.commit()

def get_id_reg(id_detalle):
    select = "SELECT id_carrera FROM carrera_materia WHERE id_detalle_materia=%s"
    cursor.execute(select, (id_detalle,))

    rows = cursor.fetchall()
    return rows

def verificar_materia(rows, id_carrera):
    id = 0
    for i in rows:
        id = i[0]
        print(id,id_carrera)
        if id == id_carrera:
            return True
    return False


def existe_nrc(nrc):
    select = "SELECT * FROM materia WHERE nrc=%s"
    cursor.execute(select, (nrc, ))

    rows = cursor.fetchall()
    if len(rows) > 0:
        return True
    else:
        return False

def get_id_materia(nrc):
    select = "SELECT id FROM materia WHERE nrc=%s"
    cursor.execute(select, (nrc,))

    rows = cursor.fetchall()
    return rows[0][0]


for file in files:
    with open(file,encoding='utf-8') as f:
        registros = json.load(f)
        for reg in registros:
            id_detalle = 0
            id_carrera = 0
            id_profesor=0
            id_edificio=0
            id_dia =0
            id_hora = 0
            id_aula = 0
            id_materia = 0

            if not existe_detalle_materia(reg['clave']):
                id_detalle = insert_detalle_materia(reg)
            else:
                id_detalle = get_id_detalle_m(reg['clave'])

            if not existe_carrera(file[:-5]):
                id_carrera = insertar_carrera(file[:-5])
            else:
                id_carrera = get_id_carrera(file[:-5])

            if not existe_profesor(reg['maestro']):
                id_profesor = insert_profesor(reg['maestro'])
            else:
                id_profesor = get_id_profesor(reg['maestro'])

            if not existe_edificio(reg['edificio']):
                id_edificio = insertar_edificio(reg['edificio'])
            else:
                id_edificio = get_id_edificio(reg['edificio'])

            if not existe_aula(reg['aula']):
                id_aula = insertar_aula(reg['aula'])
            else:
                id_aula = get_id_aula(reg['aula'])

            if not existe_dia(reg['dias']):
                id_dia = insertar_dia(reg['dias'])
            else:
                id_dia = get_id_dia(reg['dias'])

            if not existe_horas(reg['hora']):
                id_hora = insertar_hora(reg['hora'])
            else:
                id_hora = get_id_hora(reg['hora'])


            id_materia = insertar_materia(reg,id_profesor,id_dia,id_hora,id_aula,id_edificio,id_detalle)


            id_carreras = get_id_reg(id_detalle)
            if  verificar_materia(id_carreras,id_carrera)==False:
                insertar_reg(id_detalle,id_carrera)





