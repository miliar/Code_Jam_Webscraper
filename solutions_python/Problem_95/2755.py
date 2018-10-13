from sys import stdin,stdout
from sys import argv
fi=open(argv[1],"r")
fo=open(argv[2],"w")
T=int(fi.readline())

A={' ':' ','a':'y','b':'h',
   'c':'e','d':'s','e':'o',
   'f':'c','g':'v','h':'x',
   'i':'d','j':'u','k':'i',
   'l':'g','m':'l','n':'b',
   'o':'k','p':'r','q':'z',
   'r':'t','s':'n','t':'w',
   'u':'j','v':'p','w':'f',
   'x':'m','y':'a','z':'q'}

for i in range(1,T+1):
    Gt=""
    G=fi.readline()
    
    for h in G:
        if h!='\n':
        
            Gt+=A[h]
    fo.writelines(("Case #%d: %s\n"%(i,Gt)))


