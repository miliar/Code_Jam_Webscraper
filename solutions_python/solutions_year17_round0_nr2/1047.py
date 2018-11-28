def check_tidy(num):
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i+1]):
            return False
    return True

def solve(num):

    if check_tidy(num):
        return int(num)
    else:
        return 9 + (solve(str(int(num[:-1]) - 1))) * 10

with open("B-large.in") as f:
    i = 1
    with open("B-large.out", "w") as w:
        f.readline()
        for line in f:
            answer = solve(line.strip())
            print("Case #{0}: {1}".format(i, answer))
            w.write("Case #{0}: {1}\n".format(i, answer))
            i += 1