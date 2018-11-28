import sys
import os


def main():
	s = ''.join(sys.stdin.readlines()).split()
	os.close(0)

        T = int(s[0])
        s = s[1:]
        
        for i in range(T):
            N = int(s[0])
            K = int(s[1])
            s = s[2:]
            if K%2**N == 2**N-1:
                print "Case #" + str(i+1) + ": ON"
            else:
                print "Case #" + str(i+1) + ": OFF"



if __name__ == "__main__":
 	main()

