#!/usr/bin/env python

def main():
	T = raw_input()
	for t in range(int(T)):
		N = int(raw_input())
		NA = map(int, raw_input().split())
        	S = 0
		for i in NA:
			S = S ^ i
		if S == 0:
			R = str(sum(NA)-min(NA))
		else:
			R = "NO"

		print "Case #"+str(t+1)+": " + R

if __name__ == "__main__":
    main()
