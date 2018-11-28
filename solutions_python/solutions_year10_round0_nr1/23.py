
def OnOrOff(n, k):
	Circle = 2**n
	R = k % Circle
	if R==(Circle-1):
		return 'ON'
	else:
		return 'OFF'

def main():
	T = int(raw_input())
	case = 1;
	while T>=case:
		line = raw_input().split()
		n = int(line[0])
		k = int(line[1])
		print 'Case #%d: %s' %(case, OnOrOff(n,k))
		case += 1

if __name__ == '__main__':
	main()
