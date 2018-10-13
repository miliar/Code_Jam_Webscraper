[cases] = [int(x) for x in raw_input().strip().split()]
out = open('output.txt', 'w')

for case in range(cases):
    # solving logic goes here
    (n, k) = [int(x) for x in raw_input().strip().split()]

    sections = {n: 1}

    i = 0

    while True:
        # print sections
        if not len(sections.keys()):
            break
        s = max(sections.keys())
        num_s = sections[s]
        i += num_s
        if i >= k:
            break
        # print s, num_s, i
        # print s, num_s, i
        del sections[s]
        if s >= 1:
            for new_s in [(s-1)/2, s/2]:
                # print new_s
                if new_s in sections:
                    sections[new_s] += num_s
                else:
                    sections[new_s] = num_s

    # print sections
    # # print case
    if not len(sections.keys()):
        x = 1
    else:
        x = max(sections.keys())
    # # print sections
    # print [x/2, (x-1)/2]
    # break

    if x > 1:
        s = "Case #"+str(case+1)+": "+str(x/2) + " " + str((x-1)/2)+'\n'
    else:
        s = "Case #"+str(case+1)+": 0 0\n"
    out.write(s)
    print(s)
