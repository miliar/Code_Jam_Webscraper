#!/usr/bin/python


def check_one_test(fo) :

	inp=fo.readline().strip().split()
	N=int(inp[0])

	val=0
	cum=0
	for i in range(N+1):
		cum = cum+int(inp[1][i])
		if cum < i+1 :
			diff = i+1-cum 
			val = val + diff
			cum = cum + diff

	return val


# fo = open("1.inp", "r")
# fo = open("A-small-attempt0.in", "r")
fo = open("A-large.in", "r")
#fo = open("inp2", "r")
# fw = open("1.out", "w")
# fw = open("A-iiiii.out", "w")
fw = open("A-XXXXX.out", "w")
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
