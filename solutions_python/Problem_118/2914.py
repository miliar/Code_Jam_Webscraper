import math
def check_palindrome(n):
    l = len(n)
    for i in range(l/2):
        if (n[i] != n[l-i-1]):
            return 0
    return 1

f = open("C-small-attempt0.in", "r")
out = open("C-small.out", "w")

count = 0
for line in f:
    if count == 0:
        T = int(line)
    else :
        line = line.split()
        A = int(line[0])
        B = int(line[1])
        num_f_and_s = 0
        list_n = range(A,B+1)
        for num in list_n:
            if (check_palindrome(str(num))):
                sqr_rt = math.sqrt(num)
                if sqr_rt == int(sqr_rt):
                    if check_palindrome(str(int(sqr_rt))):
                        num_f_and_s += 1
        out.write("Case #"+ str(count)+": "+ str(num_f_and_s)+"\n")
    count += 1
                                           
f.close()
out.close()
