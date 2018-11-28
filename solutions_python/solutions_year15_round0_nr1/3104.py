input_file = 'A-large.in'
output_file = 'output.txt'

f = open(input_file, 'r')
out = open(output_file, 'w')


def solve(test, smax, v):
    total_cnt = 0
    extra_friends = 0
    i = 0
    for xi in v:
        if i == 0:
            total_cnt = total_cnt + int(xi)
        else:
            if total_cnt >= i:
                total_cnt = total_cnt + int(xi)
            else:
                add = i - total_cnt
                extra_friends = extra_friends + add
                total_cnt = total_cnt + int(xi) + add
        i = i + 1
    out.write("Case #" + str(test+1) + ": " + str(extra_friends) + "\n")
        

#read no test cases:
no_tests = int(f.readline())

for test in range(0, no_tests):
    line = f.readline()
    l = line.split()
    smax = l[0]
    v = l[1]
    solve(test, smax, v)
 
f.close()
out.close()
