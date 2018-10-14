
INPUT = "B-small-attempt2.in"
OUTPUT = "B-small-attempt2.out"

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def solve(N,m_k):
    r = sim1(m_k)
    i = (N-1) % r
    result = sim2(i,m_k)
    return result

def sim1(m_k):
    l = lcm(m_k[0],m_k[1])
    for k in m_k[2:]:
        l = lcm(l,k)
    
    s = 0
    for k in xrange(1,l+1):
        for j in m_k:
            if (k % j == 0):
                s += 1
    return s

def sim2(n,m_k):
    workers = [0] * len(m_k)
    result = 1
    for _ in xrange(n+1):
        i = min(workers)
        index = workers.index(i)
        result = index + 1
        workers[index] += m_k[index]
        i = min(workers)
        for j,_ in enumerate(workers):
            if workers[j]>i:
                workers[j]-=i
            else:
                workers[j]=0  
    return result
                    
    

if __name__=="__main__":
    f_in = open(INPUT)
    f_out = open(OUTPUT,"w")
    lines = f_in.readlines()
    output = []
    cases = int(lines[0].strip())
    for i in range(cases):
        line = lines[2*i+1].strip()
        data = line.split(" ")
        B,N = int(data[0]),int(data[1])
        m_k = [int(j) for j in lines[2*i+2].strip().split(" ")]
        output += "Case #%d: %d\n" % (i+1,solve(N,m_k))
        print i
        
    f_out.writelines(output)
    f_out.close()
    f_in.close()
    print 'done.'
