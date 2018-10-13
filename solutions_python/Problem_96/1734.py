import os
import sys
from sure import that


input_file = open('dancers.txt', 'r')
output_file = open('dancers_solution.txt', 'w')

T = int(input_file.readline().rstrip('\n'))
case_num = 1
while case_num - 1 < T:
    data = map(int, input_file.readline().rstrip('\n').split(' '))
    num_dancers = data[0]
    num_surprising_scores = data[1]
    score_threshold = max(data[2], 0)
    total_scores = data[3:]
    assert that(len(total_scores)).equals(num_dancers)

    legal_score_threshold = score_threshold + 2 * max(score_threshold - 1, 0)
    surprising_score_threshold = score_threshold + 2 * max(score_threshold - 2, 0)

    max_num_good_dancers = 0
    for score in total_scores:
        if score >= legal_score_threshold:
            max_num_good_dancers += 1
        elif score >= surprising_score_threshold and num_surprising_scores > 0:
            num_surprising_scores -= 1
            max_num_good_dancers += 1

    output_file.write('Case #{}: {}\n'.format(case_num, max_num_good_dancers))
    case_num += 1
