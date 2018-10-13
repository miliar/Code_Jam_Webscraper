T = int(input(''))
for i in range(T):
    s = input('')
    z = s.split()
    x = int(z[0])
    z = z[1:]
    dict = {1 : 1}
    for j in range(x):
        a = z[0]
        dict[a[0:2]] = a[2]
        z = z[1:]
    opp = []
    x = int(z[0])
    z = z[1:]
    for j in range(x):
        a = z[0]
        opp.append(a)
        z = z[1:]
    x = z[0]
    z = z[1:]
    s = z[0]
    pismena = []
    for j in s:
        pismena.append(j)
        if (len(pismena) > 1):
            o1 = pismena[-1]+pismena[-2]
            o2 = pismena[-2]+pismena[-1]
            if (o1 in dict.keys()):
                pismena = pismena[:-2]
                pismena.append(dict[o1])
            elif (o2 in dict.keys()):
                pismena = pismena[:-2]
                pismena.append(dict[o2])     
            oppo = 0
            for k in pismena[:-1]:
                o3 = pismena[-1]+k
                o4 = k+pismena[-1] 
                if ((o3 in opp) or (o4 in opp)):
                    oppo = 1
            if (oppo == 1):
                pismena = []
    print('Case #'+str(i+1)+':',pismena)