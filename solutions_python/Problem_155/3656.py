__author__ = 'gsvic'

input_file = open("input")
output_file = open("output", "w+")

num_cases = int(input_file.readline())
test_cases = []
for case in input_file:
    tmp = case.split()
    new_case = dict()
    new_case['max_shyness'] = int(tmp[0])
    new_case['audience'] = [int(i) for i in tmp[1]]
    test_cases.append(new_case)

for index, tc in enumerate(test_cases):
    needed = 0
    total = 0
    for s, p in enumerate(tc['audience']):
        if p != 0:
            if s > total:
                print "S: %d, TOTAL: %d"%(s,total)
                needed += s - total
                total += needed
        total += p

    output = "Case #%d: %d\n" % (index+1, needed)
    output_file.write(output)
output_file.close()