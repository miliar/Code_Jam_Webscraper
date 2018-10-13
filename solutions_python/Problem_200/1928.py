def solve(num):
    if len(num) == 1:
        return num
    num_len = len(num)
    i = num_len-1
    tokens = [int(x) for x in num]
    last_post = num_len
    while i >= 1:
        if tokens[i] == -1:
            tokens[i] = 9
            max_num = 9
        if tokens[i-1] > tokens[i]:
            tokens[i-1] = tokens[i-1]-1
            j = i
            while j < last_post:
                tokens[j] = 9
                j += 1
            last_post = i
        i -= 1
    if tokens[0] == 0:
        tokens = tokens[1:]
    result = [str(x) for x in tokens]
    return ''.join(result)

for i in range(int(raw_input())):
    num = raw_input()
    result = solve(num)
    print 'Case #%d: %s' % (i+1, result)