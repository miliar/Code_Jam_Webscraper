import sys

if __name__ == '__main__':
    input = open(sys.argv[1],'r')
    output = open(sys.argv[2], 'w')
    
    T = int(input.readline())
    
    for t in range(1, T+1):
        N = int(input.readline())
        ropes = []
        points = 0
        
        for n in range(N):
            next = map(int, input.readline().split())
            print "Adding "+str(next)+" to ropes"
            for rope in ropes:
                print "Comparing "+str(next)+" to "+str(rope)
                if (next[0]>rope[0]) ^ (next[1]>rope[1]):
                    print "They cross!!"
                    points += 1
            ropes.append(next)
        output.write("Case #%d: %d\n"%(t, points))
        