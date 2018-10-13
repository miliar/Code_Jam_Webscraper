f=open("input").readlines()
g=open("output", 'w')
d={'a':'y', 'b':'n', 'c':'f', 'd':'i', 'e':'c', 'f':'w','g':'l','h':'b','i':'k','j':'u','k':'o','l':'m', 'm':'x', 'n':'s', 'o':'e', 'p':'v', 'q':'z', 'r':'p', 's':'d', 't':'r', 'u':'j', 'v':'g', 'w':'t', 'x':'h','y':'a', 'z':'q', ' ': ' '}

data={}

for k in d.keys():
    data[d[k]]=k
t=int(f[0].strip())

cas=1
for s in f[1:]:
    ans=''
    q=s.strip()
    for i in q:
        ans+=data[i]
    g.write("Case #%s: %s\n"%(cas, ans))
    cas+=1   


