import fileinput

from collections import Counter

for e, line in enumerate(fileinput.input()):
    if fileinput.isfirstline():
        continue

    input = tuple(int(c) for c in line.strip().split())
    counts = list(zip(input[1:], ('R', 'O', 'Y', 'G', 'B', 'V')))
    result = []
    first = ""
    last = ""
    counts = [c for c in counts if c[0]]
    while counts:
        counts.sort(reverse=True, key=lambda x: x[0])
        #print(first, last, counts)
        for i in range(len(counts)):
            count, letter = counts[i]
            if letter != last and (letter == first or i + 1 == len(counts) or counts[i + 1][0] < count):
                index = i
                break
        count -= 1
        if count > 0:
            counts[index] = (count, letter)
        else:
            del counts[index]
        result.append(letter)
        last = letter
        if not first:
            first = letter
    if len(result) > 1 and result[0] == result[-1]:
        result = "IMPOSSIBLE"
    else:
        result = "".join(result)




    print("Case #{}: {}".format(e, result))
