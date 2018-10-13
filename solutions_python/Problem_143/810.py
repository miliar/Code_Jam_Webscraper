if __name__ == '__main__':
	FIN = open('in', 'r')
	FOUT = open('out', 'w')
	T = int(FIN.readline().rstrip('\n'))
	
	for case in range(T):
            s = map(int, FIN.readline().rstrip('\n').split(' '))
            A = s[0]
            B = s[1]
            K = s[2]
            
            c = 0
            for a in range(A):
                for b in range(B):
                    if a & b < K:
                        c += 1
            
            FOUT.write("Case #{0}: {1}\n".format(case+1, c))
