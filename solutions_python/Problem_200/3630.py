import numpy as np
 
with open('/Users/bahar/Downloads/B-large.in') as f:
    f.readline()
    case = 0
    for line in f:
        line = line.strip()
        number = np.array(list(line))
        for i in range(0, len(number)-1):
            if number[i] > number[i+1]:
                number[i] = int(number[i])-1
                number[i+1:] = 9
        case = case + 1
        print('Case #{}: {}'.format(case, int(''.join(number))))
