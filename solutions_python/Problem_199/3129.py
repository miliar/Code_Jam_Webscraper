x = int(input())
for i in range(x):
    case = input()
    cake = ""
    done = False
    k = 0
    pancakes = []
    for j in range(len(case)):
        if not done:
            if case[j] != " ":
                cake += case[j]
            else:
                done = True
                k = int(case[j+1:])
                break
    for j in range(len(cake)):
        if cake[j] == '+':
            pancakes.append(True)
        else:
            pancakes.append(False)
    count = 0
    zeros = 0
    while True:
        try:
            zeros = pancakes.index(0)
        except:
            print("Case #" + str(i+1) + ": " + str(count))
            break
        if zeros + k > len(pancakes):
            print("Case #" + str(i+1) + ": " + "IMPOSSIBLE")
            break
        else:
            for p in range(zeros, zeros+k):
                pancakes[p] = not pancakes[p]
            count += 1




            
