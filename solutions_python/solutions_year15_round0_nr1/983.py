__author__ = 'pcjjman'
test = False
test_input = \
"""4
4 11111
1 09
5 110011
0 1
19 00000000003000000005"""
test_output = \
"""Case #1: 0
Case #2: 1
Case #3: 2
Case #4: 0
Case #5: 16"""

text_input = ""
if not test:
    num_cases = int(raw_input(""))
    #print "Saw {} cases".format(num_cases)
    text_input = ""
    cases = []
    for _ in range(num_cases):
        cases.append(raw_input(""))
    #print cases
else:
    text_input = test_input

output = ""
case_number = 1
for case in cases:
    s_max, audience = case.split(' ')
    s_max = int(s_max)
    # Now we need to count the number of audience numbers we need to hit the magic value
    # Simple brute force. Let's increase the number of people until we get everyone standing
    audience_required = 0
    people_standing = 0
    for i in range(s_max + 1):
        #now we check to see if everyone is standing
        people_in_level = int(audience[i])
        if people_in_level == 0:
            continue
        if people_standing < i:
            audience_required += i - people_standing
            people_standing = i
        people_standing += int(people_in_level)
    case_output = "Case #{}: {}".format(case_number, audience_required)
    case_number += 1
    output += case_output + "\n"
    print case_output

#now that we're complete assert that everything is correct
if test:
    assert output.strip() == test_output.strip()