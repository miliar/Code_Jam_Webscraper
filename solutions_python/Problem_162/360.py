def main():
    with open('A-small-attempt5.in') as f:
        with open('output.txt', 'w+') as o:
            f.readline()
            casenum = 1
            for line in f:
                parts = int(line)
                nums = [1]
                steps = 1
                while max(nums) != parts:
                    tnums = []
                    for num in nums:
                        revnum = int(str(num)[::-1])
                        tnum = num + 1
                        tnums.append(tnum)
                        if max(nums) < revnum <= parts:
                            tnums.append(revnum)
                    nums = list(set(tnums))
                    steps += 1
                    # print str(steps) + " " + str(num) + " " + str(rnum)
                o.write("Case #" + str(casenum) + ": " + str(steps) + "\n")
                casenum += 1

if __name__ == "__main__":
    main()