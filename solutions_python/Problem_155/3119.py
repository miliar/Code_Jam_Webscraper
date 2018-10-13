
infile = "A-large.in"


with open(infile, "r") as ins:
    array = []
    first = False
    case = 1
    for line in ins:
    	if (not first): 
    		first = True
    		continue
        line = line.replace('\n', '')
        max_shy = line.split(' ')[0]
        shy_arr = line.split(' ')[1]
        shy_count = 0
        total_count = 0
        shy_level = 0
        for shy in shy_arr: 
        	if shy_level > total_count + shy_count:
        		shy_count += shy_level - (total_count + shy_count)
    		total_count += int(shy)
    		shy_level += 1
        print 'Case #' + str(case) + ': ' + str(shy_count)
        case += 1
        





