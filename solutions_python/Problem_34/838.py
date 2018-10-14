import re

contents = open('A-small-attempt8.in').readlines()
print contents
tmp = contents[0][:-1].split(' ')

length = int(tmp[0])
tc  = int(tmp[1])

rslt= []

    

for i in range(tc+1,len(contents)):
    print "Case #:"+str(i-tc),
    count = 0
    lista = []
    lista.append(contents[i])
    print lista
    lista = []
    parten = contents[i][:-1].replace('(','[').replace(')',']')
    '''
    if (i != len(contents)-1):
        parten = contents[i][:-1].replace('(','[').replace(')',']')
        #print parten,lista
    else:
        parten = contents[i].replace('(','[').replace(')',']')
        #print "end",parten
    
    '''
    for m in range(1,tc+1):
        #print parten,contents[m], 
        
        s= re.findall(parten,contents[m][:-1])
        if len(s)==0:
            pass
        else:
            print len(s)
        #print s
        count = count + len(s)
    #print count
    rslta = open('b','a')
    rslta.write("Case #"+str(i-tc)+": "+str(count)+"\n")
    rslta.close()
    
    
