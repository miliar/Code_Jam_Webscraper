c = int(input())
T = c

while T:
    T -= 1
    line = input()
    N, K = line.split(" ")
    N = int(N)
    K = int(K)

    spaces = {N: 1}
    spaces_key = {N}
    for i in range(K):
        space = max(spaces_key)

        spaces[space] -= 1
        if spaces[space] == 0:
            spaces_key.remove(space)

        if (space == 1):
            ans1 = 0
            ans2 = 0
        elif (space % 2):
            left_space = space // 2
            if (left_space in spaces.keys()):
                spaces[left_space] += 2
            else:
                spaces[left_space] = 2
            spaces_key.add(left_space)
            ans1 = int(left_space)
            ans2 = int(left_space)
        else:
            left_space = space / 2

            if (left_space in spaces.keys()):
                spaces[left_space] += 1
            else:
                spaces[left_space] = 1

            if ( (left_space - 1) in spaces.keys()):
                spaces[left_space - 1] += 1
            else:
                spaces[left_space - 1] = 1
            spaces_key.add(left_space)
            spaces_key.add(left_space - 1)
            ans1 = int(left_space)
            ans2 = int(left_space - 1)

    print("Case #" + str(c-T) + ": " + str(ans1) + " " + str(ans2))