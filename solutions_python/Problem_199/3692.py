def oversize (lst1, num):
    count = 0
    list_ = list(lst1)
    num = int(num)
    for idx in range(len(list_)-num+1):
        if list_[idx] == "-":
            count += 1
            for idx2 in range(num):
                if list_[idx + idx2] == "-":
                    list_[idx + idx2] = "+"
                else:
                    list_[idx + idx2] = "-"
        	

    for idx3 in range(num):
        if list_[-idx3] == "-":
            return "IMPOSSIBLE"
    return count



import re
f_out = open('A_output_large.txt', 'w')
f_in = open('A-large.in', 'r')
#print f_in.readlines()
lines = [line.strip() for line in f_in.readlines()][1:]
#print (lines)
lines2 = [linee.split() for linee in lines]
#test_case=[]
#one_case=[]
for idx in range(len(lines)):

	ans = oversize(lines2[idx][0],lines2[idx][1])

	# writes an answer (in a new line) to the output file
	f_out.write("Case #{0}: {1}\n".format(idx+1, ans))

f_out.close()




#print lines

