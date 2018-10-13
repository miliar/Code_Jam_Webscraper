import sys

map = { 
# cypher : plain
     'a' : 'y',
     'b' : 'h',
     'c' : 'e',
     'd' : 's',
     'e' : 'o',
     'f' : 'c',
     'g' : 'v',
     'h' : 'x',
     'i' : 'd',
     'j' : 'u',
     'k' : 'i',
     'l' : 'g',
     'm' : 'l',
     'n' : 'b',
     'o' : 'k',
     'p' : 'r',
     'q' : 'z',
     'r' : 't',
     's' : 'n',
     't' : 'w',
     'u' : 'j',
     'v' : 'p',
     'w' : 'f',
     'x' : 'm',
     'y' : 'a',
     'z' : 'q',
     ' ' : ' ',
     '\n': '\n'
}
            
def degoogle(s):
    newstr = ""
    for x in s:
        newstr += map[x]
    #print newstr
    return newstr

if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
        lines = f.readlines()[1:]
        f2 = open('output.out', 'w')
        
        count = 1
        
        for l in lines:
            f2.write("Case #" + str(count) + ": " + degoogle(l))
            count += 1
    else:
        while 1:
            degoogle(raw_input("> "))