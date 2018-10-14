f = open("A-large.txt", "w")

def flip(S):
    flipped = ''
    for c in S:
        if c == '+':
            flipped += '-'
        else:
            flipped += '+'
    return flipped

for x, line in enumerate(open("A-large.in", "r")):
    if x == 0:
        continue
    S, K = line.split()
    K = int(K)
    y = 0
    if '-' in S:
        while True:
            print x
            # Basically I get rid of the happy pancakes from the beginning and the end since any flip with them would be useless
            lP = S.find('-')
            if lP != -1:
                S = S[lP:] # Get rid of the happy faces from the beginning of the string.
            rP = S.rfind('-')
            if rP != -1:
                S = S[:rP+1] # Get rid of the happy faces from the end       of the string.
            print S
            if len(S) == K and '+' in S or len(S) < K:
                y = 'IMPOSSIBLE'
                break
            #If we got this far we must make a flip
            S = flip(S[:K]) + S[K:]
            y += 1
            if len(S) <= K:
                break
    print >>f, "Case #" + str(x) + ": " + str(y)
f.close()
