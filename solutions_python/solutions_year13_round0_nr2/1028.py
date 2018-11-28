def main():
    fileName = 'B-large.in'
    fl = open(fileName)
    wfName = 'res' + fileName
    wf = open(wfName, 'w')
    f = fl.readline()
    f = int(f)
    res = []
    for i in range(f) :
        size = fl.readline()
        size = size.split()
        size = map(int, size)
        rect = []
        for j in range(size[0]) :
            row = fl.readline()
            row = row.split()
            row = map(int,row)
            rect.append(row)
        poss = True    
        for line in rect :  
            m = max(line)
            i = 0
            while(i < len(line)) :
                if line[i] < m :  #we can;t move mover on this size in  row
                    j = 0
                    while( j < size[0]) :
                        if rect[j][i] > line[i] : # we cant move the mower in column also
                            poss = False
                            break
                        j = j + 1
                    if not poss :
                        break # break from outer loop also
                i = i + 1
        if not poss :
            res.append('NO')
        else :
            res.append('YES')
    i = 0
    for line in res :
        i = i + 1
        wf.write('Case #' + str(i) + ': ' + line + '\n')
if __name__ == "__main__" :
    
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    