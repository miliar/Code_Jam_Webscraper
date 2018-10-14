lang={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n',
      't':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q',' ':' ','\n':'\n'}

f = open("in.txt","r")
out = open("out.txt","w")
N = int(f.readline())

i=1;
for line in f:
    this_line = 'Case #'+str(i)+': '
    for j in line:
        this_line = this_line+lang[j]
    out.write(this_line)
    i=i+1
