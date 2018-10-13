T = int(input())
for test_case in range(1, T+1):
    guess_1 = int(input())
    grid_1 = [[x for x in map(int, input().split())] for _ in range(4)]
    guess_2 = int(input())
    grid_2 = [[x for x in map(int, input().split())] for _ in range(4)]

    possible_guess = [x for x in grid_1[guess_1-1]
                                if x in grid_2[guess_2-1]]
    if len(possible_guess) == 0:
        ans = "Volunteer cheated!"
    elif len(possible_guess) == 1:
        ans = possible_guess[0]
    else:
        ans = "Bad magician!"
    print("Case #{}: {}".format(test_case, ans))

