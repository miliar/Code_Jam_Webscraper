import sys

def cons( ary ):
    for i in range(len(ary)-1):
        yield ary[i], ary[i+1]

class Snapper:
    def __init__(self):
        self.power = False
        self.active = False
        
    def __repr__(self):
        ret = ""
        if self.power:
            ret+="="
        else:
            ret+="-"
        
        if self.active:
            ret+="o"
        else:
            ret+="x"
            
        if self.power and self.active:
            ret+="="
        else:
            ret+="-"
            
        return ret
        
    def int(self):
        return int(self.power and self.active)
        
def snapper_states( K ):
    return list(reversed([x=="1" for x in bin(K)[2:]]))
        
def passes_current( states, N ):
    return (False not in states[:N]) and len(states)>=N
    

def problem_1( N, K ):
    snappers = []
    for i in range(N):
        snappers.append( Snapper() )
        
    # if there are no snappers, the light is always on, I guess
    if N==0:
        return True
        
    snappers[0].power = True
    
    for i in range(K):
        # toggle the active state on every snapper with power
        for snapper in snappers:
            if snapper.power:
                snapper.active = not snapper.active
    
        for j, (last, next) in enumerate( cons(snappers) ):
            next.power = last.power and last.active
            
        print "".join( [str(x) for x in snappers] ), i+1, sum( [x.int() for x in snappers] ), bin(i+1)
    print bin(K)
    print snapper_states(K)
            
    return snappers[-1].power and snappers[-1].active


def problem_1_v2( N, K ):
    return passes_current( snapper_states( K ), N )
            
        
if __name__=='__main__':
    
    filename = sys.argv[1]
    filename_out= sys.argv[2]
    
    fpout = open( filename_out, "w" )
    
    lines = open( filename ).read().split("\n")
    
    n = int(lines[0])
    
    for i in range(n):
        
        N, K = [int(x) for x in lines[i+1].split()]
        print N, K
            
        #a1 = problem_1( N, K )
        a2 = problem_1_v2( N, K )
            
        fpout.write( "Case #%d: "%(i+1) + ("ON" if a2 else "OFF") + "\n" )
            
    
    
    
