s = set()
def neg(k):
    l = ['+' if x =='-' else '-' for x in k]
    return ''.join(l)
def get_list(v, k, count):

    k = [v[:x]+neg(v[x:x+k]) + v[x+k:] for x in range(len(v)-k+1)]

    v = [x for x in k if (x not in s)]
    s.update(v)
    return zip(v, [count+1]*len(v))


def bfs(st, k):

    final = '+'*len(st)

    u = (st,0)
    l = [u]
    while len(l):
        r = l.pop(0)

        stn, count = r
        if final == stn:
            return count
        get = get_list(stn,k,count)
        l.extend(get)
    else:
        return 'IMPOSSIBLE'

#
v = open('A-small-attempt0.in', 'r')
t = open('out.txt', 'w')
r = int(v.readline())

l = [v.readline().split() for x in range(r)]

for i,x in enumerate(l):
    print(x)
    t.writelines('Case #{0}: {1}\n'.format(i+1, bfs(x[0], int(x[1]))))
    s.clear()

t.close()
v.close()
# # print(fun(995))
#
# t = '-+-+-'
#
# print(bfs(t,4))
# # get_list(t, 3, 0)
# print(get_list(t, 3, 0)
# )