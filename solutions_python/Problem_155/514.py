def standing_ovation():
    inputs = open('standing-ovation.txt', 'r')
    output = open('standing-ovation-ans.txt', 'w')
    cases = int(inputs.readline())

    for case in range(0, cases):
        info = inputs.readline().split(' ')

        max_shyness = int(info[0])
        num_standing = 0
        num_needed = 0
        for i in range(0, max_shyness+1):
            if num_standing < i:
                num_needed += (i - num_standing)
                num_standing = i
            num_standing += int(info[1][i])
        result = 'Case #%d: %d\n' % (case+1, num_needed)
        output.write(result)

standing_ovation();