d = {'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v','h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b','o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j','v':'p','w':'f','x':'m','y':'a','z':'q'}

def parseLine(stg):
    line = []
    for s in stg:
        if s == ' ':
            line.append(" ")
        else:
            stg1 = list(s)
            for a in stg1:
                line.append(a.replace(a,d[a]))
    return ''.join(line)
    

def __main__():
    fp = open("input.txt","r")
    fpo = open("output.txt","w+")
    lines = fp.readlines()
    #print lines
    i = 0
    for line in range(1,len(lines)):
        l = lines[line].strip("\n")
        stg = parseLine(l)
        print stg
        out_line = "Case #"+str(line)+": " + stg + "\n"
        fpo.write(out_line)
        
__main__()
