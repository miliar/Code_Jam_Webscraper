cases = int(input())

for casenumber in range(cases):
    audiencia = input().split()
    tam = int(audiencia[0])
    pers = [int(i) for i in list(audiencia[1])]
    invitados = 0
    parados = 0
    for shyness in range(len(pers)):
        if parados >= shyness:
            parados = parados + pers[shyness]
        else:
            invitados = invitados + shyness - parados
            parados = parados + pers[shyness] + shyness - parados
    print('Case #' + str(casenumber + 1) + ': ' + str(invitados))

