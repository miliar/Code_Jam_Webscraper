
def solve(s,k):
    count = 0
    for i in xrange(0, len(s) - (k - 1)):
        if s[i] == '-':
            flip(s,i,k)
            count += 1

    for c in s[-(k - 1):]:
        if c == '-':
            return 'IMPOSSIBLE'

    return count

def flip(s,i,k):
    for j in xrange(i, i + k):
        if s[j] == '+':
            s[j] = '-'
        else:
            s[j] = '+'


input_count = int(raw_input())
for i in xrange(1, input_count + 1):
    input_line = raw_input()
    s, k = input_line.split()
    print r'Case #{}:'.format(i), solve(list(s),int(k))

