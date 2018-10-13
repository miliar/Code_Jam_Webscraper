def dance(scores, p, surp):
    pts = {}
    count = 0
    for score in scores:
        s1 = score / 3
        s2 = (score + 1) / 3
        s3 = score - s1 - s2
        if s1 >= p or s2 >= p or s3 >= p:
            count += 1
        elif score >= (p + 2*(p - 2)):
            pts[score] = [s1, s2, s3]

    for i in range(surp):
        if not len(pts):
            break

        max_score = max(pts.keys())
        score_pts = pts[max_score]
        score_pts.sort()
        hi = score_pts[-1] + 1
        lo = score_pts[-2] - 1

        if(hi >= p and lo >= 0 and hi - lo < 3):
            count += 1

        del pts[max_score]

    return count

fi = open("b2.in")
fo = open("b2out.txt", "w")
start = True
o = ''
i = 1
for line in fi:
    if start:
        start = False
        continue

    parts = [int(x) for x in line.split(' ')]
    o += 'Case #' + str(i) + ': ' + str(dance(parts[3:], parts[2], parts[1])) + '\n'
    i += 1

fo.write(o)