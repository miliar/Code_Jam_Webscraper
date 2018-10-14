

if __name__ == '__main__':
        name = 'A-small-attempt5'
	inf = open(name+'.in', 'r')
	outf = open(name+'c.out', 'w')

	string = inf.readline()
        T = int(string)
        for i in range(1, T+1):
                string = inf.readline()
                parts = string.rsplit(' ')
                A = int(parts[0])
                N = int(parts[1])

                string = inf.readline()
                parts = string.rsplit(' ')

                ls = []
                for e in parts:
                        ls.append(int(e))

                ls.sort()
                num = 0
                if (A==1):
                        num = N
                else:
                        for j in range (0, N):
                                if (ls[j]<A):
                                        A = A + ls[j]
                                else:
                                        o1 = N - j
                                        o2 = 0
                                        while(A<=ls[j]):
                                                A = 2*A-1
                                                o2 = o2 + 1
                                        if (o2 < o1):
                                                A = A + ls[j]
                                                num = num + o2
                                        else:
                                                num = num + o1
                                                break
                                                
                                        '''
                                        if (ls[j]<2*A):
                                                #A = A*2 - 1 + ls[j]
                                                A = 2* ls[j] + 1
                                                num = num +1
                                        else:
                                                num = num + (N-j)
                                                break
                                        '''
                outf.write('Case #'+str(i)+': '+str(num)+'\n')

        inf.close()
        outf.close()
