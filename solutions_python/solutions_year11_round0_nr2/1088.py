def go():
    f=open('1.txt')
    cases=int(f.readline())
    for c in range(1,1+cases):
        line=f.readline().split()
        combo={}
        wipe=[]
        if line[0]!='0':
            del line[0]
            for x in range(len(line[0])/3):
                combo[line[0][x*3:x*3+2]]=line[0][x*3+2]
                combo[line[0][x*3+1]+line[0][x*3]]=line[0][x*3+2]
        del line[0]

        if line[0]!='0':
            del line[0]
            for x in range(len(line[0])/2):
                wipe.append((line[0][x*2:x*3+2]))
        del line[0]

        s=''
        
        for x in line[1]:
            s+=x
            for y in combo.keys():
                if s[-2:]==y:
                    s=s[:-2]+combo[y]

            for y in wipe:
                if all(w in s for w in y):
                    s=''
        print 'Case #%d: %s'%(c,str(list(s)).replace("'",''))
    f.close()
        
        
        
