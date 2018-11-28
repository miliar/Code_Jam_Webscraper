import sys

tc_len = int(sys.stdin.readline())
for tc in range(tc_len):
    s, k = tuple(sys.stdin.readline().split())
    s = [True if c == '+' else False for c in s]
    k = int(k)
    counter = 0
    for i in range(len(s) - k + 1):
        if s[i] == False:
            counter += 1
            for j in range(i, i + k):
                s[j] = not s[j]
    okay = True
    for i in range(len(s) - k + 1, len(s)):
        if s[i] == False:
            okay = False
            break
    if not okay:
        print('Case #' + str(tc + 1) + ': IMPOSSIBLE')
    else:
        print('Case #' + str(tc + 1) + ': ' + str(counter))
