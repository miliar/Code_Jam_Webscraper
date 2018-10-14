
mapping = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}



def getOriginal(translated):
    original = []
    for word in translated.split():
        tword=''
        for c in word:
            tword += mapping[c]
        original.append(tword)
    oword = ' '.join(original)
    return oword.strip()


def main(numTestCases,testCases):
    for i in range(0,numTestCases):
        t = testCases[i]
        o = getOriginal(t)
        print "Case #%d: %s"%(i+1,o)


if __name__ == '__main__':
    import sys
    if(len(sys.argv)==2):
        f = open(sys.argv[1],'r').readlines()
        f = [i.replace('\n','') for i in f]
        numTestCases = int(f[0])
        testCases = f[1:]
        main(numTestCases,testCases)
    else:
        print "Usage: python " + sys.argv[0] +" filename"
