input = open("in.in", 'r')
lines = input.readlines()
lines = [line.replace('\n', '') for line in lines]

out = open("output.txt", 'w+')

no_of_cases = int(lines[0])
start_line = 1
line_increment = 1
end_line = line_increment + 1

for case_no in xrange(1, no_of_cases + 1):
    case = lines[case_no]
    s_max = case.split(' ')[0]
    s = case.split(' ')[1]
    total = 0
    add = 0
    people = list(s)
    for num in xrange(0, len(people)):
        si = people[num]
        total += int(si)
        if total < num + 1:
            add += num + 1 - total
            total = num+1
	start_line = end_line
	end_line += line_increment
    print "Case #" + str(case_no)  + ": " + str(add) + '\n'
    out.write("Case #" + str(case_no)  + ": " + str(add) + "\n")