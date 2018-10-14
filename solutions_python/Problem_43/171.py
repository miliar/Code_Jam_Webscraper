T = int(raw_input().strip())

def minSec(s):
    uniqueLetters = set([])
    #How many unique letters in s?
    for letter in s:
        uniqueLetters.add(letter)
    
    letterbindings = {}

    retval = 0
    base = max(len(uniqueLetters), 2)

    letterbindings[s[0]] = 1
    retval += letterbindings[s[0]] * (base ** (len(s) - (1)))
    zeroFree = True

    s = s[1:]
    for place, letter in enumerate(s):
        if letter not in letterbindings:
            if zeroFree:
                letterbindings[letter]=0
                zeroFree = False
            else:
                letterbindings[letter] = len(letterbindings)
        retval += letterbindings[letter] * (base ** (len(s) - (place + 1)))
#        print letterbindings[letter] * (base ** (len(s) - (place + 1))), letterbindings[letter], base, base ** (len(s) - (place + 1)), retval
#   print letterbindings
    return retval

for i in range(T):
    print 'Case #%s: %s' % (i + 1, minSec(raw_input().strip().rstrip()))
