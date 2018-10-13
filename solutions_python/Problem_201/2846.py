import re

# def largest_section(l):
#     a = []
#     for i, s in enumerate(l):
#         cnt = 0
#         if s == 0 and cnt == 0:


def take_optimal_position(l):
    left = 0
    right = 0
    groups = [(m.start(0) + 1, m.end(0) - m.start(0) - 1) for m in re.finditer('(o\.+)', l)]
    # m = []
    # for x in re.finditer('(10+)', l):
    #     m.append(m.start(0) + 1, m.end(0) - m.start(0) - 1)

    largest_size = 0
    largest_start_index = 0
    optimal_index = 0
    
    for index, size in groups:
        if size > largest_size:
            largest_size = size
            largest_start_index = index
    
    optimal_index = largest_start_index + (largest_size / 2) - 1
    
    if largest_size % 2 != 0:
        optimal_index += 1
    
    left = optimal_index - largest_start_index
    right = largest_size + largest_start_index - optimal_index - 1
    l = l[:optimal_index] + 'o' + l[optimal_index + 1:]
    return left, right, l

with open('C-small-1-attempt0.in','r') as fin, open('C-small-1-attempt0.out','w') as fout:
    for i, l in enumerate(fin):
        if (i > 0):
            input_vars = l.split()
            l = 'o' + ''.join(['.'] * int(input_vars[0])) + 'o'
            k = int(input_vars[1])
            while k > 0:
                left, right, l = take_optimal_position(l)
                k -= 1
            fout.write('Case #%d: %s %s\n' % (i, right, left))