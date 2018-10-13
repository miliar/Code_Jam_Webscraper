code = {}
code['a'] = 'y'
code['b'] = 'n'
code['c'] = 'f'
code['d'] = 'i'
code['e'] = 'c'
code['f'] = 'w'
code['g'] = 'l'
code['h'] = 'b'
code['i'] = 'k'
code['j'] = 'u'
code['k'] = 'o'
code['l'] = 'm'
code['m'] = 'x'
code['n'] = 's'
code['o'] = 'e'
code['p'] = 'v'
code['q'] = 'z'
code['r'] = 'p'
code['s'] = 'd'
code['t'] = 'r'
code['u'] = 'j'
code['v'] = 'g'
code['w'] = 't'
code['x'] = 'h'
code['y'] = 'a'
code['z'] = 'q'

engToGoog = code
googToEng = dict([(v,k) for (k,v) in code.iteritems()])

eng1 = "our language is impossible to understand"
eng2 = "there are twenty six factorial possibilities"
eng3 = "so it is okay if you want to just give up"

goog1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
goog2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
goog3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv"

def transETG(english):
    return translate(english, engToGoog)
    
def transGTE(google):
    return translate(google, googToEng)
    
def translate(string, dictionary):
    newstr = ""
    for char in string:
        newchar = char
        if char in dictionary.keys():
            newchar = dictionary[char]
        newstr += newchar
    return newstr

def main(filein):
    f = open(filein, "r")
    outname = filein.split(".")[0] + "OUT.txt"
    g = open(outname, "w")

    count = -1
    for line in f:
        count += 1
        if count == 0:
            continue
        newline = "Case #" + str(count) + ": " + transGTE(line)
        g.write(newline)
    
    f.close()
    g.close()