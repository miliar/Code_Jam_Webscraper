from sys import stdin as sin

def swap(l, i1, i2):
    s = l[i1]
    l[i1] = l[i2]
    l[i2] = s

for c in range(int(sin.readline())):
    digit = list(str(int(sin.readline())))
    members = list(set(digit))
    members.sort()
    sorted = digit[:]
    sorted.sort()
    sorted.reverse()

    if digit == sorted:
        digit.reverse()
        first = filter(lambda x: x>'0', digit)[0]
        digit.pop(digit.index(first))
        digit = [first, '0'] + digit
    else:
        # Start from the end and find where we have a < relation between n and n-1
        pre = '0'
        digit.reverse()
        for (idx,d) in enumerate(digit):
            if d < pre:
                break
            pre = d
        swap(digit, idx, digit.index(min(filter(lambda x: x>d, digit[:idx]))))
        remainder = digit[:idx]
        remainder.sort()
        remainder.reverse()
        digit = remainder + digit[idx:]
        digit.reverse()

    print "Case #%d: %s" % (c+1, ''.join(digit))
        
