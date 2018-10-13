num = int(input().strip())

for i in range(num):
    args = input().split()
    c, f, x = [float(a) for a in args]

    rate = 2.0
    time = x / rate
    total_time = 0

    new_time = c / rate + x / (rate + f)

    while (new_time < time):
        total_time = total_time + c / rate
        rate = rate + f

        time = new_time
        new_time = total_time + c / rate + x / (rate + f)

    total_time = total_time + x / rate
    print("Case #{}: {:.7f}".format(i+1, total_time))
