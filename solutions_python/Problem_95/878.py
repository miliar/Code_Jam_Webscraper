#!/usr/bin/env python
import sys
import re

F=list("abcdefghijklmnopqrstuvwxyz")
T=list("YHESOCVXDUIGLBKRZTNWJPFMAQ")


U=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
L=list("abcdefghijklmnopqrstuvwxyz")

def main():
	N = int(raw_input())
	for j in range(int(N)):
		S = raw_input()
		for k in range(len(F)):
			S = S.replace(F[k], T[k]);
		for k in range(len(U)):
			S = S.replace(U[k], L[k]);
			
		print "Case #"+str(j+1)+": "+S

if __name__ == "__main__":
    main()
