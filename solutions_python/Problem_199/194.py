def str_to_list(string):
    ret_list = []
    for i in xrange(len(string)):
        if string[i] == '+':
            ret_list.append(True)
        elif string[i] == '-':
            ret_list.append(False)
    return ret_list

def flip_cakes(pancakes, K):
    cakes_list = str_to_list(pancakes)
    y = 0
    for i in xrange(len(cakes_list)-K+1):
        if not cakes_list[i]:
            y += 1
            for j in xrange(K):
                cakes_list[i+j] = not cakes_list[i+j]
    for i in xrange(K):
        if not cakes_list[-i-1]:
            return 'IMPOSSIBLE'
    return y
    


t = int(raw_input())

for x in xrange(1, t+1):
    pancakes, K = raw_input().split(' ')
    K = int(K)
    print 'Case #{}: {}'.format(x, flip_cakes(pancakes, K))