nodes = []
inf = 100000000

def ok(val):
    return val < inf

def bad(val):
    return val >= inf

class Node:
    def __init__(self):
        self.and_gate = None
        self.changable = None
        self.value = None
        self.first = None
        self.second = None

    def interior(self):
        return self.first != None

    def __str__(self):
        try:
            fi = nodes.index(self.first)
        except:
            fi = -1
        try:
            si = nodes.index(self.second)
        except:
            si = -1
        return str([self.and_gate, self.changable, self.value,
                    fi, si])
        


def make_value(node, value):
    if node.interior():
        if node.and_gate:
            if value == 0:
                n = make_value(node.first, 0)
                m = make_value(node.second, 0)
                if bad(n) and bad(m):   return inf
                if ok(n) and ok(m):     return min(n, m)
                if ok(n): return n
                if ok(m): return m
            else:
                n = make_value(node.first, 1)
                m = make_value(node.second, 1)
                if bad(n) and bad(m):   return inf
                if ok(n) and ok(m):
                    if node.changable:
                        return min(n + m, n + 1, m + 1)
                    else:
                        return n + m
                if ok(n):
                    if node.changable:
                        return n + 1
                    else:
                        return inf
                if ok(m):
                    if node.changable:
                        return m + 1
                    else:
                        return inf
        else:
            if value == 0:
                n = make_value(node.first, 0)
                m = make_value(node.second, 0)
                if bad(n) and bad(m):   return inf
                if ok(n) and ok(m):
                    if node.changable:
                        return min(n + m, n + 1, m + 1)
                    else:
                        return n + m
                if ok(n):
                    if node.changable:
                        return n + 1
                    else:
                        return inf
                if ok(m):
                    if node.changable:
                        return m + 1
                    else:
                        return inf
            else:
                n = make_value(node.first, 1)
                m = make_value(node.second, 1)
                if bad(n) and bad(m):   return inf
                if ok(n) and ok(m):     return min(n, m)
                if ok(n): return n
                if ok(m): return m
    else:
        if node.value == value:
            return 0
        else:
            return inf

        
if __name__ == '__main__':
    N = input()
    for case in range(N):
        M, V = map(int, raw_input().split(' '))

        nodes = []
        for i in range((M - 1) / 2):
            G, C = map(int, raw_input().split(' '))
            n = Node()
            n.and_gate = (G == 1)
            n.changable = (C == 1)
            if i != 0:
                p = nodes[(i - 1) / 2]
                if i % 2 == 1:
                    p.first = n
                else:
                    p.second = n
            nodes.append(n)

        for i in range((M + 1) / 2):
            I = input()
            n = Node()
            n.value = I

            index = i + (M - 1) / 2
            p = nodes[(index - 1) / 2]
            if i % 2 == 1:
                p.first = n
            else:
                p.second = n
            nodes.append(n)

        root = nodes[0]
        n = make_value(root, V)
        print "Case #%d:" % (case + 1),
        if ok(n):
            print n
        else:
            print "IMPOSSIBLE"

        
            
            
    
