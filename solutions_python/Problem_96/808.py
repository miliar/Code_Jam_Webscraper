'''Qualification Round question B.
'''

import math

def passes_with_surprising(score, threshold):
    '''True if score can have at least one point over threshold if
    surprising, but not if it isn't'''
    fails = not passes_without_surprising(score, threshold)
    
    can_surprise = 2 < score 
    if threshold > 10: return False
    # Considering ixpytf score is greater than 28
    # It's possible to 

    qnt, mod = score / 3, score % 3
    surprises = qnt + max(mod, 1) >= threshold
    
    return fails and can_surprise and surprises

def passes_without_surprising(score, threshold):
    '''True if score can have at least one point over threshold without surprising'''
    return math.ceil(score / 3.0) >= threshold


def solve(surprising, threshold, totals):
    simple_over = len(filter(lambda score: passes_without_surprising(score, threshold),
                             totals))
    surprising_over = min(
        len(filter(lambda score:passes_with_surprising(score, threshold),
                   totals)),
        surprising)
    
    return simple_over + surprising_over

if __name__ == '__main__':
    T = int(raw_input())

    for i in range(T):
        nums = map(int, raw_input().split())
        (N, surprising, threshold), totals = nums[:3], nums[3:]
        
        print('Case #{num}: {answer}'.format(
                num=i+1,
                answer=solve(surprising, threshold, totals[:N])
                ))
