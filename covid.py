
def validar_dato(dato):
    '''Recibe por parametro un numero, mientras sea menor a cero pide el reingreso, sino
    retorna ese numero (dato)'''
    while dato < 0:
        dato = int(input('El dato ingresado no es valido. Vuelva a ingresarlo: '))
    return dato


def es_bisiesto(aaaa):
    '''Recibe por parametro un numero que representa un año y retorna True si es divisible por 4,
    pero no por 100, excepto que también sea divisible por 400, sino retorna False.'''
    if aaaa % 4 == 0 and not aaaa % 100 == 0:
        return True
    elif aaaa % 400 == 0:
        return True
    else:
        return False


def cant_dia_mes(month, year):
    '''Recibe por parametro dos numeros que representan un mes y un anio
    y devuelve como resultado la cantidad de dias correspondientes al mes'''
    if month > 0 and month <= 12:
        if month == 4 or month == 5 or month == 9 or month == 11:
            return 30
        if month == 2 and es_bisiesto(year) == True:
            return 29
        elif month == 2:
            return 28
        else:
            return 31
    else:
        return False


def verifica_dia(dd, mm, aaaa):
    '''Recibe por parametro tres numeros que representan dia, mes y anio respectivamente, verifica que la cantidad
        de dias sea mayor a cero, y menor o igual que la cantidad de dias correspondientes al mes ingresado, y devuelve True.
        Sino, retorna False.'''
    mes = cant_dia_mes(mm, aaaa)
    if dd > 0 and dd <= mes:
        return True
    if mm == 2 and dd <= mes:
        return True
    else:
        return False


def validar_fecha():
    '''Pide al usuario que ingrese dia, mes y anio; llama a la funcion verifica_dia() y mientras sea distinto de True vuelve a
    pedir los datos al usuario. Cuando sea valido (True), retorna dd,mm,aaaa.
    '''
    dd = int(input('Ingrese el dia: '))
    mm = int(input('Ingrese el mes: '))
    aaaa = int(input('Ingrese el año: '))
    while verifica_dia(dd, mm, aaaa) != True:
        print('La fecha no es valida')
        dd = int(input('Ingrese el dia: '))
        mm = int(input('Ingrese el mes: '))
        aaaa = int(input('Ingrese el año: '))
    return dd, mm, aaaa


def validar_infectados(infectado, test):
    '''Recibe  que representan la cantidad de infectados y los tests respectivamente,
    mientras infectados sea menor a cero o mayor a test vuelve a pedir ambos, sino, retorna infectado'''
    while infectado < 0 or infectado > test:
        infectado = int(input(
            'El dato ingresado no es valido. Vuelva a ingresar la cantidad de casos positivos: '))
    return infectado


def main():

    total_tests = 0
    total_positivos = 0
    total_mun_informados = 0
    total_camas_intensiva = 0
    total_camas_intermedia = 0
    mayor_cant_casos = 0
    total_mun_sin_camas = 0
    cant_mun_informados = 0

    fecha_valida = validar_fecha()

    nombre_municipio = input(
        'Ingrese el nombre de un municipio (* para salir): ')

    while nombre_municipio != '*':

        cant_tests = int(
            input('Ingrese la cantidad de tests realizados en el dia: '))
        test_valido = validar_dato(cant_tests)
        total_tests += test_valido

        cant_casos_pos = int(
            input('Ingrese la cantidad de casos positivos detectados: '))
        infectado_valido = validar_infectados(cant_casos_pos, test_valido)
        total_positivos += infectado_valido

        cant_camas_intermedia = int(
            input('Ingrese la cantidad de camas para terapia intermedia: '))
        intermedia_valida = validar_dato(cant_camas_intermedia)
        total_camas_intermedia += intermedia_valida

        cant_camas_intensiva = int(
            input('Ingrese la cantidad de camas para terapia intensiva: '))
        intensiva_valida = validar_dato(cant_camas_intensiva)
        total_camas_intensiva += intensiva_valida

        if mayor_cant_casos < infectado_valido:
            mayor_cant_casos = infectado_valido

        if intermedia_valida + intensiva_valida == 0:
            total_mun_sin_camas += 1

        if infectado_valido == 0 or test_valido == 0:
            por_casos = 0
        else:
            por_casos = (infectado_valido / test_valido) * 100

        cant_mun_informados += 1

        print('---------------------------------------------------------------------------------------------')
        print('Nombre del municipio: ', nombre_municipio)
        print('Cantidad de tests realizados: ', test_valido)
        print('Cantidad de casos positivos detectados: ', infectado_valido)
        print('Camas intermedias disponibles: ', intermedia_valida)
        print('Camas intensivas disponibles: ', intensiva_valida)
        print('El porcentaje en este municipio es de: ',
              "{:.2f}".format(por_casos), '%')
        print('---------------------------------------------------------------------------------------------')

        nombre_municipio = input(
            'Ingrese el nombre de OTRO municipio (* para salir): ')

        print('---------------------------------------------------------------------------------------------')

    if total_positivos == 0 or total_tests == 0:
        por_total = 0
    else:
        por_total = (total_positivos / total_tests) * 100

    print('---------------------------------------------------------------------------------------------')
    print('Fecha del informe (dd,mm,aaaa): ',
          fecha_valida[0], '/', fecha_valida[1], '/', fecha_valida[2])
    print('El valor total de tests es de: ', total_tests)
    print('El valor total de casos positivos es de : ', total_positivos)
    print('La cantidad total de municipios sin camas es de: ', total_mun_sin_camas)
    print('La mayor cantidad de casos detectados fue de: ', mayor_cant_casos)
    print('El porcentaje sobre el total de casos fue de: ',
          "{:.2f}".format(por_total), '%')
    print('Total de municipios informados: ', cant_mun_informados)


main()
