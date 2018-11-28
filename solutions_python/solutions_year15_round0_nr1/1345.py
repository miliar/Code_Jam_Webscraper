filename = "standingovation.in"



f = open(filename, "r")
num_test_cases = int(f.readline().strip())

# each test case
for test_case in range(1, num_test_cases + 1):
    line = f.readline().split(" ")
    values = line[1].strip()

    level = 0
    cumulative_people = 0
    added_people = 0
    for num_persons in values:
        num_persons = int(num_persons)
        if level > cumulative_people:
            added_people = max(added_people, level - cumulative_people)
        cumulative_people += num_persons
        level += 1

    print("Case #{}: {}".format(test_case, added_people))
