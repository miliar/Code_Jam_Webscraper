def go():
    infile=open('in.txt')
    t=int(infile.readline())
    for case in range(t):
        n,m=[int(x) for x in infile.readline().split()]



        print 'Case #%d: %s'%(case+1,docase(n,m,infile))




    infile.close()

    
def docase(n,m,infile):
    exist=[]

    ret=0
    for x in range(n):
        thisdir=infile.readline().replace('\n','').split('/')[1:]
        for y in range(len(thisdir)):
            exist.append(thisdir[:y+1])
    for y in range(m):
        thisdir=infile.readline().replace('\n','').split('/')[1:]
        for y in range(len(thisdir)):
            if thisdir[:y+1] not in exist:
                exist.append(thisdir[:y+1])
                ret+=1
                #print thisdir[:y+1]
    return ret
    
                

    
        
        
