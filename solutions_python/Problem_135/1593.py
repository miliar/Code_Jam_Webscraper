import sys

def main():
	# how many test cases we have
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		row = int(raw_input())
		rows = [map(int, raw_input().split()) for j in range(4)]
		nums1 = set(rows[row-1])
		
		row = int(raw_input())
		rows = [map(int, raw_input().split()) for j in range(4)]
		nums2 = set(rows[row-1])
		
		nums = nums1 & nums2
		if len(nums) == 0:
			msg = 'Volunteer cheated!'
		elif len(nums) == 1:
			msg = str(nums.pop())
		else: # len(nums) > 1
			msg = 'Bad magician!'
		
		print 'Case #%d: %s' % (i+1, msg)

if __name__ == '__main__':
	main()