T = int(raw_input())
str1=[]
while(T):
    str1.append(raw_input())
    T-=1

mapp = {' ':' ', 'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u',
'k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

u = []
count=1
for s in str1:
    l = list(s);
    for t in l:
      u.append(mapp[t]);  
    
    print "Case #"+str(count)+": "+"".join(str(n) for n in u)
    u=[]
    count+=1


