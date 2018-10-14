def reverse_no(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

def solve(case_id, A, B, first_try, out):
    c = 0
    n = first_try
    while True:
        sq = n**2
        if sq < A:
            n+=1
        else:
            if sq > B:
                out.write("Case #" + str(case_id) + ": " + str(c) + "\n")           
                break
            else:
                #verify if palindrome:
                if n == reverse_no(n) and sq == reverse_no(sq):
                    c+=1
                n+=1

input_file = 'C-small-attempt1.in'
output_file = 'output.txt'

f = open(input_file, 'r')
out = open(output_file, 'w')

#read no test cases:
no_tests = int(f.readline())

for test in range(0, no_tests):
    line = f.readline()
    l = line.split()
    A = int(l[0])
    B = int(l[1])
    no_dig = len(l[0])
    first_try = 10**((no_dig - 1) / 2)

    solve(test+1, A, B, first_try,out)
    
f.close()
out.close()
