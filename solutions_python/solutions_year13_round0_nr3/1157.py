FILE_IN = "C-small-attempt0.in"
FILE_OUT = "C-small-attempt0.out"
NEWLINE = '\n'
import math

def is_palindrom(num):
    s = str(num)
    l = list(s)
    l.reverse()
    s1 = "".join(l)
    reversed_num = int(s1)
    return num == reversed_num

if __name__ == '__main__':
    f = open(FILE_IN, "r")
    f_out = open(FILE_OUT, "w")
    lines = f.readlines()
    num_of_cases = int(lines[0])

    lines_out = []
    for i,line in enumerate(lines[1:]):
        l = line.strip().split(" ")
        tmp = [int(k) for k in l]
        A = tmp[0]
        B = tmp[1]
        A_sqrt = int(math.sqrt(A) // 1)
        B_sqrt = int(math.sqrt(B) // 1)
        count = 0
        for j in range(A_sqrt,B_sqrt+1):
            y = j**2
            if y < A or y > B:
                continue
            if is_palindrom(y) and is_palindrom(j):
                count += 1
        result = "Case #%d: " % (i+1) + str(count) + NEWLINE
        lines_out.append(result)     
    
    f_out.writelines(lines_out)
    f.close()
    f_out.close()
    print 'done.'
