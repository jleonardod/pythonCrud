def listarCursos(cursos):
    print("Cursos: ")
    contador = 1
    for cur in cursos:
        datos = "{0}. Codigo: {1} | Nombre: {2} ({3} creditos)"
        print(datos.format(contador, cur[0], cur[1], cur[2]))
        contador = contador+1
    print(" ")

def pedirDatosRegistro():
    codigo = input("Ingrese código: ")
    nombre = input("Ingrese nombre: ")
    creditos = input("Ingrese créditos: ")

    curso = (codigo, nombre, creditos)
    return curso

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese el codigo a editar: ")

    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break
        
    if existeCodigo:
        nombre = input("Ingrese nombre: ")
        creditos = input("Ingrese créditos: ")
        curso = (codigoEditar, nombre, creditos)
        return curso
    else:
        curso = None

    return curso
        

def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el codigo a eliminar: ")

    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break
        
    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar