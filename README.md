A. Análisis del problema. ---------

Se debe desarrollar un prototipo de software que permita representar el registro diario de casos detectados de COVID-19 en municipios del conurbano bonaerense.
El programa debe solicitar, al usuario responsable del sistema, el ingreso de la fecha del informe y, por cada municipio del que se reciba información, los siguientes datos: el nombre del municipio, la cantidad de testeos realizados en el día, la cantidad de casos positivos de COVID-19 detectados y las cantidades de camas disponibles, distinguiendo entre camas de terapia intensiva y camas de terapia intermedia.
Dicho prototipo debe ofrecer las siguientes prestaciones:
    • Controlar la validez de la fecha de proceso y, para cada municipio, controlar los siguientes criterios de validez: que la cantidad de testeos realizados sea mayor que cero; que la cantidad de casos positivos sea mayor o igual a cero, pero menor o igual que la cantidad de testeos; que la cantidad de camas sea mayor o igual a cero (tanto para terapia intensiva, como terapia intermedia). Si algún dato ingresado es incorrecto, se deberá reingresar hasta que resulte válido.
    • Calcular el porcentaje de casos de COVID-19 detectados en cada municipio informado, para mostrarlo en pantalla, simultáneamente, con todos los datos válidos del municipio.
    • Determinar y mostrar la cantidad total de municipios informados, la cantidad total de testeos realizados, la cantidad total de casos positivos de COVID-19, el porcentaje de casos positivos de COVID-19 respecto de la cantidad total de testeos, la mayor cantidad de casos positivos de COVID-19 registrados en un municipio y la cantidad de municipios sin camas disponibles (tanto para terapia intensiva, como terapia intermedia). 
Para calcular el porcentaje de casos de COVID-19 detectados se utiliza la fórmula: 
porc_casos = (cant_posi / cant_test) x 100
porc_casos: Porcentaje de casos de COVID-19 detectados
cant_posi: Cantidad de casos positivos de COVID-19
cant_test: Cantidad de testeos realizados



B. Especificación de la solución. -------

El programa debe solicitar el ingreso de  la fecha del informe y los datos de cada municipio informado, controlando la validez de algunos de los datos ingresados, y cuando un dato sea erróneo, el programa deberá pedir su reingreso hasta que resulte válido (ver en Datos de entrada los datos ingresados y los criterios de validación).  
Debe calcular el porcentaje de casos de COVID-19 detectados en cada municipio y mostrarlo junto a los demás datos válidos del municipio: nombre del municipio, cantidad de testeos realizados en el día, cantidad de casos positivos de COVID-19 detectados y cantidad de camas disponibles, tanto de terapia intensiva, como de terapia intermedia. 
Además, debe calcular y mostrar la cantidad total de municipios informados, la cantidad total de testeos realizados, la cantidad total de casos positivos de COVID-19, el porcentaje de casos positivos de COVID-19 respecto a la cantidad total de testeos realizados, la mayor cantidad de casos positivos registrados en un municipio y la cantidad total de municipios sin camas disponibles (tanto de terapia intensiva, como de terapia intermedia).
Para calcular el porcentaje de casos positivos de COVID-19 se utilizará la siguiente formula: 
Porcentaje de casos COVID-19  = (cantidad de casos COVID-19 / cantidad de testeos) * 100


Datos de entrada:
Para la fecha de ingreso: (debe ser válida)
Día del informe
Mes del informe
Año del informe
Por cada municipio:
Nombre del municipio
Cantidad de testeos realizados en el día ( > cero ) ← (D. E. validación)
Cantidad de casos positivos COVID-19 ( >= cero y <= cantidad de testeos realizados )
Cantidad de camas disponibles en terapia intensiva ( >= cero )
Cantidad de camas disponibles en terapia intermedia ( >= cero )



