num_test_cases = input()
test_cases = []
for i in range(num_test_cases):
    test_cases.append(raw_input().split(" "))
num_friends_array = []
for tcase in test_cases:
    smax = tcase[0]
    s_array = list(tcase[1])
    s_array = [ int(x) for x in s_array ]
    friends = 0
    standing_members = 0
    for index in range(len(s_array)):
        if standing_members + friends >= smax:
            break
        elif index <= standing_members + friends:
            standing_members += s_array[index]
        else:
            friends += index - standing_members - friends
            standing_members += s_array[index]
            
    num_friends_array.append(friends)
for index in range(len(num_friends_array)):
    print "Case #" + str(index + 1) + ": " + str(num_friends_array[index])
    
        
                
        
        
        
        
