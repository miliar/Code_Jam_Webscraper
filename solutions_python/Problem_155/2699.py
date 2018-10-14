def friends_to_invite(string_input):
    list_input = string_input.split(' ')
    s_max = int(list_input[0])
    s = list_input[1].rstrip('\n')
    
    friends_req = 0
    standing_up = 0
    
    if len(s) <= 1:
        if s[0] >= 1:
            return 0
        else:
            return 1
        
    for i in range(len(s)):
        if int(s[i]) == 0:
            continue
        if i <= standing_up:
            standing_up += int(s[i])
        else:
            temp = i - standing_up
            friends_req += temp
            standing_up += temp + int(s[i])
            
    return friends_req

input_file = open('A-large.in')
output_file = open('output11.out', 'w')
i = 0
for line in input_file:
    if i == 0:
        i += 1
        continue
    friends = friends_to_invite(line)
    output_file.write('Case #%d: %d\n' % (i, friends))
    i += 1

print "done"