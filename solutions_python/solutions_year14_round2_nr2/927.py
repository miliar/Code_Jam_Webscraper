def solve(a, b, k):
    count = 0
    for i in range(a):
        for j in range(b):
             if i&j < k:
                count += 1

    return count

def run(filename):
    infile = open(filename)
    outfile = open("output.txt", 'w')
    cases = int(infile.readline())
    for i in range(cases):
        l = map(int, infile.readline()[:-1].split())
        a = l[0]
        b = l[1]
        k = l[2]
        result = solve(a, b, k)
        outfile.write("Case #{0}: {1}\n".format(i + 1, result))
    infile.close()
    outfile.close()

test_file = "test.txt"
contest_file = "input.txt"

run(test_file)
try:
    run(contest_file)
except:
    print("No contest file yet")
