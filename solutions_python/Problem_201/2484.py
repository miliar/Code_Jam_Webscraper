import sys

def get_max_index(l):
    m_i = 0
    for i in range(1, len(l)):
        if l[i] > l[m_i]:
            m_i = i
    return m_i

def be_polite(n, k):
    space = [n]
    for i in range(k):
        if not i % 100:
            print(100 * i / k, end="\r")
        max_i = get_max_index(space)
        m = space[max_i]
        ls, rs = (m - 1) // 2, m // 2
        space = space[:max_i] + [ls, rs] + space[max_i + 1:]
    return max(ls, rs), min(ls, rs)


def parser(filename):
    with open(filename.replace('in','out'), 'w') as o:
        with open(filename) as f:
            cases = int(f.readline())
            print("{} cases".format(cases))

            for i in range(cases):
                n = f.readline().replace('\n','')
                n, k = n.split(' ')
                m, mn = be_polite(int(n), int(k))
                o.write('Case #{}: {} {}\n'.format(i+1, m, mn))



if __name__ == "__main__":
    parser(sys.argv[1])
