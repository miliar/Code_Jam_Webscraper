from sys import argv

def find(num, people):
    if people == 1:
        return (num//2, (num-1)//2)
    elif people % 2 == 0:
        return find(num//2, people//2)
    else:
        return find((num-1)//2, people//2)

def write_cases(func, filename):
    with open(filename) as fi, open(filename.split(".")[0] + ".out", "w") as fo:
        for i in range(1, int(fi.readline().strip())+1):
            line = fi.readline().strip()
            x, y = func(*map(int, line.split()))
            print("Case #{}: {} {}".format(i, x, y), file=fo)

def print_cases(func, filename):
    with open(filename) as fi:
        for i in range(1, int(fi.readline().strip())+1):
            line = fi.readline().strip()
            line = " ".join(func(*map(int, line.split())))
            print("{} -> {}".format(line, line))

if __name__ == "__main__":
    write_cases(find, argv[1])


