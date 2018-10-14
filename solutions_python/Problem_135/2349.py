import sys
if len(sys.argv) < 2:
    exit()
lines = [line.strip() for line in open(sys.argv[1])]

f = open('magictrickoutput.txt', 'w')

T = int(lines.pop(0))

for x in range(T):
    start = 10 * x
    q1 = int(lines[start])
    first_arr = lines[start+1:start+5]
    q2 = int(lines[start+5])
    second_arr = lines[start+6:start+10]

    first_poss = list(map(int, first_arr[q1 - 1].split()))
    second_poss = list(map(int, second_arr[q2 - 1].split()))

    answers = [num for num in first_poss if num in second_poss]

    if len(answers) == 1:
        f.write("Case #{0}: {1}\n".format(x + 1, answers[0]))
    elif len(answers) > 1:
        f.write("Case #{0}: Bad magician!\n".format(x + 1))
    else:
        f.write("Case #{0}: Volunteer cheated!\n".format(x + 1))

exit()

