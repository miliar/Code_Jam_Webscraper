'''
Created on Apr 12, 2014

@author: learning-python
'''

def factory_time_cost (winning, cost, income, benefit):
    factory_time = cost/income
    winning_time = winning / (benefit + income)
    return winning_time + factory_time

if __name__ == '__main__':
    fh = open("cookie", "r")
    next(fh) #discard head line
    
    float_list = lambda s: [float(x) for x in s.strip().split(" ")]
    
    test_cases = (float_list(line) for line in fh)
    for index, test_data in enumerate(test_cases):
        cost, benefit, winning = test_data
        income  = 2
        time = 0
        fact_time = factory_time_cost(winning, cost, income, benefit)
        time_to_win = winning/income
        while True:
            if fact_time < time_to_win:
                time += cost/income
                income += benefit
                fact_time = factory_time_cost(winning, cost, income, benefit)
                time_to_win = winning/income
            else:
                time += time_to_win
                break
        print("Case #%d: %s " % (index + 1, round(time, 7)))
        
