# coding=latin-1 

if __name__ == '__main__':
    
    #trans è un dictionary googlese:eng
    trans = {'y': 'a',  'n': 'b',  'f': 'c',  'i': 'd',  'c': 'e',  'w': 'f',  'l': 'g',  'b': 'h',  'k': 'i',  'u': 'j',  'o': 'k',  'm': 'l',  'x': 'm',  's': 'n',  'e': 'o',  'v': 'p',  'z': 'q',  'p': 'r',  'd': 's',  'r': 't',  'j': 'u',  'g': 'v',  't': 'w',  'h': 'x',  'a': 'y',  'q': 'z'}
    fileinput = open("./input.in", "r")
    n = int(fileinput.readline())
    
    for k in range(1, n+1):
        myline = fileinput.readline()
        for j in range(len(myline)):
            try:
                myline = myline[:j]+trans[myline[j]]+myline[j+1:]
            except KeyError:
                pass
        print "Case #" + str(k) + ":", myline,
        
