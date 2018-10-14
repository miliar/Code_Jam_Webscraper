'''
Created on 14-04-2012

@author: Marta
'''

def pass_soft_condition(suma, limit):
    return suma >= limit and suma >=3*limit-4

def pass_hard_condition(suma, limit):
    return suma >= limit and suma >= 3*limit-2

def get_soft_conditions_pass_count(only_soft_count, limit):
    return min(only_soft_count, limit)

def hard_count_only_soft_count(scores, limi_score):
    hard_count = 0
    only_soft_count = 0
    for sum in scores:
        pass_hard = pass_hard_condition(sum, limi_score)
        pass_soft = False
        if pass_hard:
            hard_count += 1
        else:
            only_soft_count += 1 if pass_soft_condition(sum, limi_score) else 0
    return hard_count, only_soft_count
            
def passing_count(scores, limit_score, limit_uncompensed):
    hard_count, only_soft_count = hard_count_only_soft_count(scores, limit_score)
    soft_pass_count = get_soft_conditions_pass_count(only_soft_count, limit_uncompensed)
    return hard_count + soft_pass_count


def process_input(in_filename, out_filename):
    file = open(in_filename, 'r')
    output = open(out_filename, 'w+')
    # dont care abount number of cases
    file.readline()  
    i = 0  
    for line in file.readlines():
        i+=1
        numbers = line.split()
        numbers = [int(number) for number in numbers]
        S = numbers[1] # number of suprising tripets
        p = numbers[2] # score_linit
        scores = numbers[3:]
        result = passing_count(scores, p, S)
        heading = "Case #%d: %d\n" %(i, result)
        output.write(heading)
        
if __name__ == '__main__':
    process_input('../input/B-large.in', '../output/output-large')