f = open('C:\Users\Anh Duong\Desktop\A-large.in','r')
f2 = open('output.txt','w')
T = int(f.readline())
for i in range(T):
    string = f.readline()
    index = string.index(' ')
    sm = int(string[0:index])
    string = string[index+1:-1]
    a = 0
    sum = 0
    for j in range(sm+1):
        while a+sum<j:
            a+=1
        sum+=int(string[j])
    f2.write('Case #'+str(i+1)+': '+str(a)+'\n')

f.close()
f2.close()