import sys

def TicTac(fname):
    texto=['Game has not completed','X won','O won','Draw','Draw','X won','O won','Draw']
    with open(fname) as file:
        line = file.readline()
        T=int(line)
        for case in range(1,T+1):
            mapa=[]
            result=0
            for r in range(0,4):
                mapa.append(file.readline())
                if ('.' not in mapa[r]) and ('O' not in mapa[r]):
                    result|=1
                if ('.' not in mapa[r]) and ('X' not in mapa[r]):
                    result|=2
            file.readline()
            R=3
            I=3
            draw=4
            for c in range(0,4):
                #diagonals
                if mapa[c][c]=='.':
                    R=0
                if mapa[c][c]=='X':
                    R&=1
                if mapa[c][c]=='O':
                    R&=2
                if mapa[c][3-c]=='.':
                    I=0
                if mapa[c][3-c]=='X':
                    I&=1
                if mapa[c][3-c]=='O':
                    I&=2
                #column
                C=3
                for r in range(0,4):
                    if mapa[r][c]=='.':
                        C=0
                        draw=0
                    if mapa[r][c]=='X':
                        C&=1
                    if mapa[r][c]=='O':
                        C&=2
                result|=C
            result|=R
            result|=I
            result+=draw
            print("Case #{0}: {1}".format(case,texto[result]))
    file.close()
