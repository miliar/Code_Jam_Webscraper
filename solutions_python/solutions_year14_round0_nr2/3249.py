from sys import argv
with open(argv[1], "r") as f:
    cases = int(f.readline())
    for i in range(cases):
        l = f.readline().split()
        c_val = float(l[0])
        f_val = float(l[1])
        x_val = float(l[2])
        current_rate = 2.0
        time_spent = 0.0

        while True:
            if c_val / current_rate + x_val / (current_rate + f_val) < x_val / current_rate:
                time_spent += c_val / current_rate
                current_rate += f_val
            else:
                time_spent += x_val / current_rate
                break

        print("Case #%d: %f" % (i + 1, time_spent))


