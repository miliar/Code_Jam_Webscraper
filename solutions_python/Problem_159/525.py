fr = open('in', 'r')
fw = open('out', 'w')

def main():
	case_num = int(fr.readline().strip())
	for case in range(case_num):
		line = fr.readline().strip()
		n = int(line)
		s = fr.readline().strip().split()
		s = [int(i) for i in s]
		ans1=0
		mi = 0
		for i in range(n-1):
			ans1 += max(0, s[i]-s[i+1])
			mi = max(mi, s[i]-s[i+1])
		ans2 = mi*(n-1)
		for i in range(n-1):
			if s[i]<mi:
				ans2-=mi-s[i]
		print 'Case #%d: %d %d' % (case+1, ans1, ans2)
		fw.write('Case #%d: %d %d\n' % (case+1, ans1, ans2))
	fr.close()
	fw.close()


if __name__ == '__main__':
	main()