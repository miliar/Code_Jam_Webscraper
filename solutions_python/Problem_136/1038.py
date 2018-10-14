#!/usr/bin/python


def check_one_test(fo) :
	t1=0.0
	t2=0.0
	T=0.0
	r=2.0

	inp=fo.readline().strip().split()
	C=float(inp[0])
	f=float(inp[1])
	X=float(inp[2])

	t1=X/r
	while(1):
		T+=C/r
		t2=T+X/(r+f)
		if(t2 > t1):
			 break
		else:
			t1=t2
		r+=f;
	return t1


fo = open("B-large.in", "r")
#fo = open("inp2", "r")
fw = open("B-XXXXX.out", "w")
no_of_cases = int(fo.readline().strip())
#print no_of_cases
count = 1
while no_of_cases:
    val = check_one_test(fo)

    #print("Case #" + str(count) + ": " + str(val) + "\n")
    fw.write("Case #" + str(count) + ": " + str(val) + "\n")

    no_of_cases =  no_of_cases - 1
    count = count + 1

fo.close
fw.close
