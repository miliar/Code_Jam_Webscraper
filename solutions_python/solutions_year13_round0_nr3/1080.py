#!/user/bin/python
import math

def check_pal(num):
    string = str(num)
    if string == string[::-1]:
        return 1

def check_one_test(fo) :
    n_m = fo.readline().strip().split()
    #print n_m
    count = 0
    for i in range(int(n_m[0]), int(n_m[1]) + 1):
        if check_pal(i):
            sq = math.sqrt(i)
            if sq == int(sq):
                if check_pal(int(sq)):
                    count = count + 1
    return count

fo = open("input", "r")
fw = open("output", "w")
no_of_cases = int(fo.readline().strip())
#print no_of_cases
count = 1
while no_of_cases:
    ret = ''
    string = ''
    ret = check_one_test(fo)
    #print ret
    fw.write("Case #" + str(count) + ": " + str(ret) + "\n")
    no_of_cases =  no_of_cases - 1
    count = count + 1

fo.close
fw.close