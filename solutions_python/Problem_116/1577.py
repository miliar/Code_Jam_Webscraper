def main():
    """
        docstring for main
    """
    #table = [['X','X','X','T'],[.,.,.,.]]
    exit_values = []
    N = int(raw_input())
    for case in range(1,N+1):
        table = []
        for row in range(0,4):
            r = raw_input()
            r.split()
            row = [str(a) for a in r]
            table.append(row)
        result = check(table)
        #print "Case %d " % case
        #print table
        #print result
        if (4,'X') in result:
            exit_values.append((case,'X'))
        elif (4,'O') in result:
            exit_values.append((case,'O'))
        else:
            not_finished = False
            for row in table:
                if '.' in row:
                    exit_values.append((case,"."))
                    not_finished = True
                    break
            if not_finished == False:
                exit_values.append((case,"D"))
        if case != N:
            raw_input()

    for value in exit_values:
        res = ""
        if value[1] == "O":
            res = "O won"
        elif value[1] == "X":
            res = "X won"
        elif value[1] == ".":
            res = "Game has not completed"
        elif value[1] == "D":
            res = "Draw"
        print "Case #%d: %s" % (value[0], res)

def check(table):
    #if one has won is because there is 4 fich in row or in vertical or in the cross
    result = []
    result.append(conectadas(table,0,0,1,1))
    result.append(conectadas(table,0,3,1,-1))
    for x in range(0,4):
        result.append(conectadas(table,0,x,1,0))
    for y in range(0,4):
        result.append(conectadas(table,y,0,0,1))
    return result


def conectadas(table,f,c,df,dc):
    fich = table[f][c]
    suma = contar(table,f,c,df,dc,fich) + contar(table,f,c,-df,-dc,fich) -1
    return (suma, fich)

def contar(table,f,c,df,dc,fich,ac=0):
    if valida(f,c) and (table[f][c] == fich or table[f][c]=="T"):
        return contar(table,f+df,c+dc,df,dc,fich,ac+1)
    return ac

def valida(f, c):
    return (0 <= f < 4 and 0 <= c < 4)

if __name__ == '__main__':
    main()
