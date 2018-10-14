

def get_problems():
    f = file("A-small-attempt0.in")
    f2 = open("A-small-attempt0.out", 'w')
    numCases = f.readline()
    for i in xrange(1, int(numCases)+1):
        line = f.readline()
        output = translate(line)
        stra = "Case #%d: %s" % (i, output)        
        f2.write(stra)
    f2.close()
        



def translate(line):

    out = ""
    for letter in line:
        if letter in dictionary:
            out += dictionary[letter]
        else:
            out+= letter
    return out

dictionary ={"y":"a","n":"b","f":"c","i":"d","c":"e","w":"f","l":"g","b":"h","k":"i","u":"j","o":"k","m":"l","x":"m","s":"n","e":"o","v":"p","z":"q","p":"r","d":"s","r":"t","j":"u","g":"v","t":"w","h":"x","a":"y","q":"z"}


get_problems()


