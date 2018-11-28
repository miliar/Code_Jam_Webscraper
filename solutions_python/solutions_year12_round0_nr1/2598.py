def writeFile():
    f = open('/home/maderix/Documents/codejam/lines.txt','r')
    w = open('/home/maderix/Documents/codejam/output.txt','w')
    count=0
    for line in f:
        if line == '3':
            continue
        newline=''
        for i in range(len(line)):
            newchar = getReplaceChar(line[i])
            if newchar != '!':
                newline += newchar
        if count > 0:
            w.write('Case #'+str(count)+': ' + newline + '\n')
        count += 1
    f.close()
    w.close()