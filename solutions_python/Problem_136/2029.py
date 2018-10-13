
def better_to_wait(current_amount,current_rate,cost,rate,goal):
    if (goal-current_amount)/current_rate < (goal-current_amount+cost)/(current_rate+rate):
        return True
    else:
        return False

def calculate_max(cost,rate,goal):
    current_rate = 2
    time =0
    amount = 0
    while amount<goal:
        if amount >= cost:
            if better_to_wait(amount,current_rate,cost,rate,goal):
                time = time + (goal-amount)/current_rate
                amount = goal
            else:
                amount = amount - cost
                current_rate = current_rate + rate
        else:
            if cost > goal:
                time = time + (goal-amount)/current_rate
                amount = goal
            else:
                time = time + (cost-amount)/current_rate
                amount = cost
    return time



if __name__ == "__main__":
    with open('problem.txt','r') as f:
        with open('solution.txt','w') as g:
            trials = int(f.readline())
            for i in range(0,trials):
                trial = f.readline().split()
                maximum = calculate_max(float(trial[0]),float(trial[1]),float(trial[2]))
                g.write("Case #%s: %s \n"%(i+1,maximum))
