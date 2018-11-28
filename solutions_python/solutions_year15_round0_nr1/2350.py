f_in = open("A-large.in", "r")

num_case = int(f_in.readline())

data = []

for line in f_in:
    # Split data to store in list
    case = line.strip()
    case = case.split(' ')

    # Initialise variables
    max_shy = int(case[0])
    ppl = case[1]
    len_ppl = max_shy + 1
    standing = 0
    needed = 0
    ans = 0

    # Process data
    for num in range(len_ppl):
        if ppl[num] != '0':
            if standing >= max_shy:
                break
            if standing >= num:
                standing += int(ppl[num])
            else:
                needed = num - standing
                ans += needed
                standing += needed + int(ppl[num])

    case.append(ans)
    data.append(case)


f_out = open("standing_ovation_output.txt", "w")

counter = 0
for shy, ppl, count in data:
    f_out.write("Case #%s: %s\n" % (counter + 1, count))
    counter += 1

f_in.close()
f_out.close()
