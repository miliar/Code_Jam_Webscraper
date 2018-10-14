def nearest_series(n):
    digits = str(n)
    if digits[-1] == '0':
        return '9' * (len(digits) - 1)
    out = []
    limit = '9'
    for d in digits[::-1]:
        digit = min(d, limit)
        out.append(digit)
        limit = digit
    out = out[::-1]
    for i in xrange(len(out)):
        if out[i] < digits[i]:
            for j in xrange(i+1, len(out)):
                out[j] = '9'
            break
    return ''.join(out)

def test(n, out):
    if int(out) > n:
        raise Exception('{} > {}'.format(out, n))
    prev = '0'
    for d in out:
        if d < prev:
            raise Exception(out)
        prev = d

def f(n):
    digits = list(str(n))
    found_break = False
    for i in xrange(1, len(digits)):
        if digits[i] < digits[i-1]:
            found_break = True
            break
    if not found_break:
        return n
    right = ''.join(['9'] * (len(digits) - i))
    left = nearest_series(int(''.join(digits[0:i])) - 1)
    out = left + right
    out = out.lstrip('0')
    test(n, out)
    return out

T = int(raw_input())
for i in xrange(T):
    N = int(raw_input())
    print('Case #{}: {}'.format(i + 1, f(N)))
