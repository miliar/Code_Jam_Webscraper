def friends(shyness):
    num_friends = 0
    people_standing = 0
    index = 0
    for n in shyness:
        additional_friends = max(index - people_standing, 0)
        num_friends += additional_friends
        people_standing += n + additional_friends
        index += 1
    
    return num_friends

for T in range(int(raw_input())):
	shyness = [int(n) for n in raw_input().split(' ')[1]]
	print "Case #%d: %d" % (T+1, friends(shyness))