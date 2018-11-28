#Program
import time


tSTART = time.time()

def g2text(string):
    output = ''
    g2tmap = {'a':'y', 'b':'h', 'c':'e', 'd':'s', 'e':'o', 'f':'c', 'g':'v',
            'h':'x', 'i':'d', 'j':'u', 'k':'i', 'l':'g', 'm':'l', 'n':'b',
            'o':'k', 'p':'r', 'q':'z', 'r':'t', 's':'n', 't':'w', 'u':'j',
            'v':'p', 'w':'f', 'x':'m', 'y':'a', 'z':'q', ' ':' '}
    for i in string:
        output += g2tmap[i]
    return output
        
    

f = open("A-small-attempt1.in", "r")
text = f.read()
f.close()
lines = text.split('\n')

f = open("output.txt", "w") 

for i in range(1, int(lines[0])+1):
    output = "Case #"+str(i)+": "+g2text(lines[i])+'\n'
    f.write(output)

f.close()

print time.time()-tSTART,"seconds"
