test_cases = int(raw_input())

for i in range(test_cases):
    get_input = raw_input().split(" ")
    pancakes = list(get_input[0])
    k = int(get_input[1])
    left_point = 0
    count = 0
    while left_point <= len(pancakes)-k:
        if pancakes[left_point] == "+":
            left_point += 1
        else:
            for index in range(left_point, left_point + k):
                if pancakes[index] == "+":
                    pancakes[index] = "-"
                else:
                    pancakes[index] = "+"
            count += 1
    print "Case #" + str(i+1) + ": ",
    if "-" not in pancakes:
        print str(count)
    else:
        print "IMPOSSIBLE"
