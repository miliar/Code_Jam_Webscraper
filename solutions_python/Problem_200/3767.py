import sys

def is_tidy(n):
    if n < 10:
        return True
    digits = [int(d) for d in str(n)]
    prev = digits[0]
    for cur in digits[1:]:
        if cur < prev:
            return False
        prev = cur
    return True

def solve(n):
    n = int(n)
    if is_tidy(n): return n

    digits = [int(d) for d in str(n)]
    prev = digits[0]
    new = []
    for i, cur in enumerate(digits[1:]):
        #print i, cur
        if cur >= prev:
            new.append(prev)
            prev = cur
        else:
            new.append(prev - 1)
            new.extend([9 for d in digits[i+1:]])
            break
    next = int("".join([str(d) for d in new]).lstrip("0"))
    return next if is_tidy(next) else solve(next)

def get_input(filename):
    with file(filename, "r") as infile:
        lines = infile.readlines()[1:]
        return [line.strip().split(" ") for line in lines]

def write_out(results):
    with file("out.txt", "w") as outfile:
        for i, line in enumerate(results):
            outfile.write("Case #{}: {}\n".format(i+1, solve(*line)))

if __name__ == '__main__':
    write_out(get_input(sys.argv[-1]))
    #print solve(111111111111111110)