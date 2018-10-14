def is_tidy(num):
    num = str(num)

    prev = '0'
    for n in num:
        if n >= prev:
            prev = n
        else:
            return False

    return True

def down(num):
    num = str(num)

    for i in reversed(range(len(num))):
        if num[i] != '9':
            num = num[:i] + '9' + num[i+1:]
            i -= 1
            while i >= 0 and num[i] == '0':
                num = num[:i] + '9' + num[i+1:]
                i -= 1
            
            i += 1
            if i == 0:
                num = num[1:]
            else:
                num = num[:i-1] + str((int(num[i-1]) - 1)) + num[i:]

            return int(num)

lines = int(input())

for i in range(lines):
    n = int(input())

    while not is_tidy(n):
#        n -= 1
        n = int(down(n))

    print("Case #%d: %d" % (i+1, n))
