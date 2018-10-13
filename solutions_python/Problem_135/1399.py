#!/usr/bin/python 
#Bad magician!
# Case #3: Volunteer cheated!
import sys

def main():
	T = int(sys.stdin.readline().strip())
	for i in range(T):
		s = sys.stdin.readline()
		number_str = s.split()
		t1 = int(number_str[0])
		for j in range(4) :
			s = sys.stdin.readline()
			if j == t1-1  :
				num1 = s.split()
		s = sys.stdin.readline()
		number_str = s.split()
		t2 = int(number_str[0])
		for j in range(4) :
			s = sys.stdin.readline()
			if j == t2-1  :
				num2 = s.split()
		c = 0
		for k in range(4) :
			if num1[k] in num2 : 
				c+=1
				tmp = num1[k]
		sys.stdout.write('Case #{}: '.format(i+1))
		if c == 0: 
			sys.stdout.write('Volunteer cheated!\n')
		if c >= 2:
			sys.stdout.write('Bad magician!\n')
		if c==1 :
			sys.stdout.write('%s\n' %tmp)
		
        
        
        
        

if __name__ == '__main__':
	main()
