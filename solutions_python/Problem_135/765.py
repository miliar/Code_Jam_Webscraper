def magic(T, r1, r2, m1, m2):
    tmp1 = m1[r1 - 1]
    tmp2 = m2[r2 - 1]
    same = [v1 for v1 in tmp1 for v2 in tmp2 if v1 == v2]
    count = len(same)

    if count == 0:
        return "Case #%d: Volunteer cheated!" % T
    elif count == 1:
        return "Case #%d: %d" % (T, same[0])
    else:
        return "Case #%d: Bad magician!" % T


def parse_matrix(m):
    return [list(map(int, line.strip().split(' '))) for line in m]


with open("A-small-attempt0.in", "r") as f:
    with open("A-small.out", "w") as fo:
        lines = f.readlines()
        T = int(lines[0].strip())


        for i in range(0, T):
            r1 = int(lines[1 + i * 10].strip())
            r2 = int(lines[6 + i * 10].strip())

            sm1 = 2 + i * 10
            em1 = 6 + i * 10
            m1 = parse_matrix(lines[sm1:em1])

            sm2 = 7 + i * 10
            em2 = 11 + i * 10
            m2 = parse_matrix(lines[sm2:em2])
            #print(r1, r2, m1, m2, sm1, em1, sm2, em2, i)
            
            result = magic(i + 1, r1, r2, m1, m2)
            print(result)
            fo.write(result + '\n')
