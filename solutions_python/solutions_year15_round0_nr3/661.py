import itertools

def product(x, y):
    if x[0] == '1':
        if y == '1':
            return ['1', x[1]]
        elif y == 'i':
            return ['i', x[1]]
        elif y == 'j':
            return ['j', x[1]]
        elif y == 'k':
            return ['k', x[1]]
    elif x[0] == 'i':
        if y == '1':
            return ['i', x[1]]
        elif y == 'i':
            return ['1', x[1] + 1]
        elif y == 'j':
            return ['k', x[1]]
        elif y == 'k':
            return ['j', x[1] + 1]
    elif x[0] == 'j':
        if y == '1':
            return ['j', x[1]]
        elif y == 'i':
            return ['k', x[1] + 1]
        elif y == 'j':
            return ['1', x[1] + 1]
        elif y == 'k':
            return ['i', x[1]]
    elif x[0] == 'k':
        if y == '1':
            return ['k', x[1]]
        elif y == 'i':
            return ['j', x[1]]
        elif y == 'j':
            return ['i', x[1] + 1]
        elif y == 'k':
            return ['1', x[1] + 1]

t = input()
for n in range(t):
    l, x = map(int, raw_input().split())
    s = raw_input()
    s = s * x
    # print s
    # for i, j in itertools.combinations(range(l * x - 1), 2):        
    #     left = s[:i+1]
    #     middle = s[i+1:j+1]
    #     right = s[j+1:]
    #     #print left, middle, right
    #     flg = True
    #     left_ops = ['1', 0]
    #     for c in left:
    #         left_ops = product(left_ops, c)
    #     # print left_ops
    #     # print flg
    #     if not (left_ops[0] == 'i' and left_ops[1] % 2 == 0):
    #         flg = False
    #     middle_ops = ['1', 0]
    #     for c in middle:
    #         middle_ops = product(middle_ops, c)
    #     if not (middle_ops[0] == 'j' and middle_ops[1] % 2 == 0):
    #         flg = False
    #     # print middle_ops
    #     # print flg
    #     right_ops = ['1', 0]
    #     for c in right:
    #         right_ops = product(right_ops, c)
    #     if not (right_ops[0] == 'k' and right_ops[1] % 2 == 0):
    #         flg = False
    #     # print right_ops
    #     # print flg
    #     if flg == True:
    #         print 'Case #{0}: {1}'.format(n + 1, 'YES')
    #         break
    # else:
    #     print 'Case #{0}: {1}'.format(n + 1, 'NO')

    state = 0
    res = ['1', 0]
    for i in range(l * x):
        res = product(res, s[i])
        if state == 0:
            if res[0] == 'i' and res[1] % 2 == 0:
                state = 1
                res = ['1', 0]
        elif state == 1:
            if res[0] == 'j' and res[1] % 2 == 0:
                state = 2
                res = ['1', 0]
        elif state == 2:
            if res[0] == 'k' and res[1] % 2 == 0:
                state = 3
                res = ['1', 0]
        #print res, state
    if state == 3 and res[0] == '1' and res[1] % 2 == 0:
        print 'Case #{0}: {1}'.format(n + 1, 'YES')
    else:
        print 'Case #{0}: {1}'.format(n + 1, 'NO')


