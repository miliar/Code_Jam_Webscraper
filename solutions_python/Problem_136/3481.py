import sys, itertools

input_file_name = 'input2.in'
output_file_name = 'output2.out'

f_in = open(input_file_name,'r')
f_out = open(output_file_name,'w')

contents = f_in.readlines()
num_cases = int(contents.pop(0))
for case in range (num_cases):
    line = contents.pop(0)
    nums = line.split()
    C,F,X = [float(elem) for elem in nums]

    prevtime = 0
    farms = 0
    while 1:
        rate = 2.0
        buildtime = 0
        for i in range(farms):
            buildtime = buildtime + (C/rate)
            rate = rate + F
        time = buildtime + X/rate
        if (farms > 0) and (prevtime < time):
            break
        else:
            prevtime = time
            farms = farms + 1
    answer = round(prevtime,7)
    print('Case #{}: {}'.format(case+1, answer), file = f_out)
  
f_in.close()
f_out.close()
