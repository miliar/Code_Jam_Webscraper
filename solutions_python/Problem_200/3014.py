n = int(input())
for b in range(n):
    freq = 0

    count = 0
    no = input()

    no = list(no)
    no = [int(x) for x in no]

    for i in range(len(no) - 1):
        if no[i] < no[i+1]:
            freq = 0

        elif no[i] > no[i + 1]:
            if freq == 0:
                freq = 0
                no[i] -= 1
                for j in range(i + 1, len(no)):
                    no[j] = 9
            else:
                no[i - freq] -=1
                for m in range(i - freq + 1, len(no)):
                    no[m] = 9
                freq = 0
                break;
                i+=1
        elif no[i] == no[i + 1]:
            freq += 1

    print("Case #{}: {}".format(b + 1, int(''.join(map(str, no)))))
