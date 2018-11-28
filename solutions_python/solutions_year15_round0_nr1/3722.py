input_file = open('/Users/nyuad/Desktop/codejam/1/input.txt', 'r')
output_file = open('/Users/nyuad/Desktop/codejam/1/output.txt', 'w')
cnt = 0
test_cases = int(input_file.readline()[:-1])
for line in input_file:
    cnt += 1
    input_array = line[2:-1]
    people_standing = 0
    friends_required = 0
    for i in xrange(0,len(input_array)):
        if i <= people_standing:
            people_standing +=  int(input_array[i])
        elif int(input_array[i]) > 0:
            temp_friends = i - people_standing
            friends_required += temp_friends
            people_standing +=  temp_friends + int(input_array[i])

    if cnt == test_cases:
        output_file.write('Case #'+ str(cnt) + ': '+ str(friends_required))
    else:
        output_file.write('Case #'+ str(cnt) + ': '+ str(friends_required) + '\n')
        
input_file.close()
output_file.close()
