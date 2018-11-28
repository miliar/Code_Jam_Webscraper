import sys
in_file = sys.argv[1]
f = open(in_file, 'r')
input_array,output_array = [],[]
for line in f:
    input_array += [line.rstrip()]
input_array = input_array[1::]
def count_successes(case):
    case = case.split(' ')
    surprises = int(case[1])
    p = int(case[2])
    scores = case[3:]
    count = 0
    for i in scores:
        if p > int(i): pass
        elif int(i) > 3*p-3:
            count += 1
        elif int(i) >= 3*p-4 and surprises > 0:
            count += 1
            surprises -= 1
    return str(count)
for case in input_array:
    output_array += ['Case #'+str(len(output_array)+1)+': '+count_successes(case)]
for line in output_array:
    print line
