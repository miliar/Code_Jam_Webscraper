import math, collections, copy, sys
f = open('input.in','r')
g = open('output.txt','w')
"""

"""
combos = ['BO','RG','YV']
letters = ['B', 'R', 'Y']
for index in xrange(1, int(f.readline()[:-1]) + 1):
    N, R, O, Y, G, B ,V = [int(x) for x in f.readline()[:-1].split(' ')]
    if (B and B <= O) or (R and R <= G) or (Y and Y <= V):
        result = 'IMPOSSIBLE'
    else:
        s = [B-O, R-G, Y-V]
        i = max([0,1,2], key = lambda i:s[i])
        j = (i+1)%3
        k = (i+2)%3
        nums = [O,G,V]
        if 2*s[i] > sum(s):
            result = 'IMPOSSIBLE'
        elif s[j] == 0 or s[k] == 0:
            if s[j] == 0:
                j,k = k,j
            result = combos[j]*nums[j]+letters[j] + combos[i]*nums[i]+letters[i] + (letters[j]+letters[i])*(s[i]-1)
        elif s[i] == s[j] and s[i] == s[k]:
            result = combos[j]*nums[j]+letters[j] + combos[i]*nums[i]+letters[i] + combos[k]*nums[k]+letters[k] + (letters[j]+letters[i]+letters[k])*(s[i]-1)
        elif s[i] == s[j] or s[i] == s[k]:
            if s[i] == s[k]:
                j,k = k,j
            result = [combos[j]*nums[j]+letters[j] + combos[i]*nums[i]+letters[i] + combos[k]*nums[k]+letters[k]  ]
            result.append((letters[j]+letters[i]+letters[k])*(s[k]-1))
            result.append((letters[j]+letters[i])*(s[i]-s[k]))
            result = ''.join(result)
        else:
            result = [combos[j]*nums[j]+letters[j] + combos[i]*nums[i]+letters[i] + combos[k]*nums[k]+letters[k]  ]
            result.append( (letters[j]+letters[i]+letters[k])*(s[j]+s[k]-s[i]) )
            result.append(letters[i])
            s[i], s[j], s[k] = 2*s[i]-s[j]-s[k]-2, s[i]-s[k]-1, s[i]-s[j]-1
            while s[i]:
                if s[j]:
                    result.append(letters[j])
                    s[j] -= 1
                else:
                    result.append(letters[k])
                    s[k] -= 1
                result.append(letters[i])
                s[i] -= 1
            result = ''.join(result)
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()