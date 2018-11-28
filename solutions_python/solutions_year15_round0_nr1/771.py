import sys
case_count = int(sys.stdin.readline())
for i in range(case_count):
    
    
    max_shy_level, shy_level_sequence = sys.stdin.readline().split()
    standup_count = 0
    required_people_sum = 0 
    for shy_level, people_count in enumerate(shy_level_sequence):
        
        shy_level = shy_level # start with shy_level 0
        people_count = int(people_count)
        
        if people_count == 0:
            continue

        if shy_level == 0 or shy_level <= standup_count:
            standup_count += people_count

        else:
            required_people = shy_level - standup_count
            required_people_sum += required_people
            standup_count += required_people + people_count
            

    print "Case #%d: %d" % (i+1, required_people_sum)

