#from __future__ import division
from operator import itemgetter


def main():
    entrada=open('B-large.in', 'r')
    saida=open('ZZZZ.out','w')
    casos = int(entrada.readline())
    debug = [21]
    for ii in range(1,casos+1):
        tat = int(entrada.readline())
        n = entrada.readline().strip("\n").split(" ")
        a = []
        for na in range(int(n[0])):
            a.append(entrada.readline().strip("\n").split(" "))

        b = []
        for nb in range(int(n[1])):
            b.append(entrada.readline().strip("\n").split(" "))

        sorted(a, key=itemgetter(0))
        sorted(b, key=itemgetter(0))

        sa = []
        for x, y in a:
            nx = x.split(":")
            ny = y.split(":")

            hx = int(nx[0])*60+int(nx[1])
            hy = int(ny[0])*60+int(ny[1])

            sa.append([hx,hy])

        sb = []
        for x, y in b:
            nx = x.split(":")
            ny = y.split(":")

            hx = int(nx[0])*60+int(nx[1])
            hy = int(ny[0])*60+int(ny[1])

            sb.append([hx,hy])

        sa.sort(reverse=True)
        sb.sort(reverse=True)
        if ii in debug:
            print sa
        if ii in debug:
            print sb
        
        todos = True
        ta, tb = 0,0
        toa, tob = 0,0
        enca = []
        encb = []

        if ii in debug:
            print "O turnarround time é %i e o caso %i" % (tat, ii)
        for i in range(1800):
            if ii in debug:
                print i
                
            if len(sa) == 0 and len(sb) == 0:
                if ii in debug:
                    print "No minuto %i não haviam mais trens na fila!" % i
                break
            
            if len(sa) > 0:
                auxa = sa.pop()

            if len(sb) > 0:
                auxb = sb.pop()

            aencb = encb[::]
            for trem in aencb:
                tchegada = int(trem[1])+int(tat)
                if tchegada == i:
                    if ii in debug:
                        print "O trem chegou em B as %i:%i e agora tem %i trems" % ((trem[1]+tat)/60,(trem[1]+tat)%60, tb+1)
                        print enca
                        print encb
                    encb.remove(trem)
                    tb+=1

            aenca = enca[::]
            for trem in aenca:
                tchegada = int(trem[1])+int(tat)
                if tchegada == i:
                    if ii in debug:
                        print "O trem chegou em A as %i:%i e agora tem %i trems" % ((trem[1]+tat)/60,(trem[1]+tat)%60, ta+1)
                        print enca
                        print encb
                    enca.remove(trem)
                    ta+=1
                    
            if auxa[0]==i:
                encb.append(auxa)
                if ii in debug:
                    print "Trem saindo de A as %i:%i pra chegar as %i:%i sobraram %i trems" % ((auxa[0])/60,(auxa[0])%60, auxa[1]/60, auxa[1]%60, ta-1)
                    print enca
                    print encb
                if ta < 1:
                    if ii in debug:
                        print "Não tinha trem em A para sair as %i" % auxa[0]
                    toa+=1
                else:
                    ta-=1
                while len(sa)>0 and sa[-1][0]==i:
                    auxa = sa.pop()
                    encb.append(auxa)
                    if ta < 1:
                        if ii in debug:
                            print "Não tinha trem em A para sair as %i" % auxa[0]
                        toa+=1
                    else:
                        ta-=1

            if auxb[0]==i:
                enca.append(auxb)
                if ii in debug:
                    print "Trem saindo de B as %i:%i pra chegar as %i:%i sobraram %i trems" % ((auxb[0])/60,(auxb[0])%60, auxb[1]/60, auxb[1]%60, tb-1)
                    print enca
                    print encb
                if tb < 1:
                    if ii in debug:
                        print "Não tinha trem em B para sair as %i" % auxb[0]
                    tob+=1
                else:
                    tb-=1
                while len(sb)>0 and sb[-1][0]==i:
                    auxb = sb.pop()
                    enca.append(auxb)
                    if tb < 1:
                        if ii in debug:
                            print "Não tinha trem em A para sair as %i" % auxb[0]
                        tob+=1
                    else:
                        tb-=1
                
            if auxa not in encb and auxa != (-1,-1):
                sa.append(auxa)
                auxa = (-1,-1)

            if auxb not in enca and auxb != (-1,-1):
                sb.append(auxb)
                auxb = (-1,-1)

            if len(sa) > 0:
                gambiarraa = sa.pop()
            else:
                gambiarraa = (-1,-1)
                
            if len(sb) > 0:
                gambiarrab = sb.pop()
            else:
                gambiarrab = (-1,-1)

            if gambiarraa[0] == i or gambiarrab[0] == i:
                print "Passei aqui\n"*30
                i-=1

            if gambiarraa !=(-1,-1):
                sa.append(gambiarraa)

            if gambiarrab !=(-1,-1):
                sb.append(gambiarrab)

        if ii in debug:
            print "%i %i" % (toa, tob)
            print enca
            print encb
            
        saida.write("Case #%i: %i %i\n" % (ii, toa, tob))
        if ii in debug:
            print "Novo CASO!"

    entrada.close()
    saida.close()
    print "Tchau e obrigado pelos peixes!"

main()
