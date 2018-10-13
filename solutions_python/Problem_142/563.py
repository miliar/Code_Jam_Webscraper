def convert(str):
    ret = []
    last = ''
    count = 0
    str += '!'
    for i in str:
        if i == last:
            count += 1
        else:
            ret.append((last, count + 1))
            count = 0
            last = i
    ret.pop(0)
    return ret

def homogeneous(ls):
    return len(set(ls)) == 1

def nth(n):
    return lambda x: x[n]

def solve(words):
    if not homogeneous(map(len, words)):
        return -1
    ans = 0
    for i in range(0, len(words[0])):
        ls = map(nth(i), words)
        chars = map(lambda (x, y): x, ls)
        counts = map(lambda (x, y): y, ls)
        if not homogeneous(chars):
            return -1
        avg = int(round(sum(counts, 0.0) / len(counts)))
        ans += reduce(lambda x, y: x + abs(y - avg), counts, 0)
    return ans



N = input()
for i in range(1, N + 1):
    n = input()
    words = []
    for j in range(0, n):
        words.append(convert(raw_input()))
    ans = solve(words)
    print 'Case #{0}: {1}'.format(i, ans if ans >= 0 else "Fegla Won")