Datos de salida:
Fecha de ingreso (Día/Mes/Año)
Por cada municipio: 
Nombre del municipio
Cantidad de testeos realizados en el día
Cantidad de casos positivos de COVID-19 detectados
Cantidad de camas disponibles en terapia intensiva
Cantidad de camas disponibles en terapia intermedia
Porcentaje de casos de COVID-19 detectados
Cantidad total de municipios informados
Cantidad total de testeos realizados
Cantidad total de casos positivos de COVID-19
Porcentaje de casos de COVID-19 detectados sobre el total
Mayor cantidad de casos positivos registrados en un municipio
Cantidad total de municipios sin camas disponibles

C. Diseño de la solución. ---------

Función main:
Se asigna valor cero a las variables: cant_mun_informados, total_tests, total_infectados, acum_camas_intensiva, acum_camas_intermedia, mun_sin_camas, max_cant_casos.
Se le solicita al usuario que ingrese día, mes, año y se asignan sus valores a las variables dia, mes, año respectivamente
Se definen las funciones validar_datos, validar_infectados y porcentaje_infectados. 
Se asigna a la variable fecha_valida el valor de la función validar_fecha(dia, mes, año).
Se solicita al usuario el nombre de un municipio (nombre_municipio) y 
Se inicia un ciclo While con centinela, mientras nombre_municipio sea distinto de '*'.

Se pide al usuario que ingrese cantidad de tests realizados (cant_test) y se asigna a la variable test_valido el valor de la función validar_datos(cant_test). Luego total_tests acumulará el valor de test_valido.
Se pide al usuario que ingrese cantidad de casos positivos (cant_posi) y se asigna a la variable infectado_valido el valor de la función validar_infectados(cant_posi). Luego total_infectados acumulará el valor de infectado_valido.
Se pide al usuario que ingrese cantidad de camas de terapia intensiva (camas_intensiva) y se asigna a la variable intensiva_valido el valor de la función validar_datos(camas_intensiva). Luego acum_camas_intensiva acumulará el valor de intensiva_valido.
Se pide al usuario que ingrese cantidad de camas de terapia intermedia (camas_intermedia) y se asigna a la variable intermedia_valido el valor de la función validar_datos(camas_intermedia). Luego acum_camas_intermedia acumulará el valor de intermedia_valido.
Mientras max_cant_casos < infectado_valido, se le asignará a max_cant_casos el valor de infectado_valido.
Si la suma entre intermedia_valida e intensiva_valida es igual a cero, se incrementará en uno mun_sin_camas.
Se llama a la función porcentaje_infectados y se asigna su valor a porc_casos
La variable total_mun_informados aumentará en uno. 

Se mostrará en pantalla el resultado de las variables: nombre_municipio, tests_valido, infectado_valido, intermedia_valida, intensiva_valida, porc_casos.
Por último se volverá a pedir al usuario que ingrese el nombre de un municipio.
Fuera del While:

Se llama a la función porcentaje_infectados y se asigna su valor a porc_total.
Luego se mostrará en pantalla, fecha_valida, cant_mun_informados, total_tests, total_infectados, max_cant_casos, porcentaje_total, mun_sin_camas.


------

Especificación de funciones:
    • es_bisiesto(año): Recibe por parámetro un número que representa el año y retorna True si el valor es divisible por 4 y 400 pero no es divisible por 100; sinó retorna False.
    • cant_dia_mes(mes,año): Recibe por parámetro un número que representa mes y un año y llama a la función es_bisiesto(año). Devuelve la cantidad de días correspondientes al mes dependiendo si el año ingresado es, o no bisiesto.
    • validar_fecha (dd, mm, aaaa): Recibe por parámetro 3 números (dd, mm, aaaa) que representan día, mes y año; llama a la función cant_dia_mes (mes, año). Devuelve día, mes, año.
    • validar_datos(dato): Recibe por parámetro un número y lo valida mientras que sea menor a cero; luego lo retorna.
    • validar_infectados(dato): Recibe por parámetro un número de infectados y lo valida mientras sea menor a cero y mayor a test_valido; luego lo retorna.
    • porcentaje_infectados (infectados, test): Recibe por parámetro dos números y verifica, si ambos son igual a cero, sino realiza el cociente entre infectados y test por cien. Asigna el valor a por_casos y lo retorna.
