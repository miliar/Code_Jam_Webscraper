

def tidy(number):
    max = 0
    i = (int)(number)
    while(i>0):
#        print(i)
        if(badCase(i)):
#            print("i badcase")
            s = len((str)(i))
            num = (str)(i)[0]
            i = (int)(num) * 10 ** (s-1)
#            print(i)
            
        if(checknum(i)):
            return i
        i -= 1
        
def badCase(kalle):
#    print(kalle)
    a = (str)(kalle)
    num = a[0]
    k = 0
    t = True
    while(k < len(a) - 1):
#        print(a[k])
        if(a[k] != num):
            t = False
        k += 1
    if((int)(a[len(a)-1]) != 0):
#        print("i if")
        t = False
 #   print(t)
    return t
    

def checknum(number):
    min = 0
    b = (str)(number)
    for char in b:
#        print(char)
#        print(min)
        if((int)(char) < min):
#           print("returning false")
           return False
        min = (int)(char)
 #   print("returning true")
    return True

a = []
k = 0
with open("B-small-attempt2.in") as fin:
    for line in fin:
#        print(k)
        a.append(line)
        k += 1
#print(a)
f = open('out.txt','w')
cases = a[0]
for i in range(1,(int)(cases) + 1):
    f.write("Case #" + (str)(i) + ":")
    num = tidy(a[i])
    print(num)
    f.write(" " + (str)(num) + "\n")
f.close()