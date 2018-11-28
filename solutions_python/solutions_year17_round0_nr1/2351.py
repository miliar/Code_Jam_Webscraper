# coding: utf-8

def main():
	T = input()
	for ka in range(T):
		data = raw_input().split()
		pancake = data[0]
		sz = int(data[1])
		lst = []
		for x in pancake:
			if x == '+':
				lst.append(1)
			else:
				lst.append(0)
				
		ans = 0
		
		# print lst
		
		for i in range(len(lst)):
			if lst[i] == 1:
				continue
			else:
				if i+sz > len(lst):
					ans = "IMPOSSIBLE"
					break
				for j in range(sz):
					lst[i+j] = (lst[i+j]+1) % 2
				ans = ans + 1
		
		print "Case #{}: {}".format(ka+1, ans)

if __name__ == '__main__':
	main()