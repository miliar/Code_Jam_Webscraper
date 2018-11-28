import numpy as np
import csv
def calculate(n):
	while n >= 0:
		flag = 0
		#print(n)
		temp = n
		l = []
		while temp > 0:
			l.append(temp%10)
			temp /= 10
		for i in range(len(l)-1):
			if l[i] < l[i+1]:
				n -= 1
				flag = 1
				break
		if flag == 1:
			continue		
		return n 
    
if __name__ == '__main__':
    f = open('o.txt', 'w')
    with open("inp.txt") as file: 
        reader = csv.reader(file, delimiter=' ')
        i = 0
        for row in reader:
            if i == 0:
                T = row
            else :
                w = row
                s = int(w[0])
               # print(int(w[0]))
                num = calculate(s)
                f.write('Case #{}: {}\n'.format(i,num))  # python will convert \n to os.linesep
            i+=1
    f.close()
