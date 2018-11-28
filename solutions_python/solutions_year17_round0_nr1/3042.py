T = int(input())
for case in range(T):
    S = input()
    K = S.split(" ")[1]
    S = list(S.split(" ")[0])
    count = 0
    for pancake in range(len(S)):
        if(S[pancake] == '+'):
            continue
        for neighbor in range(int(K)):
            if (pancake+neighbor >= len(S)):
                count = -1
                break
            if(S[pancake+neighbor] == '-'):
                S[pancake+neighbor] = '+'
            else:
                S[pancake+neighbor] = '-'
        if (count == -1):
            break
        count += 1

    if (count == -1):
        count = "IMPOSSIBLE"
     
    print("Case #{}: {}".format(case+1, count)) 


