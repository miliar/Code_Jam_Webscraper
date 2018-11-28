import sys

num_cases = int(sys.stdin.readline())

for case in range(1, num_cases+1):
    A, B = map( int, sys.stdin.readline().split() )
    success_probs = map( float, sys.stdin.readline().split() )
    unsuccess_probs = map( lambda x: 1.0-x , success_probs)
    
    probs = [unsuccess_probs,success_probs]
        
    opt1 = 0.0
    opt2 = [0.0] * A
    opt3 = 1 + B + 1
        
    for i in range(2**A):
        binary_str = bin(i)
        binary_str = binary_str[2:]
        
        binary_str = '0' * (A - len(binary_str)) + binary_str
        assert len(binary_str) == A
        
        binary_str = map(int,binary_str)
        
        prob = 1.0
        for k in range(A):
            prob *= probs[binary_str[k]][k]    
        
        #opt1
        for k in range(A):
            if binary_str[k] == 0:
                opt1 += prob * ((B-A)+1+B+1)
                break
        else:
            opt1 += prob * ((B-A)+1)
            
        #opt2
        for num_back in range(1,A+1):
            for k in range(A-num_back):
                if binary_str[k] == 0:
                    opt2[num_back-1] += prob * (num_back + num_back + (B-A)+1+B+1)
                    break
            else:
                opt2[num_back-1] += prob * (num_back + num_back + (B-A) +1)
        
    opt2.append(opt1)
    opt2.append(opt3)
    min_keys = min(opt2)
    print "Case #%s: %s" % (case, min_keys)
        
               
                
        
        
        
            
         
    