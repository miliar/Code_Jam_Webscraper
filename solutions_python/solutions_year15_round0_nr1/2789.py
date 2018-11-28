

def standing_ovation():

    input_file = 'A-large.in'
    output_file = 'output'

    with open(input_file, 'r') as fr, open(output_file, 'w') as fw:
        n_cases = int(fr.readline())

        for case in xrange(n_cases):
            case_meta = fr.readline().split()
            s_max = int(case_meta[0])
            lst = [int(x) for x in list(case_meta[1])]

            bring = 0
            standing = 0
            last_added = 0

            if lst[0] == 0:
                bring += 1
                last_added += 1
                standing += 1
            else:
                standing = lst[0]

            for k in xrange(1, len(lst)):
                if lst[k] != 0:
                    last_added = k - standing if standing < k else 0
                    standing = standing + last_added + lst[k]
                    bring += last_added
                if standing >= s_max:
                    break

            fw.write('Case #{0}: {1}\n'.format(case+1, bring))

if __name__ == '__main__':
    standing_ovation()
