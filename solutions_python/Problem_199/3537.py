'''
Created on Apr 8, 2017

@author: Admin
'''

def flipStr(ops,start,k):
     
    for h in range(start,start+k):
        if ops[h]=='-':
            ops[h] = '+'
        else:
            ops[h]='-'     

def getOptimumFlips():
    with open(r'F:\CodeJam2017\ProblemA\large.in','r') as rp:
        with open(r'F:\CodeJam2017\ProblemA\large.out','w') as wp:
            tcs = int(rp.readline())
            for tc in range(1,tcs+1):
                ps,k = rp.readline().split()
                k = int(k)                                
                if '-' not in ps:
                    wp.write('Case #{}: {}\n'.format(tc,0))
                else:
                    if '+' not in ps:
                        if len(ps)%k==0:
                            wp.write('Case #{}: {}\n'.format(tc,int((len(ps)/k))))
                        else:
                            wp.write('Case #{}: {}\n'.format(tc,'IMPOSSIBLE'))
                    else:
                        if len(ps)<k:
                            wp.write('Case #{}: {}\n'.format(tc,'IMPOSSIBLE'))
                            continue                       
                        flipCount = 0
                        ps = list(ps)
                        start = 0                        
                        ops = ps[:]
                        res = None
                        for start in range(len(ps)):
                            if ops[start]=='-':
                                if (len(ops)-start)<k:
                                    res = 'IMPOSSIBLE'
                                    break
                                flipCount +=1
                                flipStr(ops,start,k)
                                                             
                                if '-' not in ops:
                                    break                                
                                for index,ele in enumerate(ops):
                                    if ele=='-':
                                        start = index
                                        break                                
                               
                                if (len(ops)-start)<k:
                                    res = 'IMPOSSIBLE'
                                    break
                            else:                               
                                continue
                        if res:
                            wp.write('Case #{}: {}\n'.format(tc,'IMPOSSIBLE'))
                        else:
                            if '-' in ops:
                                wp.write('Case #{}: {}\n'.format(tc,'IMPOSSIBLE'))
                            else:
                                wp.write('Case #{}: {}\n'.format(tc,flipCount))
                    
def main():
    getOptimumFlips()

if __name__=='__main__':
    main()
         