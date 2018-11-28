t, s_max = 0, 0

t = eval(input())

if t > 0 and t <= 100:

    for i in range(0, t):
        dataset = input()
        s_max, audiance = dataset.split(" ")

        s_max, audiance = int(s_max), str(audiance)

        total = int(audiance[0])
        missing = 0

        if s_max >= 0 and s_max <= 1000:

            for j in range(1, s_max+1):
                if j <= total:
                    total += int(audiance[j])
                else:
                    if abs(total - j) > missing:
                        missing = abs(total - j)
                    total += int(audiance[j])

        print("Case #"+str(i+1)+": "+str(missing))
