from collections import Counter

def countSubseq(haystack, needle):
    s, c = -1, 0
    while s < len(haystack):
        s = haystack.find(needle, s + 1)
        if s >= 0:
            c += 1
        else:
            break
    return c

if __name__ == '__main__':
    with open('monkeys.in') as infile:
        with open('monkeys.out', 'w') as outfile:
            numTestCases = int(infile.readline().strip())
            
            for sample in range(numTestCases):
                K, L, S = tuple(int(x) for x in infile.readline().strip().split())
                counts = Counter(infile.readline().strip())
                target = infile.readline().strip()
                
                letters = list(counts.keys())
                maxCount, mean = 0, 0.0
                w = letters[0] * S
                while True:
                    num = countSubseq(w, target)
                    if num > maxCount:
                        maxCount = num
                    wordProb = 1.0
                    for l in w:
                        wordProb *= counts[l] / K
                    mean += num * wordProb
                    
                    i = S - 1
                    while i >= 0:
                        if w[i] == letters[-1]:
                            w = w[:i] + letters[0] + w[i+1:]
                            i -= 1
                        else:
                            w = w[:i] + letters[letters.index(w[i]) + 1] + w[i+1:]
                            break
                    if i < 0:
                        break
                
                outfile.write('Case #{}: {}\n'.format(sample + 1, maxCount - mean))