num = int(input().strip())

for i in range(num):
    guess1 = int(input().strip()) - 1

    row1 = []
    for x in range(4):
        if x != guess1:
            input()
            continue
        row = input().split()
        row1 = [int(x) for x in row]
        

    guess2 = int(input().strip()) - 1

    row2 = []
    for x in range(4):
        if x != guess2:
            input()
            continue
        row = input().split()
        row2 = [int(x) for x in row]

    choices = [x for x in row1 if x in row2]
    if len(choices) == 0:
        print("Case #{}: Volunteer cheated!".format(i+1))
    elif len(choices) > 1:
        print("Case #{}: Bad magician!".format(i+1))
    else:
        print("Case #{}: {}".format(i+1, choices[0]))
