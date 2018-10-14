#Google Code Jam 2015 - Qualification Round
#Problem D. Ominous Omino

R = 'RICHARD'
G = 'GABRIEL'
omino = {'2 1 1':R,
         '2 1 2':G,
         '2 1 3':R,
         '2 1 4':G,
         '2 2 1':G,
         '2 2 2':G,
         '2 2 3':G,
         '2 2 4':G,
         '2 3 1':R,
         '2 3 2':G,
         '2 3 3':R,
         '2 3 4':G,
         '2 4 1':G,
         '2 4 2':G,
         '2 4 3':G,
         '2 4 4':G,
         '3 1 1':R,
         '3 1 2':R,
         '3 1 3':R,
         '3 1 4':R,
         '3 2 1':R,
         '3 2 2':R,
         '3 2 3':G,
         '3 2 4':R,
         '3 3 1':R,
         '3 3 2':G,
         '3 3 3':G,
         '3 3 4':G,
         '3 4 1':R,
         '3 4 2':R,
         '3 4 3':G,
         '3 4 4':R,
         '4 3 4':G,
         '4 4 3':G,
         '4 4 4':G,
    }

def ominous_omino():
    fi = open('D-small-attempt2.in','r')
    fo = open('D-small-attempt2.ou','w')
    case = int(fi.readline().strip('\n'))
    for i in range(1,case+1):
        s = fi.readline().strip('\n')
        if s[0]=='1': result = G
        elif s[0]=='4' and s not in ['4 3 4','4 4 3','4 4 4']: result = R
        else: result = omino[s]
        fo.write('Case #'+str(i)+': '+result+'\n')
    fi.close()
    fo.close()

if __name__ == '__main__':
    ominous_omino()
