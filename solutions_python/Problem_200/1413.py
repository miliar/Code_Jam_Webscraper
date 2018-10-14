# linear scan. memorize max so far
# if current number > max so far, minus 1 the previous digit. set rest digits to 9


x = '111111111111111110'
x = list(x)

def list_to_int(l):
    r = 0
    for i in range(len(l)):
        r += int(l[i]) * (10**(len(l)-i-1))
    return r

with open('B-large.in') as f:
    f.readline()
    casecount = 1
    for l in f:
        casestr = 'Case #{}:'.format(casecount)
        x = list(l.strip())
        last_result = -1
        while True:
            maxsofar = int(x[0])
            for i in range(len(x))[1:]:
                curdigit = int(x[i])
                if curdigit < maxsofar:
                    x[i-1] = int(x[i-1]) - 1
                    x[i:] = ['9'] * (len(x) - i)
                    break
                else:
                    maxsofar = curdigit

            result = list_to_int(x)
            if last_result == result:
                print '{} {}'.format(casestr, result)
                break
            last_result = result
        casecount += 1