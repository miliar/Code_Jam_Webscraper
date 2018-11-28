myfile = open('bl.in','r')
myfile2 = open('bl.out','w+')


def gcd(a,b):
    if not b:
        return a
    elif not a:
        return b
    elif a>b:
        return gcd(b,a%b)
    else:
        return gcd(a,b%a)


x=myfile.readline()
t=int(x)
#print(t)

for i in range(t):
    x=myfile.readline()
    
    
    pn= (x.split(' '))
    partr=[]
    
    myx=int (pn[0])
    pn.pop(0)
    for kk in range(myx):
        partr.append(int (pn[kk]))
    partr.sort()

    #print(partr)
    if myx==2:
        myr=int (int (partr[1])-int (partr[0]))
    else:
        parts=[]
        for k in range(myx-1):
            parts.append(int (int(partr[k+1])-int (partr[k])))
            #print(parts[k])

        myp=int (parts[0])
        myq=int (parts[1])      
        myr=int (gcd(myp,myq))
        #print(myr)
        for j in range(myx-3):
            myr=int ( gcd( myr,int (parts[j+2]) ))
            #print(myr)
            
                  
    #print(myr)
    #print( 5-(26%5) )
    #print(partr[0])

    ss=str("Case #"+str(i+1)+": "+ str( ( int(myr)-int ( int(partr[0]%myr) ) )%myr) )
    print(ss)
    myfile2.write(ss)
    myfile2.write('\n')


myfile2.close()
    
        
    


