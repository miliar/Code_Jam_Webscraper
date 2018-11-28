#probably the ugliest code I ever written (except in school maybe)

import sys, math
    
def main():
    if len(sys.argv) < 2:
        print ('usage: python something.py input_filename')
        quit()
        
    f = open(sys.argv[1], 'r')
    out = open("out", 'w')
    
    cases = int(f.readline()) #number of cases
    
    for case in range(cases):    
        print '\nCase', case+1
        
        line = f.readline().split()
        
        n_c = int(line[0]) #number of combines
        combines = line[1:n_c+1]
        combines = map(list, combines)
        print "combine:", combines
        
        last = n_c + 1
        n_d = int(line[last]) #number of opposed
        opposed = line[last+1:last+n_d+1]
        opposed = map(list, opposed)
        print 'opposed:', opposed
        
        last = last+n_d+2
        invoke = line[last]
        
        result = []
        
        for c in list(invoke):
            combined = False
            cleared = False
            
            #check if combines with last one
            if len(result) > 0:       
                for comb in combines:
                    if (comb[0] == result[-1] and comb[1] == c) or \
                        (comb[1] == result[-1] and comb[0] == c):
                        result[-1] = comb[2]
                        combined = True            
                        break
            if combined:
                print 'invoke', c, "combined:", result
                continue
                
            #check if opposed
            for o in opposed:
                if c in list(o):
                    for c2 in result:
                        if c2 != c and c2 in list(o):
                            cleared = True
                            break
            if cleared:
                result = []
                print 'invoke', c, "cleared", result
                continue 
                    
            result.append(c)
            print 'invoke', c, result
            
        out.write('Case #{0}: {1}\n'.format(case+1, "[" + ", ".join(result) + "]"))
    out.close()
    
if __name__ == "__main__":
    main()