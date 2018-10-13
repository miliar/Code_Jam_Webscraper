
def solve(n):

    i = 0
    while i < len(n) - 1:
        if int(n[i]) > int(n[i + 1]):
            n[i] = str(int(n[i]) - 1)
            for j in xrange(i+1,len(n)):
                n[j] = '9'
            i = 0
            continue
        i += 1

    return int("".join(n))

input_count = int(raw_input())
for i in xrange(1, input_count + 1):
    input_line = raw_input()
    n = input_line
    print r'Case #{}:'.format(i), solve(list(n))

