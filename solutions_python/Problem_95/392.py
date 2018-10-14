dict1={'e':'o','j':'u','p':'r','m':'l','y':'a','s':'n','l':'g','c':'e','k':'i','d':'s','x':'m','v':'p','n':'b','i':'d','r':'t','b':'h','t':'w','k':'i',' ':' ','z':'q','\n':'\n','w':'f','f':'c','v':'p','o':'k','u':'j','l':'g','g':'v','a':'y','h':'x','q':'z'}
f=open('/home/cscape/Desktop/test.txt','r')
num=f.readlines()
f.close()
f1=open('/home/cscape/Desktop/test123456.txt','w')
for i in range(int(num[0])):
    f1.writelines('Case #%s: '%(i+1))
    for char in num[i+1]:
        f1.write(dict1[char])
f1.close()
