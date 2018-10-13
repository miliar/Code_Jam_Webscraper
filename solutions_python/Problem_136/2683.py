import sys
def main():
    T = int(sys.stdin.readline())
    for i in xrange(T):
        C, F, X = map(float, sys.stdin.readline().split())
        z = 2
        time = 0
        while True:
            if X/z < C/z + X/(z+F):
                time += X/z
                break;
            else:
                time += C/z
                z=z+F
        print "Case #" + str(i+1) + ": " + str(time)
        
                
        
if __name__ == "__main__":
	main();
