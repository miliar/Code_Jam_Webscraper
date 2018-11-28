f=open("a.txt","r")
g=open("ans.txt","w")
count=0
d={'y':'a','n':'b','f':'c','i':'d','c':'e','w':'f','l':'g','b':'h','k':'i','u':'j','o':'k','m':'l','x':'m','s':'n','e':'o','v':'p','z':'q','p':'r','d':'s','r':'t','j':'u','g':'v','t':'w','h':'x','a':'y','q':'z'}
for line in f:
    if count==0:
        count=count+1
        continue
    s=""
    for let in line:
        if let==" " or let=="\n":
            s=s+let
        else:
            s=s+d[let]
    st="Case #"+str(count)+": "+s
    g.write(st)
    count=count+1
f.close()
g.close()
