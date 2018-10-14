import sys

def rotate(string):
    return string[-1] + string[:-1]

f = open(sys.argv[1], 'r')
lines = f.readlines()[1:]
f.close()

case = 1
for line in lines:
    low = line.split()[0]
    hi = line.split()[1]

    pairs = 0
    for i in range(int(low), int(hi) + 1):
        working_with = str(i)
        working_with_new = working_with
        for j in range(len(low) - 1):
            working_with_new = rotate(working_with_new)
            if working_with_new == working_with:
                break;
            if int(low) <= int(working_with) < int(working_with_new) <= int(hi):
                pairs += 1
    print 'Case #' + str(case) + ': ' + str(pairs)
    case += 1
