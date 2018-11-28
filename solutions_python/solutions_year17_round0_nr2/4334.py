


# doesnt catch correct tidy from inputs like 188886
'''def tidy(n):
    str_val = str(n)
    if len(str_val) == 1:
        return n
    else:
        res = str_val[0]
        for k in range(1, len(str_val)):
            if int(str_val[k]) >= int(res[k - 1]):
                res += str_val[k]
            else:
                val = int(str_val[k - 1]) - 1
                if val > 0: #and str_val[k - 2] != str_val[k - 1]:
                    fucking_immutable_strings_in_python = list(res)
                    fucking_immutable_strings_in_python[k - 1] = str(val)
                    res = ''.join(fucking_immutable_strings_in_python)
                    for p in range(k, len(str_val)):
                        res += str(9)
                    return res
                else:
                    #print('yo')
                    res = ''
                    for p in range(0, len(str_val) - 1):
                        res += str(9)
                    return res
        return res'''

def do_nines(start, finish, res):
    for i in range(start, finish):
        res += str(9)
    return res

# correction
def tidy2(n):
    num = str(n)
    if len(num) == 1:
        return n
    res = num[0]
    c = 0 # the awesome same-digit counter
    for k in range(1, len(num)):
        if int(num[k]) >= int(num[k - 1]):
            if num[k-1] == num[k]:
                c += 1
            else:
                c = 0
            res += num[k]
        else:
            val = int(num[k - 1]) - 1
            if val > 0:
                fucking_immutable_strings_in_python = list(res[:k - c])
                fucking_immutable_strings_in_python[k - c - 1] = str(val)
                res = ''.join(fucking_immutable_strings_in_python)
                #print('len(num): {}; k: {}; c: {}; digits: {}'.format(len(num), k, c, res))
                return do_nines(k - c, len(num), res)
            else:
                res = ''
                return do_nines(0, len(num) - 1, res)
    return res






filein = open('B-large.in', 'r')
#filein = open('testBin', 'r')

lines = list()
t = int(filein.readline())
for i in range(1, t + 1):
    n = filein.readline().rstrip('\n')
    #res = tidy(n)
    res = tidy2(n)
    lines.append('Case #{}: {}'.format(i, res))
    print('Case #{}: {}'.format(i, res))
filein.close()

fileout = open('B-large.out', 'w')
for i in lines:
    fileout.write(i + '\n')
fileout.close()



