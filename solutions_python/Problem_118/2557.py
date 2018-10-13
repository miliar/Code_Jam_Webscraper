import math

def is_palindrone(num):
    n = str(num)
    pos = len(n) - 1
    i = 0
    while i < pos:
        if n[i] != n[pos]:
            return False
        i = i + 1
        pos = pos - 1
    return True


def find_fair_squares(low, high):
    original_high = high
    count = 0
    low = math.ceil(math.sqrt(low))
    high = math.ceil(math.sqrt(high))
    while(low <= high):
        square = low * low
        if square > original_high:
            return count
        if is_palindrone(square) and is_palindrone(low):
            count = count + 1
        low = low + 1
    return count

def main():
    f = open("t.txt", 'r')
    output = open("output.txt", 'w')
    lines = f.readlines()
    count = int(lines[0])
    line = 1
    while line <= count:
        low, high = lines[line].strip().split()
        low = int(low)
        high = int(high)
        result = find_fair_squares(low, high)
        output.write("Case #%d: %d\n" % (line, result))
        line = line + 1
    f.close()
    output.close()

if __name__ == "__main__":
    main()




