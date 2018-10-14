import sys

fnamein = sys.argv[1]
fnameout = sys.argv[2]

fid = open(fnamein, 'r')
fout = open(fnameout, 'w')

T = int(fid.readline())  # number of test cases


def check_line(line):
    if len(line) == 1:
        return True
    else:
        for n in range(1, len(line)):
            if int(line[n - 1]) > int(line[n]):
                return False
        return True


def process_line(line):

    if len(line) == 1:
        output = line

    elif len(line) == 2:
        v1 = int(line[0])
        v2 = int(line[1])
        if v1 > v2:
            v1 -= 1
            v2 = 9
            if v1 <= 0:
                output = str(v2)
            else:
                output = str(v1) + str(v2)
        else:
            output = line

    else:
        output = ''
        for n in range(1, len(line)):
            v1 = int(line[n - 1])
            v2 = int(line[n])

            if v1 > v2:
                v1 -= 1
                v2 = 9

                if (n < 2) and (v1 <= 0):
                    output = '9' * (len(line) - n)
                    break

                else:
                    output += str(v1) + '9' * (len(line) - n)
                    break
            else:
                output += str(v1)

            if n == len(line) - 1:
                output += str(v2)
    return output


for case in range(T):
    line = fid.readline().rstrip('\n')
    output = process_line(line)
    check = check_line(output)
    while not check:
        output = process_line(output)
        check = check_line(output)
    fout.write("Case #%d: %s\n" % (case + 1, output))
    print(line, output, check)

# remove last newline
size = fout.tell()
fout.truncate(size - 1)

fid.close()
fout.close()
