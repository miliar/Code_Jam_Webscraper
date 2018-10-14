import sys

def parse(filename):
    cases = []
    with open(filename) as fp:
        line = fp.readline().strip()
        nr_cases = int(line)
        nr_strings = int(fp.readline())
        while True:
            strings = []
            for i in range(nr_strings):
                strings.append(fp.readline().strip())
            cases.append(strings)
            try:
                nr_strings = int(fp.readline())
            except:
                break
    assert nr_cases == len(cases)
    return cases

def run(cases):
    output = ''

    for k, case in enumerate(cases):
        print k, case
        fegla_won = False
        nr_actions = []
        for i in range(len(case)):
            for j in range(i):
                # if case[i] == case[j]:
                #     nr_actions.append(0)
                #     continue
                # if len(set(case[i]) ^ set(case[j])) > 0:
                #     fegla_won = True
                #     break

                # reduce both strings
                s1_new = ''
                last_l = None
                for l in case[i]:
                    if l != last_l:
                        s1_new += l
                    last_l = l

                s2_new = ''
                last_l = None
                for l in case[j]:
                    if l != last_l:
                        s2_new += l
                    last_l = l

                print len(case[i])
                print len(case[j])
                print s1_new
                print s2_new
                if s1_new != s2_new:
                    fegla_won = True
                    print "fegla won"
                    break

                idx1 = 0
                idx2 = 0
                count = 0
                while True:
                    if idx1 == len(case[i]) or idx2 == len(case[j]):
                        print "Finished", count
                        print idx1 - len(case[i])
                        count += len(case[i]) - idx1
                        count += len(case[j]) - idx2
                        break
                    if case[i][idx1] == case[j][idx2]:
                        idx1 += 1
                        idx2 += 1
                    else:
                        count += 1
                        if case[i][idx1] == case[i][idx1 - 1]:
                            idx1 += 1
                        elif case[j][idx2] == case[j][idx2 - 1]:
                            idx2 += 1
                        else:
                            print "???"

                # print abs(len(case[i]) - len(case[j]))
                # print "count", s1_count + s2_count
                nr_actions.append(count)
                print nr_actions[-1]

            if fegla_won:
                break

        if fegla_won:
            output += "Case #%d: Fegla Won\n" % (k+1)
        else:
            output += "Case #%d: %d\n" % (k+1, min(nr_actions))
    return output

if __name__ == '__main__':
    fn = sys.argv[1]
    out = fn + ".out"

    cases = parse(fn)

    output = run(cases)

    with open(out, 'w') as fp:
        fp.write(output)