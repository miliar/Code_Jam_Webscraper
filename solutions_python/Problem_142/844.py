t = int(input())

for i in range(1, t + 1):
    s = []
    N = int(input())

    for j in range(N):
        s.append(input())

    for j in range(N):
        temp = list(s[j])
        k = 0
        length = len(temp)
        while k < length - 1 :
            if(temp[k][0] == temp[k+1][0]):
                temp[k] = temp[k] + temp[k+1]
                temp.pop(k+1)
                length -= 1
                k -= 1
            k += 1
        s[j] = temp

    temp = s[0]
    indices = range(len(temp))
    max_steps = [0 for x in indices]
    min_steps = [100000 for x in indices]
    flag = True
    for j in s:
        if len(temp) == len(j):
            for k in indices:
                if j[k][0] != temp[k][0]:
                    flag = False
                    break
                max_steps[k] = max(len(j[k]), max_steps[k])
                min_steps[k] = min(len(j[k]), min_steps[k])
        else:
            flag = False
            break
    if flag:
        print("Case #" + str(i) + ":", sum(max_steps) - sum(min_steps))
    else:
        print("Case #" + str(i) + ": Fegla Won")
