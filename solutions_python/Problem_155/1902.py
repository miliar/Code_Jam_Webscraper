def min_friends(audience): 
    cumulative_people = 0
    num_friends = 0
    for i, num_people in enumerate(audience): 
        if num_people > 0: 
            if i > cumulative_people + num_friends: 
               num_friends += i-cumulative_people
            cumulative_people += num_people
    return num_friends
    
if __name__ == '__main__': 
    num_tests = int(raw_input())
    for i in range(num_tests): 
        _, audience_str = raw_input().strip().split()
        audience = []
        for num_people in audience_str: 
            audience.append(int(num_people))
        print('Case #%d: %d' % (i+1, min_friends(audience)))