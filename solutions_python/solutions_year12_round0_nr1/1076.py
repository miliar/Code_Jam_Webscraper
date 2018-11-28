d ={'e':'o','j':'u','p':'r',' ':' ','m':'l','y':'a','s':'n','l':'g','c':'e','k':'i','d':'s','x':'m',
    'v':'p','e':'o','n':'b','r':'t','i':'d','r':'t','b':'h','t':'w','a':'y','h':'x','w':'f','f':'c','o':'k','a':'y','u':'j','g':'v','q':'z','z':'q'}
f=open("inp.in","r")
wf=open("out.txt","w+")
for i in range(int(f.readline())):
    c=f.readline()
    o=""
    for x in c:
        if x !='\n':
            o+=d[x]
    wf.write("Case #"+str(i+1)+": "+o+"\n")
f.close()
wf.close()
