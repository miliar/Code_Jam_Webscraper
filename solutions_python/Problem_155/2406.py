__author__ = 'dfisher'

# shyness level Si waits until at least S other audience members have already stood to clap.
# If Si = 0, then that audience member will always stand and clap immediately.
# e.g. Si = 2, will clap if at least two others are standing and clapping

# what is the minimum number of friends needed to guarantee a standing ovation?

# s_max = maximum level of shyness
# string of s_max + 1 digits.  kth digit represents number of people in audience with shyness k.
# 409 means 4 members with Si=0, 0 with Si=1, and 9 with Si=2
# There will always be between 0 and 9 people with each shyness level.
# String never ends with 0.  There will always be at least one person in the audience.

# filename = "standing_ovation_input.txt"
# filename = "A-small-attempt0.in"
filename = "A-large.in"
inputFile = open(filename, "r")
lines = []
for line in inputFile:
    lines.append( line.strip() )
    
inputFile.close()

numCases = int(lines[0])
# print 'numCases = ', numCases
line_number = 1
for i in range(numCases):
    case_str = "Case #" + str(i+1) + ":"
    
    line = lines[line_number]
    values = line.split()
    s_max = (int)(values[0])
    audience = values[1]
    
    audience_size = 0
    count = len(audience)
    for n in range(count):
        audience_size += int(audience[n])
        
    # print 'audience_size', audience_size
    index = 0
    standing_count = 0
    added_count = 0
    while (index < count):
        value = int(audience[index])        
        standing_count += value
        # print index, ': value, standing_count', value, standing_count
        need = index+1
        if (standing_count < need): 
            diff = need - standing_count
            # print "adding ", diff
            added_count += diff
            standing_count += diff
        index += 1
    
    print case_str, added_count
    line_number+=1
    






