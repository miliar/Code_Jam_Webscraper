CASE_SIZE = 1


def num_recyle_pairs(a,b):
    pairs = set()
    for n in xrange(a,b+1):
        n = str(n)
        for digits in xrange(len(n)-1):
            digits = digits +1
            m = n[len(n)-digits:] + n[:len(n)-digits] 
            
            m = int(m)
            if  a <= int(n) and int(n) < m and m <=b:
                pairs.add((n,m))
    return len(pairs)  


def main():
    with open('input.txt') as f:        
        all_lines = f.readlines()
        
    num_cases = int(all_lines[0])
    result = []
    for case_nbr in xrange(num_cases):
        
        a, b = [int(x) for x in all_lines[case_nbr*CASE_SIZE+1].strip().split(" ")]
        num = num_recyle_pairs(a,b)
        result.append( "Case #%s: %s\n" % (case_nbr+1, num))
#    
    with open('output.txt','w') as f:        
        all_lines = f.writelines(result)

main()
print "done"