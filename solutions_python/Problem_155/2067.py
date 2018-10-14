with open('A-large.in', 'r') as file:
    file_content = file.read()
    lines = file_content.split('\n')
    test_num = lines.pop(0)
    lines.pop()
    print "%s cases in total\n" %test_num

    output = open('A-small-practice.out', 'w')
    for line_num, line in enumerate(lines):
        print line_num, line
        shyest_level, dist = line.split(' ')        
        dist_list = list(dist)
        
        count1 = 0
        count2 = 0
        for index, people_num in enumerate(dist_list):
            people_num = int(people_num)
            if index > count1:
                count2 += index - count1
                count1 += index - count1
            count1 += people_num
        output.write("Case #%d: %d\n" % (int(line_num)+1, count2))
                
