


testcases = int(input())
# print(testcases)

for testcase in range(1, testcases+1):
    answer1 = int(input())
    #print(answer1)
    for i in range(1,5):
        line = input().split(" ");
        #print(line)
        if i == answer1:
            candidates = set(line)
    answer2 = int(input())
    #print(answer2)
    for i in range(1,5):
        line = input().split(" ");
        #print(line)
        if i == answer2:
            candidates = candidates & set(line)

    #print(candidates)
    if len(candidates) > 1:
        result = "Bad magician!"
    elif len(candidates) == 1:
        result = candidates.pop()
    else:
        result = "Volunteer cheated!"

    print("Case #{}: {}".format(testcase, result))

