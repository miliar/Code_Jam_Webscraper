def f(string):
    alpha = {'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4',
             'h':'44','i':'444','j':'5','k':'55','l':'555','m':'6','n':'66',
             'o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88',
             'v':'888','w':'9','x':'999','y':'999','z':'9999',' ':'0','\n':'',
             }
    res = ''

    for i in xrange(len(string)):
        res += alpha[string[i]]

        try:
            if alpha[string[i]][0] in alpha[string[i+1]]:
                res += ' '
        except:
            continue
        
    return res
            

infile = open('C:\Users\SOUFIANE\Downloads\C-small-practice.in','r')
outfile = open('out.data','w')

n = int(infile.readline().strip())

for i in xrange(1,n+1):
    
    message = infile.readline()
    res = 'Case #%i: %s\n' % (i,f(message))
    outfile.write(res)
    
infile.close()
outfile.close()
