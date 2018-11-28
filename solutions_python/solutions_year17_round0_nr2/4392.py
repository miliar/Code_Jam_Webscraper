import sys
def func(num):
        temp = num
	while(temp > 0):
                last = temp%10
		temp = temp/10
		if last < temp%10:
                        return False
        return True

fname = 'input1.txt'
with open(fname) as f:
        content = f.readlines()
        num = content[1:]

orig_stdout = sys.stdout
fout = open('out1.txt', 'w')
sys.stdout = fout
for j,i in enumerate(num):
        temp = int(i)
        while temp > 0:
                if func(temp):
                        print 'Case #'+str(j+1)+': '+str(temp)
                        temp = 0
                else:
                        temp = temp-1
	
sys.stdout = orig_stdout
f.close()
fout.close()
