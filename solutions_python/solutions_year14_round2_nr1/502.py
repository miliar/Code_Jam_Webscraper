import sys
f = open(sys.argv[1], 'r')
T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    input_strings = []
    for n in range(N):
        input_strings.append(f.readline().strip())   

    normalized_strings = []
    for input_string in input_strings:
        normalized_string = []
        current_char = input_string[0]
        current_count = 1
        for char in input_string[1:]:
            if char != current_char:
                normalized_string.append((current_char, current_count))
                current_char = char
                current_count = 1
            else:
                current_count += 1
        normalized_string.append((current_char, current_count))
        normalized_strings.append(normalized_string)

    fegla_won = False

    # if they don't all have the same character w/ order, fegla won
    dedup_strings = []
    for normalized_string in normalized_strings:
        dedup_string = ""
        for char, count in normalized_string:
            dedup_string += char
        dedup_strings.append(dedup_string)
    base_dedup = dedup_strings[0]
    for dedup_string in dedup_strings:
        if dedup_string != base_dedup:
            fegla_won = True
            break
    if fegla_won:
        print "Case #%d: Fegla Won" % (t + 1)
        continue

    sum_string = [0 for n in range(len(normalized_strings[0]))]
    for normalized_string in normalized_strings:
        i = 0
        for char, count in normalized_string:
            sum_string[i] += count
            i += 1

    avg_string = [0 for n in range(len(normalized_strings[0]))]
    for i in range(len(avg_string)):
        avg_string[i] = round(float(sum_string[i]) / N)

    edit = 0
    for normalized_string in normalized_strings:
        i = 0
        for char, count in normalized_string:
            edit += abs(count - avg_string[i])
            i += 1

    print "Case #%d: %d" % (t + 1, edit)
