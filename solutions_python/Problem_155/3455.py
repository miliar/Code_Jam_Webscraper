import sys

def main():
    f = open('A-small-attempt5.in', 'r')
    #f = open('rt.txt', 'r')
    p = open('out.in', 'w')

    n = int(f.readline().strip())

    case = 1
    for x in range(0, n):
        m, sh = f.readline().strip().split()
        
        m = int(m)
        if m == 0:
            p.write("Case #" + str(case) + ": " + str(m))
            p.write('\n')
        else:
            invite = 0
            sm = 0
            up = 0

            i = 0
            while up != m:
                if sh[i] == '0':
                    i += 1
                    continue
                else:
                    if up >= i:
                        up += int(sh[i])
                    else:
                        invite += i - up 
                        up += invite + int(sh[i])
                    
                    
                if up >= m:
                    p.write("Case #" + str(case) + ": " + str(invite))
                    p.write('\n')
                    break
                
                i+= 1
            
        case += 1
    
                    
                    
                
                
                    

        
        

if __name__ == '__main__':
    main()
