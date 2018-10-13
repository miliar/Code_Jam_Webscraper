
def main():
	for case in xrange(int(raw_input())):
		d, n = map(int, raw_input().split())
		horses = []
		for i in xrange(n):
			horses.append((map(float, raw_input().split())))
		time = max([(d - horse[0]) / horse[1] for horse in horses])
		answer = d / time
		print 'Case #{}: {}'.format(case + 1, answer)
		
if __name__ == '__main__':
	main()