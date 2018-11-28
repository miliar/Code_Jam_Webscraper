import sys

def minimum_add(pool):
    current_clap = 0
    adder_tot = 0
    for i,j in enumerate(pool): 
        if current_clap < i:
            adder = (i-current_clap)
            adder_tot += adder
            current_clap += adder
        current_clap +=j 
    return adder_tot 

if __name__ == '__main__':
    N = int(raw_input())
    for i in range(N):
        length,pool = tuple(raw_input().split())
        pool = [int(l) for l in str(pool)]
        print "Case #"+str(i+1)+": "+str(minimum_add(pool))

