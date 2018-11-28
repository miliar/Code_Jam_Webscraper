'''
Created on Apr 12, 2013

@author: uglytroll
'''

def check_arr(a):
    for x in xrange(len(a)):
        for y in xrange(len(a[x])):
            result = True
            for vert in xrange(len(a)):
                result = result and (a[vert][y] <= a[x][y])
                if not result:
                    break
            if result:
                continue
            else:
                result = True
                for hor in xrange(len(a[x])):
                    result = result and (a[x][hor] <= a[x][y])
                    if not result:
                        return False
    return True

f = open('/home/uglytroll/codejam/2013/qual/2a.in', 'r')
o = open('/home/uglytroll/codejam/2013/qual/2a.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    x, y = map(int, f.readline().strip().split(' '))
    a = []
    for _ in xrange(x):
        hang = map(int, f.readline().strip().split(' '))
        a.append(hang)
    is_valid = check_arr(a)
#     result_x = True
#     for b in a:
#         result_x = result_x and check_arr(b)
#     result_y = True
#     for row in xrange(y):
#         b = []
#         for col in xrange(x):
#             b.append(a[col][row])
#         result_y = result_y and check_arr(b)
    if is_valid:
        result = 'YES'
    else:
        result = 'NO'
    s = "Case #%d: %s\n" % (t+1, result)
#     print s
    o.write(s)
            
        
    