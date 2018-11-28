# Google Codejam 2012
# Qualification Round
# Nivvedan S

INPUT_FILE_NAME="p3.in"
OUTPUT_FILE_NAME="p3.out"
IN = open(INPUT_FILE_NAME, "r")
OUT = open(OUTPUT_FILE_NAME, "w")

lines=IN.readlines()

T=int(lines[0].strip())
lines=lines[1:]

count = 1

def is_valid(test, org, A, B):
    if (test >= A) and (test<= B) and (test > org):
        return True
    else:
        return False

for line in lines:
    line = line.strip()
    A = int(line.split()[0])
    B = int(line.split()[1])

    ans = 0
    for cand in range(A, B+1):
        cand_string = str(cand)
        if (not(cand_string[0] == '0')):
            done = []
            for i in range(0, len(cand_string)-1):
                test_string = cand_string[i+1:] + cand_string[0:i+1]
                ## print cand_string, "  ", test_string
                if (not(test_string[0] == '0')):
                    test = int(test_string)
                    if test not in done:
                        done.append(test)
                        if is_valid(test, cand, A, B):
                            ## print ans
                            ## print "(" , cand, ",", test, ")"
                            ans = ans + 1

    print "Case #"+str(count)+": "+str(ans)
    count = count + 1
