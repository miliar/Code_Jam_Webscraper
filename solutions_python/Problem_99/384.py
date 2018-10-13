def check(a, b, correct):
    enter = 2+b
    
    prod = correct[0]
    for i in correct[1:]:
        prod *= i
    
    t1 = (b-a + 1)
    t2 = t1 + b + 1    
    keep = t1 * prod + t2 * (1-prod)
    
    #back
    backs = [keep, enter]
    for i in range(1,len(correct)+1):
        prod /= correct[-i] 
        t1 += 2
        t2 += 2
        backs.append(t1 * prod + t2 * (1-prod))
        
    return min(backs)

if __name__ == '__main__':
    inputFile = "A-small-attempt0.in"#sys.argv[1]
        
    result = []
    fin = open(inputFile)
    cases = fin.readline().strip()
    
    for i in range(int(cases)):
        a,b = list(map(int, fin.readline().strip().split(' ')))                
        correct = list(map(float, fin.readline().strip().split(' ')))
        
        print(a,b)
        print(correct)
        
        ans = "Case #%d: %s" % (i+1, check(a,b,correct))
        result.append(ans)
        print(ans)
    
    outputFile = inputFile.replace(".in", ".out")
    f = open(outputFile,'w')
    f.write('\n'.join(result))

