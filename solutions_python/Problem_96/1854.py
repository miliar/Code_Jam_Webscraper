input_file = open("C:\\B-small-attempt1.in", 'r')
output_file = open("C:\\B-small-attempt1_salida.in", 'w')
t = int(input_file.readline())
for i in range(0,int(t)):
    count = 0
    need_surprising = 0
    entra = input_file.readline()
    valores = entra.split()
    googlers = int(valores[0])
    surprising = int(valores[1])
    p = int(valores[2])
    for j in range(3, len(valores)):
        puntaje = int(valores[j])
        if puntaje%3 == 0:
            if(puntaje/3 >= p):
                count = count + 1
            elif((puntaje+3)/3 >= p) & ((puntaje-3)/3 > 0):
                need_surprising = need_surprising + 1
        if(puntaje%3 == 1):
            if((puntaje+2)/3 >= p):
                count = count + 1
        if(puntaje%3 == 2):
            if((puntaje+1)/3 >= p):
                count = count + 1
            elif((puntaje+4)/3 >= p):
                need_surprising = need_surprising + 1
    if(need_surprising > surprising):
        count = count + surprising
    else:
        count = count + need_surprising
    output_file.write("Case #" + str(i+1) + ": " + str(count) + "\n")
input_file.close()
output_file.close()
        
