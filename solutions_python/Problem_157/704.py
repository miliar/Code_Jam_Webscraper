__author__ = 'pcjjman'
test = False
test_input = \
"""6
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i
27 1
iiiiiiiiijjjjjjjjjkkkkkkkkk"""
test_output = \
"""Case #1: NO
Case #2: YES
Case #3: NO
Case #4: YES
Case #5: NO"""
conversion_map = {"1": 0, "i": 1, "j": 2, "k": 3}
#multiply array
ma = [[0, 1, 2, 3], [1, 0, 3, 2], [2, 3, 0, 1], [3, 2, 1, 0]]
#negative array
na = [[False, False, False, False], [False, True, False, True], [False, True, True, False], [False, False, True, True]]
def multiply(value1, value2, negative):
    output_value = ma[value1][value2]
    negative = ((na[value1][value2] == True and not negative) or (na[value1][value2] == False and negative))
    return output_value, negative

def find_i(values):
    #returns the new string starting with i if it completes, None if it fails.
    start = True
    negative = False
    while (start or negative or (values[0] != 1)) and len(values) > 3:
        new_letter, negative = multiply(values[0], values[1], negative)
        values = values[1:]
        values[0] = new_letter
        start = False
    if len(values) < 3:
        return None
    return values

def find_k(values):
    #we start from the end and make our way left until we find a k, otherwise we return a -1
    start = True
    negative = False
    while (start or negative or (values[-1] != 3)) and len(values) > 3:
        new_letter, negative = multiply(values[-2], values[-1], negative)
        values = values[:-1]
        values[-1] = new_letter
        start = False
    if len(values) < 3:
        return None
    return values

def validate_j(values):
    #returns true if the set of letters collapse down to a j, False otherwise
    negative = False
    last_letter = values[0]
    for letter in values[1:]:
        last_letter, negative = multiply(last_letter, letter, negative)
    if not negative and last_letter == 2:
        return True
    else:
        return False


if not test:
    num_cases = int(raw_input(""))
    #print "Saw {} cases".format(num_cases)
    text_input = ""
    cases = []
    for _ in range(num_cases):
        cases.append(raw_input("") + "\n" + raw_input(""))
    #print cases
else:
    cases = []
    num_cases = int(test_input.split('\n')[0])
    for i in range(num_cases):
        cases.append(test_input.split('\n')[i * 2 + 1] + "\n" + test_input.split('\n')[i * 2 + 2])

current_case = 1
for case in cases:
    found = False
    first = True
    letter_count, multiplier = case.split('\n')[0].split(' ')
    multiplier = int(multiplier)
    letters = case.split('\n')[1]
    converted = [conversion_map[x] for x in letters]
    #do some pre checks
    #if both j and k are not in the map, we'll never find the right one
    if 2 not in converted and 3 not in converted:
        found = True
    #if the length is three and
    if not found:
        converted *= multiplier
    #if it's already only three and they're not in the right order we'll never find them
    if len(converted) == 3 and converted != [1, 2, 3]:
        found = True
    success = False
    if converted == [1, 2, 3]:
        found = True
        success = True
    while not found:
        #first we need to find our i, if one is available
        if not first or converted[0] != 1:
            converted = find_i(converted)
            if converted is None:
                found = True
                break
        #next we need to find a valid z
        if not first or converted[-1] != 3:
            converted = find_k(converted)
            if converted is None:
                found = True
                break
        if len(converted) <= 3:
            found = True
            break
        if validate_j(converted[1:-1]):
            success = True
            found = True
        first = False
    if success:
        print "Case #{}: YES".format(current_case)
    else:
        print "Case #{}: NO".format(current_case)
    current_case += 1