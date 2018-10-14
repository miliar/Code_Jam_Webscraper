dictionary={'\n':'\n',' ':' ','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','0':'0','a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}
def g(c):
    return(dictionary[c])
def f(l):
    y=''
    for i in range(0,len(l)):
        y=y+g(l[i])
    return(y)
k=open('A-small-attempt1.txt','r')
v=k.readlines()
t=''
for i in range(1,len(v)):
    t=t+'Case #'+str(i)+': '+f(v[i])
h=open('output.txt','w')
h.write(t)
k.close()
h.close()
