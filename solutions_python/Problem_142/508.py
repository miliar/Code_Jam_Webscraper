def factorize(word):
    counts  = [1]
    letters = word[0]

    for i in xrange(1, len(word)):
        if word[i] == letters[-1]:
            counts[-1] += 1
        else:
            counts.append(1)
            letters += word[i]
    
    return (counts, letters)

def equate(counts):
    #print counts
    middle = float(sum(counts)) / len(counts)
    x = int(round(middle, 0))

    total = 0
    for n in counts:
        total += abs(n - x)

    #print '>>> %d' % total
    return total

def solve(words):
    words = [factorize(word) for word in words]
    for word in words[1:]:
        if word[1] != words[0][1]:
            return "Fegla Won"

    moves = 0
    l = len(words[0][1])
    for i in xrange(0, l):
        counts = [word[0][i] for word in words]
        moves += equate(counts)

    return moves

T = int(raw_input())
for t in xrange(0, T):
    words = []
    N = int(raw_input())
    for i in xrange(0, N):
        words.append(raw_input().strip())
    print 'Case #%d: %s' % (t + 1, solve(words))
