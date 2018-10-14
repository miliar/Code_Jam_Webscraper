
"""
Based on the examples and the hint from the problem
description the following mapping can be constructed
"""
gToE = {
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
     }


if __name__ == '__main__':
    f = open("input.txt")
    out = open("output.txt", "w")
    nr = int(f.readline())
    
    for i in range(0, nr):
        problem = f.readline().strip()
        sollution = ""
        for char in problem:
            sollution += gToE[char]
        s = "Case #" + str(i + 1) + ": " + sollution
        print s
        out.write(s + "\n")
    out.close()
    f.close()