
if __name__ == "__main__":
    
    mapping = {'a': 'y',
        'c': 'e',
        'b': 'h',
        'e': 'o',
        'd': 's',
        'g': 'v',
        'f': 'c',
        'i': 'd',
        'h': 'x',
        'k': 'i',
        'j': 'u',
        'm': 'l',
        'l': 'g',
        'o': 'k',
        'n': 'b',
        'q': 'z',
        'p': 'r',
        's': 'n',
        'r': 't',
        'u': 'j',
        't': 'w',
        'w': 'f',
        'v': 'p',
        'y': 'a',
        'x': 'm',
        'z': 'q'
}  
    
    fi = open("input", "r")
    fo = open("output", "w")

    tests = int(fi.readline())
    
    for test in range(tests):

        line = fi.readline()
        words = line.split()       

        ans = ""
        for w in words:
            for i in w:
                if i.isalpha():
                    ans += mapping[i]
                
            ans += " "
        
        ans = ans.strip()
        fo.write("Case #" + str(test + 1) + ": " + ans + "\n")

    fo.close()
    fi.close()