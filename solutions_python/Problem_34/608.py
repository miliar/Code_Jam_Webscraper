import re

if __name__ == "__main__":
    file = open('in.txt','r')
    (L, D, N) = file.readline().split(' ')
    L = int(L)
    D = int(D)
    N = int(N)
    words = []
    for d in range(0,D):
        words.append(file.readline()[0:-1])
    regexps = []
    for n in range(0,N):
        regexps.append(file.readline()[0:-1].replace('(','[').replace(')',']'))
    
    file.close()

    for n in range(0,N):
        regexps[n] = re.compile(regexps[n])
    
    file =open('out.txt','w')
    for n in range(0, N):
        matchings = 0
        for word in words:
            if regexps[n].match(word):
                matchings+=1
        file.write('Case #%i: %i\n' % (n+1, matchings))
    file.close()
        
