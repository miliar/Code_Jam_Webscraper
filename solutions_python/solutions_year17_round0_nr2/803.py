
# def find(s):
#     if len(s) == 1:
#         return s
#     res = []
#     make9 = False
#     for i in xrange(0, len(s)):
#         if make9:
#             res.append('9')
#         else:
#             curval = int(s[i])
#             if i + 1 < len(s) and curval > int(s[i + 1]):
#                 if s[i] == '1' and s[i + 1] == '0':
#                     return ''.join(['9'] * (len(s) - 1))
#                 if len(res) != 0 or curval != 1:
#                     res.append(str(curval - 1))
#                 make9 = True
#             else:
#                 res.append(s[i])
#     #if make9:
#     #    res.append('9')
#     #else:
#     #    res.append(s[-1])
#     return ''.join(res)

def find(s):
    if len(s) == 1:
        return s
    res = []
    res.append(s[-1])
    for i in xrange(len(s) - 2, -1, -1):
        curval = int(s[i])
        if i == 0 and curval == 1 and s[i + 1] == '0':
            return '9' * (len(s) - 1)
        if curval > int(res[-1]):
            #j = -2
            #while j < len(res) and res[j] != '9':
            #    res[j] = '9'
            #    j += 1
            res[-1] = '9'
            j = len(res) - 2
            while j >= 0 and res[j] != '9':
                res[j] = '9'
                j -= 1
            res.append(str(curval - 1))
        else:
            res.append(s[i])

    if res[-1] == '0':
        return ''.join(res[(len(res) - 2)::-1])
    else:
        return ''.join(res[::-1])


if __name__ == '__main__':
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        s = raw_input()
        res = find(s)
        print "Case #{}: {}".format(i, res)