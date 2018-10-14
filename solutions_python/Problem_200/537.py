import sys

def main():
	T = int(input())

	for t in range(1, T+1):
		num = input()
		size = len(num)
		num = list(num)

		changed = True
		while changed:
			changed = False
			for i in range(1, size):
				if num[i-1] > num[i]:
					num[i-1] = chr(ord(num[i-1])-1)
					for j in range(i,size):
						num[j] = str(9)
					changed = True
					break
					
		if num[0] == '0':
			del num[0]
		print ("Case #" + str(t) + ": " + "".join(num))

if __name__ == "__main__":
	main()
# 321513
# 299999 