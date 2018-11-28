
def cnt_min(s, q):
    lets = {}
    for ch in s:
        lets[ch] = lets.get(ch, 0) + 1
    res = q.get(s[0], 0) // lets[s[0]]
    for l in lets:
        if q.get(l, 0) // lets[l] < res:
            res = q.get(l, 0) // lets[l]
    # print('Max:', s, q, res)
    return res

def cut(s, cnt, q):
    for ch in s:
        q[ch] = q[ch] - cnt
    return q
        
def ret(s, cnt, q):
    for ch in s:
        q[ch] = q[ch] + cnt
    return q

def tryall(digit, next_digit, digit_str, number, rest):
    for count in range(cnt_min(digit_str, rest) + 1):
        #print('Try: ', digit, count, rest)
        if count > 0:
            number1 = number + digit * count
            rest = cut(digit_str, count, rest)
            result, success = search(next_digit, number1, rest)
            rest = ret(digit_str, count, rest)
        else:
            result, success = search(next_digit, number, rest)
        if success:
            return (result, success)
    return (number, False)

def trymax(digit, next_digit, digit_str, number, rest):
    count = cnt_min(digit_str, rest)
    # print('Try: ', digit, count, rest)
    if count > 0:
        number1 = number + digit * count
        rest = cut(digit_str, count, rest)
        result, success = search(next_digit, number1, rest)
        rest = ret(digit_str, count, rest)
    else:
        result, success = search(next_digit, number, rest)
    if success:
        return (result, success)
    return (number, False)

def search(digit, number, rest):
    s = 0
    for q in rest:
        if rest[q] < 0:
            print('Rest < 0!')
            exit(1)
        s = s + rest[q]
    if s == 0:
        return (number, True)
    if digit == '0':
        res, success = trymax('0', '1', 'ZERO', number, rest)
        if success:
            return (res, success)
    if digit == '1':
        res, success = tryall('1', '2', 'ONE', number, rest)
        if success:
            return (res, success)
    if digit == '2':
        res, success = tryall('2', '3', 'TWO', number, rest)
        if success:
            return (res, success)
    if digit == '3':
        res, success = tryall('3', '4', 'THREE', number, rest)
        if success:
            return (res, success)
    if digit == '4':
        res, success = tryall('4', '5', 'FOUR', number, rest)
        if success:
            return (res, success)
    if digit == '5':
        res, success = tryall('5', '6', 'FIVE', number, rest)
        if success:
            return (res, success)
    if digit == '6':
        res, success = trymax('6', '7', 'SIX', number, rest)
        if success:
            return (res, success)
    if digit == '7':
        res, success = tryall('7', '8', 'SEVEN', number, rest)
        if success:
            return (res, success)
    if digit == '8':
        res, success = trymax('8', '9', 'EIGHT', number, rest)
        if success:
            return (res, success)
    if digit == '9':
        res, success = tryall('9', 'Q', 'NINE', number, rest)
        if success:
            return (res, success)
    return (number, False)     

T = int(input().strip())
for casen in range(1, T + 1):
    x = input().strip()
    lets = {}
    for ch in x:
        lets[ch] = lets.get(ch, 0) + 1
    number, success = search('0', '', lets)
    if success:
        print('Case #%d: %s' % (casen, number, ))
    else:
        print('Case #%d: >>> FAIL!!! <<<' % (casen, ))
