def clap_all_audiance(shy):
    add = 0
    sum_p = shy[0]
    for i in xrange(1,len(shy)):
        if (shy[i] > 0) and (i > sum_p):
            #print "At level {} just {} have clapped, adding {}".format(i, sum_p, (i-sum_p))
            add = add + (i-sum_p)
            sum_p = i
        sum_p = sum_p + shy[i]
    return add

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

test_cases = input_file.readline()
for nline,line in enumerate(input_file):
    max_shy = int(line.split()[0])
    shy = map(int, [i for i in line.split()[1]])
    output_file.write("Case #{}: {}\n".format(nline+1, clap_all_audiance(shy)))

output_file.close()

