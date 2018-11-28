T = int(input())

for _ in range(T):
    s_max, num = input().split()

    s_max = int(s_max)
    num = [int(char) for char in num]

    cur_num = num[0]
    cur_friends = 0

    for i in range(1, s_max + 1):
        if cur_num < i:
            cur_friends += i - cur_num
            cur_num = i
        cur_num += num[i]

    print("Case #" + str(_ + 1) + ": " + str(cur_friends))
