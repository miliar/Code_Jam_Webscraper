import os

def read_input():
	file_name = "%s/large.in" % os.getcwd()
	return open(file_name, "r")

def method2(nums):
	max_rate = 0
	for i in range(len(nums)-1):
		if nums[i] - nums[i+1] > max_rate:
			max_rate = nums[i] - nums[i+1]
	ans = 0
	for i in range(len(nums)-1):
		if nums[i] <= max_rate:
			ans += nums[i]
		else:
			ans += max_rate
	return ans

def method1(nums):
	ans = 0
	for i in range(len(nums)-1):
		if nums[i] > nums[i+1]:
			ans += nums[i] - nums[i+1]
	return ans

def get_ans(nums, case):
	ans = "%d %d" % (method1(nums), method2(nums))
	return "Case #%d: %s" % (case, ans)

def make_output(ans):
	file_name = "%s/large.out" % os.getcwd()
	f = open(file_name, "w")
	f.write(ans)
	f.close()

def main():
	ans = ""
	f = read_input()
	
	T = int(f.readline())
	for i in range(T):
		print i
		N = int(f.readline())
		nums = [int(x) for x in f.readline().split()]
		ans += get_ans(nums, i+1)
		if i < T-1: ans += "\n"

	f.close()
	make_output(ans)

main()

print get_ans([10, 5, 15, 5], 1)
print get_ans([100, 100], 2)
print get_ans([81, 81, 81, 81, 81, 81, 81, 0], 3)
print get_ans([23, 90, 40, 0, 100, 9], 4)
print get_ans([100, 0, 100, 0, 100, 0, 100, 0, 100, 0], 5)

