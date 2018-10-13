vowels = "aeiou"

def solve(name, n):
    counts = hasCons(name, n)
    i = n
    result = sum(counts)
    while i < len(name):
        newCounts = [0]*(len(counts)-1)
        for j in range(len(newCounts)):
            newCounts[j] = 1 if counts[j] + counts[j+1] > 0 else 0
        counts = newCounts
        result += sum(counts)
        i += 1
    return result


def hasCons(name, n):
    return [1 if sum(name[i:i+n].count(c) for c in vowels) == 0 else 0 for i in range(len(name)-n+1)]



inp = raw_input()
T = int(inp)
for t in range(1,T+1):
    inp = raw_input()
    name, n_str = inp.split(' ')
    n = int(n_str)
    answer = solve(name, n)
    print "Case #" + str(t) + ": " + str(answer)
