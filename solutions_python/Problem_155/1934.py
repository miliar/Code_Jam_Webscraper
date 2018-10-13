cases = int(input())

for case in range(cases):
    line = input().split()
    s_max = int(line[0])
    audience = [int(x) for x in line[1]]

    cumulative_audience = []

    friends = 0

    for index, item in enumerate(audience):
        if cumulative_audience:
            cumulative_audience.append(item + cumulative_audience[index - 1])
        else:
            cumulative_audience.append(item)

        if cumulative_audience[-1] <= index:
            new_friends = index - cumulative_audience[-1] + 1
            friends += new_friends
            cumulative_audience[-1] += new_friends

    print('Case #%s: %s' % (case + 1, friends))