f = open('C-small-attempt0.in','r')

def permute(a):
        a = a[-1] + a[0:-1]
        return a
def NumOfPerm(a):
        if (len(a) % 2 == 0) and (a[0:len(a)/2] == a[len(a)/2:]):
                q = len(a)/2
        else:
                q = len(a)
        return q
                

NumberOfCases = int(f.readline())
CaseNumber = 1
for i in range(NumberOfCases):
        ans = 0
	num = [int(j) for j in f.readline().split()]
	A = num[0]
	B = num[1]
	for i in range(A,B+1):
                a = str(i)
                p = NumOfPerm(a)
                for j in range(p-1):
                        a = permute(a)
                        if int(a) < i and A <= int(a):
                                ans = ans + 1
                                #print a, i

	value = 'Case #{}: {}'.format(CaseNumber,ans)
	CaseNumber = CaseNumber + 1
        print value
