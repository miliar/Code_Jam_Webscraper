"""
000 % 0
001 % 1
011 % 2
002 % 2 *
012 % 0 *
022 % 1 *
"""

times = int(raw_input())
i = 1
process = []
while i <= times:
    sentence = raw_input()
    fields = [int(k) for k in sentence.split()]
    persons, surprise, max_number, scores = fields[0], fields[1], fields[2], fields[3:]
    scores.sort(reverse=True)
    result = 0
    for j in range(persons):
        score = scores[j]
        yushu = score % 3
        if score == 0:
            if max_number == 0:
                result += 1
                continue
            else:
                continue
        if score == 1:
            if max_number <= 1:
                result += 1
                continue
            else:
                continue

        if score / 3 + 2 < max_number:
            break

        if yushu == 2:
            if score / 3 + 1 >= max_number:
                result += 1
            elif surprise > 0 and score / 3 + 2 >= max_number:
                result += 1
                surprise -= 1
        elif yushu == 0:
            if score / 3 >= max_number:
                result += 1
            elif surprise > 0 and score / 3 + 1 >= max_number:
                result += 1
                surprise -= 1
        else:
            if score / 3 + 1 >= max_number:
                result += 1
            elif surprise > 0 and score / 3 + 1 >= max_number:
                result += 1
                surprise -= 1
    process.append("Case #%d: %d" % (i, result))
    i += 1

for j in process:
    print j


