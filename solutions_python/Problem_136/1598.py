from decimal import *

def cookies(C, F, X):
    cant_cookie = Decimal(2)
    if C > X:
        return X/cant_cookie
    tiempo_inicial = C/cant_cookie
    tiempo_granjeando = 0
    tiempo_anterior = X/(cant_cookie)

    num_granja = 0
    while(1):
        denominador= cant_cookie + F*num_granja
        tiempo_granjeando += C/denominador
        denominador = cant_cookie+ (num_granja+1)*F
        tiempo_para_ganar = X/denominador
        tiempo = tiempo_granjeando + tiempo_para_ganar
        if tiempo > tiempo_anterior:
            return  format(tiempo_anterior, '.15f')    
        else:
            tiempo_anterior = tiempo    
        num_granja+=1
    return format(tiempo,'.15f')


if __name__ == "__main__":
    getcontext().prec = 28

    file_name = "cookies_text"
    objecto_archivo = open(file_name, 'r')
    count_case = int(objecto_archivo.readline()[:-1])

    for number_case in range(0, count_case): 

        frase = "Case #"+str(number_case +1)+": "
        values = objecto_archivo.readline()[:-1]
        values_unico = values.split(" ")
        values_unico = [Decimal(x) for x in values_unico]
        print frase + str(cookies(values_unico[0], values_unico[1], values_unico[2]))

    objecto_archivo.close()


    