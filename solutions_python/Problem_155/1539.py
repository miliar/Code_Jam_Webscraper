output = ""
file = open('in','r')
cases = int(file.readline())
for case_no in range(cases):
    people_up = 0
    people_added = 0
    line = file.readline().split()
    people = line[1]
    max_shyness = line[0]
    for shyness, count in enumerate(people):
        shyness = shyness - people_up
        if shyness > 0:
            people_added += shyness
            people_up += shyness
        people_up += int(count)
    output += "Case #{}: {}\n".format(case_no + 1, people_added)
    
    
out_file = open("out","w")
out_file.truncate(0);
out_file.write(output)