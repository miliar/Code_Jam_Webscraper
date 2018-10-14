fin = open("A-small-attempt0.in", "r")
fout = open("test.out", "w")

lang = {'a':'y','b':'h','c':'e','d':'s','e':'o',  
        'f':'c','g':'v','h':'x', 'i':'d','j':'u',   
        'k':'i','l':'g','m':'l', 'n':'b','o':'k',    
        'p':'r','q':'z','r':'t','s':'n','t':'w',      
        'u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

N = int(fin.readline())
for n in range(1,N+1):
    fout.write("Case #%i: " %(n))
    string = fin.readline()
    for c in string:
        if c == ' ':
            fout.write(c)
        if c in lang:
            fout.write(lang[c])
    fout.write("\n")                        
fout.close()
