BASE_RATE = 2

def test(C_cookies, F_rate, X_target):
    min_time = X_target / BASE_RATE
    times = []
    current_time = 0
    current_rate = BASE_RATE
    updated = True
    while updated:
        updated = False
        current_time += C_cookies / current_rate
        current_rate += F_rate
        new_time = current_time + X_target / current_rate
        if new_time < min_time:
            min_time = new_time
            updated = True
    return str(round(min_time, 7))

with open('B.in') as f:
    with open('B.out', 'w') as f2:
        lines = f.readlines()
        lines = [[float(item) for item in line.split(" ")] for line in lines[1:]]
        for i in range(len(lines)):
            result = "Case #" + str(i+1) + ": " + test(*lines[i])
            print(result)
            f2.write(str(result) + "\n")
