gte = {'e' : 'o',
       'j' : 'u',
       'p' : 'r',
       'm' : 'l',
       'y' : 'a',
       's' : 'n',
       'l' : 'g',
       'c' : 'e',
       'k' : 'i',
       'd' : 's',
       'x' : 'm',
       'v' : 'p',
       'n' : 'b',
       'r' : 't',
       'i' : 'd',
       'b' : 'h',
       'a' : 'y',
       'f' : 'c',
       'g' : 'v',
       'h' : 'x',
       'o' : 'k',
       'q' : 'z',
       't' : 'w',
       'u' : 'j',
       'w' : 'f',
       'z' : 'q'}

def run(fileName):
    f = open(fileName)
    noOfCases = int(f.readline())
    for i in range(noOfCases):
        print "Case #"+str(i+1)+": "+translate(f.readline())



def translate(text):
    result = ''
    for char in text:
        if char == '\n':
            break
        result = result + ' ' if char == ' ' else result + gte[char]
    return result
