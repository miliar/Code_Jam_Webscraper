import sys

def recycled_n_digits(n):
    if n == 0:
        return 0
m_bob = {}
def is_recycled(a,b):
    if (a,b) in m_bob:
        return m_bob[(a,b)]
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        failure = False
        for j in range(len(b)):
            if(a[(i+j) % len(a)] != b[j]):
                failure = True
                break
        if not failure:
            m_bob[(a,b)] = True
            return True
    m_bob[(a,b)] = False
    return False

def count_range(a,b):
    count =0
    for x in range(a,b+1):
        for y in range(a,b+1):
            if x == y:
                continue
            if is_recycled(str(x),str(y)):
                count += 1
    return count/2

def handle_lines(lines):
    for i, line in enumerate(lines):
        a,b = map(int, line.split(" "))
        print "Case %s: %s" % (i+1, count_range(a,b))
 
if __name__=='__main__':
    handle_lines(open(sys.argv[1]).readlines()[1:])
