def main():
	tc = int(raw_input())
	for loop in range(0, tc):
		A, B, K = map(int, raw_input().split())
		count = 0
		for i in range(0, A):
			for j in range(0, B):
				if (i&j)<K:
					count=count+1
		res = "Case #"+str((loop+1))+": "+str(count)
		print res
main()