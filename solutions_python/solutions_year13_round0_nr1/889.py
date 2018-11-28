#!/usr/bin/python
import sys

def main():
    f = open(sys.argv[1], 'rU')
    t = int(f.readline())

    fout = open(sys.argv[1]+'.out', 'w')

    for case in range(1,t+1):
        result = processcase(f)
        fout.write("Case #%(case)d: " %{"case":case})
        fout.write(result)

    fout.close()
    f.close()


def processcase(fin):
    rows = [fin.readline()[:4] for _ in range(4)]   #array of strings
    fin.readline()  #discard blank line
    
    for i in range(4):
        #check rows
        ws = winnersec(rows[i][0],rows[i][1],rows[i][2],rows[i][3])
        if ws:
            return ws+" won\n"

    for i in range(4):
        #check columns
        ws = winnersec(rows[0][i],rows[1][i],rows[2][i],rows[3][i])
        if ws:
            return ws+" won\n"
    #diagonals
    ws = winnersec(rows[0][0],rows[1][1],rows[2][2],rows[3][3])
    if ws:
        return ws+" won\n"
    ws = winnersec(rows[3][0],rows[2][1],rows[1][2],rows[0][3])
    if ws:
        return ws+" won\n"

    #not ended or draw
    if (''.join(rows).count('.') == 0):
        return "Draw\n"
    else:
        return "Game has not completed\n"



def winnersec(a,b,c,d):
    if ('T' in a+b+c+d):
        if ((a+b+c+d).count("X") == 3):
            return "X"
        if ((a+b+c+d).count("O") == 3):
            return "O"
    else:
        if ((a+b+c+d).count("X") == 4):
            return "X"
        if ((a+b+c+d).count("O") == 4):
            return "O"
    return ""   #empty string casts into bool as false



if __name__ == '__main__':
    main()

