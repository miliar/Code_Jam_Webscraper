def main():
    inputfile = open('A-large .in', 'r')
    outputfile = open('output', 'w')
    currentcase = 1
    totalcase = int(inputfile.readline().strip())
    while currentcase <= totalcase:
        (R, C) = inputfile.readline().strip().split()
        R = int(R)
        C = int(C)
        l = []
        for r in range(0,R):
            l.append(inputfile.readline().strip())
            l[r] = [x for x in l[r]]
        i = 0
        possible = True
        while i < R and possible:
            j = 0
            while j < C and possible:
                if l[i][j] == '#':
                    if (i < R - 1) and (j < C - 1) and l[i+1][j] == '#' and l[i][j+1] == '#' and l[i+1][j+1] == '#':
                        l[i][j] = '/'
                        l[i+1][j+1] = '/'
                        l[i+1][j] = '\\'
                        l[i][j+1] = '\\'
                        j +=2
                    else:
                        possible = False
                else:
                    j += 1
            i += 1   
        output = ''
        if possible:
            for x in l:
                for y in x:
                    output += y
                output += '\n'
        else:
            output = 'Impossible\n'
        output = "Case #%d:\n%s"%(currentcase, output)
        outputfile.write(output)
        currentcase += 1
    inputfile.close()
    outputfile.close()
    
    
if __name__ == "__main__":
    main()