import sys

map = {}
def main():
    inp = open(sys.argv[1], "r")
    out = open(sys.argv[2], "w")

    T = int(inp.readline())

    if not T:
        return

    for j in xrange(T):
        count = 0
        IN_STRING = inp.readline().strip()
        OUT_STRING = "Case #" + str(j + 1) + ": "
        arr = IN_STRING.split(" ")
        size = len(arr[0])
        A = int(arr[0])
        B = int(arr[1])
        for i in xrange(A, B + 1):
            num = i
            rec = num
            map[num] = {}
            for j in xrange(size - 1):
                rec = ((rec % 10) * pow(10, size - 1) + rec/10)
                if (rec > num and rec <= B and rec not in map[num]):
                    map[num][rec] = True
                    count += 1
        out.write(OUT_STRING + str(count))
        if j < T -1:
            out.write("\n")

if __name__ == "__main__":
    main()
