import sys

orig_stdout = sys.stdout
f = open('out.txt', 'w')
sys.stdout = f


def readfile():
	in_file = open("inp.txt","r")
	line = in_file.read().split("\n")
	
	return line

def main():
	lines = readfile()
	#print (lines)
	T=int(lines[0])
	tc = 1
	while tc<=T:
		print("Case #",tc,": ",sep='',end=' ')
		numstr =""
		numstr = str(lines[tc])
		tc +=1
		num = int(numstr)
		while num>=10:
			f=0
			i1 = 0
			for i in range(len(numstr)-2,-1,-1):
				i1 = i
				d1 = int(numstr[i])
				d2 = int(numstr[i+1])
				#print(d1,d2,end=' ')
				if(d2<d1):
					f=1
					break
			#print(f)
			if f==0:
				break
			#print(num)

			s1 = "9" *(len(numstr)-i1-1)
			numstr = numstr[:i] + str(d1-1) + s1
			num = int(numstr)
			#print(num)
			#num = num -1 
		print (num)

			




if __name__ == '__main__':
   main()

sys.stdout = orig_stdout
f.close()

