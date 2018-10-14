T = int(input())

for i in range(1, T+1):
    first_answer = int(input())
    first_row = []
    for r in range(1, 5):
        z = input()
        if r == first_answer:
            first_row = z.split(' ')

    second_answer = int(input())
    second_row = []
    for r in range(1, 5):
        z = input()
        if r == second_answer:
            second_row = z.split(' ')

    answer = list(set(first_row) & set(second_row))

    if len(answer) == 0:
        print("Case #" + str(i) + ": Volunteer cheated!")
    elif len(answer) == 1:
        print("Case #" + str(i) + ": " + answer[0])
    else:
        print("Case #" + str(i) + ": Bad magician!")




