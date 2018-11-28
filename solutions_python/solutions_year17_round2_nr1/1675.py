#input_file_name = 'example.txt'
input_file_name = 'A-small-attempt7.in'


with open(input_file_name, 'r') as in_file:
    lines = map(lambda t: t.strip(), in_file.readlines())
    T = float(lines[0])
    testcases = []
    cur = 1
    for i in xrange(0,int(T)):
        D = float(lines[cur].split(' ')[0])
        N = float(lines[cur].split(' ')[1])
        cur +=1
        horses = []
        for j in xrange(0,int(N)):
            K = float(lines[cur].split(' ')[0])
            S = float(lines[cur].split(' ')[1])
            cur +=1
            horse = {}
            horse['K'] = K
            horse['S'] = S
            horses.append(horse)
        testcase = {}
        testcase['D'] = D
        testcase['N'] = N
        testcase['horses'] = horses
        testcases.append(testcase)

#print testcases
def calc_testcase(testcase):
    horses = sorted(testcase['horses'], key=lambda h: h['K'], reverse=True)
    D = testcase['D']
    N = testcase['N']
    print horses
    print 'D:{}, N:{}'.format(D,N)
    for i in xrange(0,len(horses)):
        K = horses[i]['K']
        S = horses[i]['S']
        if i==0:
            avg = S
        else:
            Kt = horses[i - 1]['K']
            St = horses[i - 1]['S']
            if ((S-St) != 0):
                t = (Kt-K)/(S-St)
            else:
                t = -1
            #print t
            ttc_initial = (D-K)/S
            if t < 0 or t > ttc_initial: #(t*S) > D-K:
                avg = S
            else:
                S1 = S
                S2 = St
                t1 = t
                X2 = D-K-(t*S1)
                t2 = X2/S2
                avg = (S1*t1+S2*t2)/(t1+t2)
        ttc = (D-K)/avg
        horses[i]['avg'] = avg
        horses[i]['ttc'] = ttc
    print horses
    A_S = D/horses[int(N)-1]['ttc']
    return A_S

print calc_testcase(testcases[46])

with open(input_file_name + '_out.txt','w') as f_out:
    for l in xrange(0,len(testcases)):
        print '\n\n\n===============================\n\n\n'
        #if l == 62:
        #    print 'here'
        A_S = round(calc_testcase(testcases[l]),6)
        print 'Case #{}: '.format(l+1) + '{0:f}'.format(A_S)
        f_out.write('Case #{}: '.format(l+1) + '{0:f}'.format(A_S)+'\n')
