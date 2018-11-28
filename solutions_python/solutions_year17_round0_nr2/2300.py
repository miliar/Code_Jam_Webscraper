#!/usr/bin/env python3
import sys

T = int(sys.stdin.readline())

def main():
	for x in range(1, T+1):
		print("Case #{}: ".format(x), end="")
		num = int(sys.stdin.readline())
		N = list(str(num))
		i = 0
		while (i < len(N)-1):
			if(N[i+1] >= N[i]):
				i += 1
			else:
				break
		
		if (i != len(N)-1):
			while(i>0 and N[i] == N[i-1]):
				i = i - 1
			new = int("".join(N[:i+1]))
			new = new * 10**(len(N)-i-1)
			new = new - 1
			print(new)
		else:
			print("".join(N))
		
if __name__ == "__main__":
    main()