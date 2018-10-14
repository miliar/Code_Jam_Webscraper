#!/usr/bin/env python3

# Get number of tests, and increment over them
count = int(input())
for x in range(1,count+1):
    # Get input
    test_input = input().split(" ")
    max_shy = int(test_input[0])
    shy_list = list(test_input[1])

    shyness_level = 0
    audience_count = 0
    new_friends_count = 0
    for y in shy_list:
        count = int(y)

        if count > 0:
            # If we have too many shy people
            if audience_count < shyness_level:
                # Add enough to make them clap
                new_friends = shyness_level - audience_count
                audience_count += new_friends
                new_friends_count += new_friends
        audience_count += count
        shyness_level += 1

    # Answer for each case
    print ("Case #" + str(x) + ": " + str(new_friends_count))
