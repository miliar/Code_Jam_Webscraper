dic = {
    '11': ('1', 1),
    '1i': ('i', 1),
    '1j': ('j', 1),
    '1k': ('k', 1),
    'i1': ('i', 1),
    'ii': ('1', -1),
    'ij': ('k', 1),
    'ik': ('j', -1),
    'j1': ('j', 1),
    'ji': ('k', -1),
    'jj': ('1', -1),
    'jk': ('i', 1),
    'k1': ('k', 1),
    'ki': ('j', 1),
    'kj': ('i', -1),
    'kk': ('1', -1)
}


def eva(s):
    if len(s) == 0:
        return
    pos, res = 1, '1'
    for i in xrange(len(s)):
        cur = res+s[i]
        res = dic[cur][0]
        pos *= dic[cur][1]
    if pos > 0:
        return (1, res)
    else:
        return (-1, res)
    

# for case in range(int(raw_input())):
#     L, X = map(int, raw_input().split())
#     res = False
#     s = raw_input()
#     if X > 12:
#         X %=4
#     s *= X
#     left, right = 1, len(s) - 1
#     ll, rr = s[0], s[-1]
#     while right > left:
#         if dic[ll+s[left]] != (1, 'i'):
#             ll = dic[ll+s[left]][0]
#             left += 1
#             continue
#         if dic[s[right]+rr] != (1, 'k'):
#             rr = dic[s[right]+rr][0]
#             right -= 1
#             continue
#         if eva(s[left:right]) == (1, 'j'):
#             res = True
#             break
#     if res:
#         print "Case #%d: %s" % (case+1, 'YES')
#     else:
#         print "Case #%d: %s" % (case+1, 'NO')



    
for case in range(int(raw_input())):
    L, X = map(int, raw_input().split())
    res = False
    s = raw_input()
    if X > 12:
        X %=4
    s *= X
    left, right = 1, len(s) - 1
    while right > left:
        if eva(s[:left]) != (1, 'i'):
            left += 1
            continue
        if eva(s[right:]) != (1, 'k'):
            right -= 1
            continue
        if eva(s[left:right]) == (1, 'j'):
            res = True
            break
    if res:
        print "Case #%d: %s" % (case+1, 'YES')
    else:
        print "Case #%d: %s" % (case+1, 'NO')

                
    
