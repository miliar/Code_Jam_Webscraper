import sys
import getopt

def play(C, F, X):
    cookies = 0
    rate = 2.0
    sec = 0
    while(cookies < X):
        if (X-cookies)/rate < ((C-cookies)/rate + X/(rate+F)):
            # not buying a farm, trivial solution
            sec = sec + (X-cookies)/rate
            cookies = X
        else:
            # best option buy a farm
            sec = sec + (C - cookies)/rate
            rate = rate + F
            cookies = 0
    return sec    
    
def main(argv=sys.argv):
    file = open(sys.argv[1], 'r')
    lines = int(file.readline())
    for prob in range(lines):
        line = file.readline().split()
        line = [float(i) for i in line]
        C = line[0]
        #print C
        F = line[1]
        #print F
        X = line[2]
        #print X
        print 'Case #'+str(prob+1)+': '+str(play(C, F, X))
        

if __name__ == "__main__":
    main()