import sys

def product(vec1, vec2):
    sum = 0
    for i in xrange(len(vec1)):
        sum += vec1[i] * vec2[i]
    return sum
def process(r):
    r.readline()
    vec1_str = r.readline()
    vec2_str = r.readline()
    
    vec1 = [int(n_str) for n_str in vec1_str.split(" ")]
    vec2 = [int(n_str) for n_str in vec2_str.split(" ")]
    
    vec1.sort()
    vec2.sort()
    vec2.reverse()
    return product(vec1,vec2)
    
def main():
    if len(sys.argv) > 1:
        
        r1 = open(sys.argv[1])
        cases_str = r1.readline()
        cases = int(cases_str)
        for x in xrange(cases):
            
            val =  process(r1)
            print "Case #%d: %d"%(x+1, val)
main()
