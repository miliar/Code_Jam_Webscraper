f = open('B-large.in')
test_cases = int(f.readline())
main_data = []

for i in range(test_cases):
    line_data = [int(s) for s in f.readline().split(' ')]
    sample = {}
    sample['no'] = line_data[0]
    sample['surprise'] = line_data[1]
    sample['p'] = line_data[2]
    sample['scores'] = line_data[3:]
    main_data.append(sample)

p = open('output_attempt-large.txt', 'w')
p.close()

for i in range(len(main_data)):
    sample = main_data[i]
    case = 0;
    max_score = sample['p'] * 3
    for s in sample['scores']:
        base = s / 3;
        if s%3 == 0:
            if base >= sample['p']:
                case = case + 1
            elif sample['surprise'] > 0 and base > 0 and base + 1 >= sample['p']:
                case = case + 1
                sample['surprise'] = sample['surprise'] - 1
        elif s%3 == 1:
            if base >= sample['p'] or base+1 >= sample['p']:
                case = case + 1
            elif sample['surprise'] > 0 and base > 0 and base + 1 >= sample['p']:
                case = case + 1
                sample['surprise'] = sample['surprise'] - 1
        elif s%3 == 2:
            if base + 1 >= sample['p'] or base >= sample['p']:
                case = case + 1
            elif sample['surprise'] > 0 and base + 2 >= sample['p']:
                case = case + 1
                sample['surprise'] = sample['surprise'] - 1
    p = open('output_attempt-large.txt', 'a')
    print "Case #"+str(i+1)+": " + str(case)
    print >> p, "Case #"+str(i+1)+": " + str(case)
    p.close()
