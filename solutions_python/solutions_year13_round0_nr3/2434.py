#!/usr/bin/python
import sys
import math

def main():
	f = open(sys.argv[1]).read().splitlines()
	n = int(f[0])
	i = 0
	while i < n :
		i = i + 1
		a = f[i].split()
		num1 = int(a[0])
		num2 = int(a[1])
		ans = 0
		begining = int(math.sqrt(num1))
		if begining*begining == num1 and palindrome(str(begining)) and palindrome(str(num1)):
				ans = ans + 1
		begining = begining + 1
		while(not palindrome(str(begining))):
			begining = begining + 1
		value = begining * begining
		while value <= num2 :
			check = palindrome(str(value))
			if check == True:
				ans = ans + 1
			begining = begining + 1
			while(not palindrome(str(begining))):
				begining = begining + 1
			value = begining * begining
		print "Case #" + str(i) + ": " + str(ans)

def palindrome(n):
    index=0
    check=True
    while index<len(n):
        if n[index]==n[-1-index]:
            index+=1
            return True
        return False

if __name__=='__main__':
	main()
