for test in range(int(input())):
    rows = [None, None]
    for i in [0,1]:
        ans = int(input())
        for row in range(4):
            line = input()
            if row+1 == ans:
                rows[i] = set(line.split())
    intersection = rows[0] & rows[1]
    num = len(intersection)
    if num == 0:
        res = "Volunteer cheated!"
    elif num == 1:
        res = list(intersection)[0]
    else:
        res = "Bad magician!"
    print("Case #" + str(test+1) + ": " + res)
        
