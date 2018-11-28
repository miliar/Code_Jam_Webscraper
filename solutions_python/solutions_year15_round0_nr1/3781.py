def standing_ovation()
    file_input = open('input.in')
    file_output = open('output.out', 'w')
    test_cases = int(file_input.readline().strip('\n'))
    for i in range(test_cases):
        case = file_input.readline().strip('\n')
        s_max = case[0]
        audience = case[2:2+s_max]
        audience_sum = 0
        added_members = 0
        for j in range(len(audience)):
            if j <= audience_sum:
                added_members += 1
            else:
                pass
            audience_members += int(audience[j])
        file_output.write('case #{0}: {1}'.format(i, added_members))   
    file_output.close()
    file_input.close()

if __name__ == '__main__':
    standing_ovation()