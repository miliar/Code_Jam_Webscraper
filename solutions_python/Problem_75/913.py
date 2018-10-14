#!/usr/bin/env python3.1

import copy

with open("Magicka.out","w") as out:
    with open("Magicka.in") as input:

        T = int(input.readline())

        for i in range(T):
            magicka=[]
            combines=[]
            opposed=[]
            r = input.readline().split()
            C=int(r[0])

            for j in range(1,C+1):
                combines.append((r[j][0:2],r[j][2:]))

            index = C+1
            D=int(r[index])

            for k in range(index,D+index):
                opposed.append(r[k+1])

            index+=D+1

            N=r[index]
            magicka.append(r[index+1][0])

            for l in r[index+1][1:]:
                ok=0
                mg=copy.copy(magicka)
                if len(combines)>0 and len(magicka)>0:

                    str1=l+magicka[len(magicka)-1]
                    str2=magicka[len(magicka)-1]+l
                    for c in combines:
                        if str1==c[0] or str2==c[0]:
                            magicka = magicka[:len(magicka)-1]
                            magicka.append(c[1])
                            ok=1
                if len(opposed)>0 and len(magicka)>0 and ok==0:
                    for w in mg:
                        str1=w+l
                        str2=l+w
                        for op in opposed:
                            if op==str1 or op==str2:
                                magicka=[]
                                ok=1

                if ok==0 :
                    magicka.append(l)
            out.write("Case #"+str(i+1)+": "+str(magicka)+'\n')
