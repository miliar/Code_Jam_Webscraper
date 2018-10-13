'''
Created on Apr 14, 2012

@author: maka6er
'''

def isSurprising(triplet):
    result = False
    for i in range(0, len(triplet)):
        for j in range(0, len(triplet)):
            if i != j and abs(triplet[i] - triplet[j]) >= 2:
                result = True
                break
        if not result:
            break
    return result

# Create triplet with maximum spread of scores
def make_triplet(total_score):
    if total_score == 0:
        return [0, 0, 0]
    elif total_score == 1:
        return [0, 0, 1]
    elif total_score == 2:
        return [0, 0, 2]
    
    triplet = []
    
    balance = total_score % 3
    median = total_score / 3

    if balance == 0:
        triplet = [median - 1, median, median + 1]
    else:
        triplet = [median, median, median + balance]
    
    return triplet

def normalize(triplet):
    result = False
    normalized = sorted(triplet)

    if normalized[0] == normalized[1] and normalized[1] != normalized[2]:
        if normalized[2] - normalized[1] > 1:
            normalized[1] += 1
            normalized[2] -= 1
            result = True
    elif normalized[0] != normalized[1] and normalized[1] != normalized[2]:
        if normalized[2] - normalized[1] >= 1 and normalized[1] - normalized[0] >= 1:
            normalized[0] += 1
            normalized[2] -= 1
            result = True

    return normalized, result


def bestResult(total_scores, surprising, atLeast):
    triplets = []
    s = 0
    
    for total_score in total_scores:
        triplet = make_triplet(total_score)
        previous = triplet
        
        if s < surprising:
            normalized, r = normalize(triplet)
            if max(previous) >= atLeast:            
                while max(normalized) >= atLeast and r:
                    previous = normalized
                    normalized, r = normalize(normalized)
            else:
                while r:
                    previous = normalized
                    normalized, r = normalize(normalized)
        else:
            normalized, r = normalize(triplet)            
            while r:
                previous = normalized
                normalized, r = normalize(normalized)

        if isSurprising(previous):
            s += 1
        if max(previous) >= atLeast:
            triplets.append(previous)

    return len(triplets)


T = 0
lines = []
input_file = open('Dancing_With_the_Googlers.small.input', 'r')
input_file_lines = input_file.readlines()
T = int(input_file_lines[0])
line_number = 0
for line in input_file_lines:
    if line_number > 0:
        lines.append(line.rstrip('\n').split(' '))
    line_number += 1
    if line_number > T:
        break
#===============================================================================
results = []
j = 1
for line in lines:
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    max_scores = []
    for i in range(0, N):
        max_scores.append(int(line[3 + i]))    
    results.append('Case #' + str(j) + ': ' + str(bestResult(max_scores, S, p))) 
    j += 1

#===============================================================================

output_file = open('Dancing_With_the_Googlers.large.output', 'w')

for line in results:
    output_file.write(str(line))
    output_file.write('\n')
