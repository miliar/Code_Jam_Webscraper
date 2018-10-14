def go():
    f=open('in.txt')
    for case in  range(int(f.readline())):
        l=f.readline().split()
        lpk=int(l[0])
        keys=int(l[1])
        letters=int(l[2])
        fr=[int(x) for x in f.readline().split()]
        if letters>lpk*keys:
            print 'Case #%d: Impossible'%(case+1)
        else:
            fr.sort()
            fr.reverse()
            r=0
            i=0
            #print fr
            for x in range(1,lpk+1):
                if i==len(fr):
                        break
                for y in range(keys):
                    if i==len(fr):
                        break
                    r+=fr[i]*x
                    i+=1
            print  'Case #%d: %d'%(case+1,r)
            
            
        






    f.close()



go()
