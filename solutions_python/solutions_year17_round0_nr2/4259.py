import math;

def is_tidy(arr):
	sizeArr = len(arr);
	mymin = arr[0];
	for k in range(1,sizeArr):
		if(arr[k]>mymin):
			return False;
		else:
			mymin = arr[k];
	return True;

def to_arr(num):
	size = math.floor(math.log10(num))+1;
	res = [];
	for j in range(0,size):
		res.append(num%10);
		num = (num//10);
	return res

def cleanup(arr):
	siz = len(arr);
	p = siz-1;
	while True:
		if(arr[p]>arr[p-1]):
			arr[p] = arr[p]-1;#cannot be 0
			for f in range(p-1,-1,-1):#make all 9s after
				arr[f]=9;
			break;
		p = p-1;
	return arr;
#Main
T = int(input());
for i in range(1,T+1):
	N = int(input());
	N_arr = to_arr(N);
	while True:
		if(is_tidy(N_arr)):
			prnt =''.join(map(str, reversed(N_arr)));
			print("Case #"+str(i)+": "+str(int(prnt)));
			break;
		N_arr = cleanup(N_arr);
