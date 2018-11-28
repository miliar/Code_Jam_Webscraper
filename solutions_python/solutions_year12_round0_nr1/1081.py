import os

dic = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' ' }

fi = open('C:\\Users\\VINSY\\Desktop\\1.in','r')
f2 = open('C:\\Users\\VINSY\\Desktop\\1.out','w')

a = int(fi.readline())

for i in range(1,a+1):
    s = ''
    for lin in fi.readline():
        if lin == '\n':
            break
        s = s+dic[lin]
    b = "Case #"+str(i)+": "
    f2.write(b)
    f2.write(s)
    if i < a:
        f2.write('\n')

fi.close()
f2.close()

