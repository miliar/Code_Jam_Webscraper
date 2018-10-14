
# coding: utf-8

# In[18]:

def readline_num(f, num_type=int):
    line = f.readline().strip()
    numbers = [num_type(x) for x in line.split()]
    return numbers if len(numbers) > 1 else numbers[0]


# In[35]:

def solve(input_filename, output_filename):
    input = open(input_filename)
    output = open(output_filename, 'w')

    T = readline_num(input)
    for n in range(T):
        C, F, X = readline_num(input, float)
        result = _solve(C, F, X)
        output.write('Case #%d: %.9f\n' % (n + 1, result))

    input.close()
    output.close()


# In[29]:

def _solve(cost, productivity, goal):
    current_productivity = 2.0
    time = 0.0
    if goal <= cost:
        return goal / float(current_productivity)
    else:
        while True:
            time += cost / current_productivity
            wait_time = (goal - cost) / current_productivity
            buy_time = goal / (current_productivity + productivity)
            if wait_time <= buy_time:
                time += wait_time
                break
            else:
                current_productivity += productivity
                
    return time


# In[36]:

solve('test.in', 'solution.txt')


# In[ ]:



