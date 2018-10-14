def convert(n,x):
    flag = 0
    if n.find('10') != -1:
        n1 = '9'
        for i in range(2,len(n)):
            n1 = n1 + '9'
    else:
        if n[0] == str(x):
            n1 = str(x-1)
            flag =1
            #print len(n1)
        else:
            n1 = n[0]
        for i in range(1,len(n)-1):
            if n[i] == str(x):
                if flag != 1:
                    n1 += str(x-1)
                    flag = 1
                else:
                    n1 += '9'
                #print len(n1)
                #print str (x-1)
            else:
                n1 += n[i]
        n1+= '9'
        
    return n1
def tidyMax(n):
    if len(n) > 1:
        for i in range(len(n)-1):
            if int(n[i]) > int(n[i+1]):
                n2 = convert(n[0:i+2],int (n[i]))
                #print n[0:i+2], n[i]
                if len(n)- i-1 > 0:
                    for i in range (1, len(n)-i-1):
                        n2+='9'
                return n2
        return n
    else:
        return n[0]
            
f=open('input.txt','r')
f1=open('output.txt','w+')
n = f.readline()
for i in range(int(n)):
    f1.write("Case #%d: " %(int(i)+1))
    t=f.readline()
    output = tidyMax(t[0:len(t)-1])
    f1.write("%s\n" %output)
f.close
f1.close


	
