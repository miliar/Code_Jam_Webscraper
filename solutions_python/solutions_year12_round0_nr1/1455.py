from string import maketrans
import collections
from itertools import permutations

aaa = 'yeq'
bbb = 'aoz'
bfreq = 'etinshrdlcumwfgypbvkjxq' # abcdfghijklmnoprstuvwxz

# ngrams?
#wl = ['a', 'the', 'is', 'are', 'to', 'if', 'so', 'there', 'you', 'our', 'just', 'up', 'and', 'also']
f = open('words.txt', 'r')
wl = [l.replace('\n', '') for l in f.readlines()]
f.close()

def main(lines):
    global aaa, bbb, freq, bfreq
    text = ' '.join(lines)
    
    d = collections.defaultdict(int)
    for c in text: # letter frequency
        d[c] += 1
    ds = sorted(d.items(), key=lambda t: t[1]) # sort by value
    ds.reverse()
    afreq = ''.join([a for a,b in ds if a!=' ' and a not in aaa])
    bfreq = bfreq[:len(afreq)]
    # print afreq
    # print bfreq
    
    step = 6
    for r in xrange(1):
        # step = r+2
        aa = aaa
        bb = bbb
        for i in xrange(step, len(afreq)+step, step):
            end = min(i, len(afreq))
            agram = afreq[i-step:end]
            bgram = bfreq[i-step:end]
            cmax = 0
            maxgram = bgram
            for p in permutations(bgram):
                pgram = ''.join(p)
                trans = text.translate(maketrans(aa+agram, bb+pgram))
                words = trans.split()
                c = 0
                for word in words:
                    if word in wl: c+=1
                if c <= cmax:
                    continue
                else:
                    cmax = c
                    maxgram = pgram
                    # print trans
            aa += agram
            bb += maxgram
        # print text.translate(maketrans(aa, bb))
        # print bfreq
        bfreq = bb[3:]
    aaa = aa
    bbb = bb
    # print aaa
    # print bbb

if __name__ == '__main__':
    import sys
    N = int(sys.stdin.readline())
    lines = []
    for i in xrange(N):
        lines.append(sys.stdin.readline().strip())
    main(lines)
    map = maketrans(aaa, bbb)
    for i in xrange(N):
        print "Case #%d: %s" % (i + 1, lines[i].translate(map))	
