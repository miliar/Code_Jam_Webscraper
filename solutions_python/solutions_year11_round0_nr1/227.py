def parse_line(line):
    # 4 O 2 B 1 B 2 O 4
    values = line.split()
    steps = int(values[0])
    orange_tasks = []
    blue_tasks = []
    for step in range(1, steps + 1):
        robot = values[2*step - 1]
        button = int(values[2*step])
        if robot == 'O':
            orange_tasks.append((step, button))
        elif robot == 'B':
            blue_tasks.append((step, button))
    return orange_tasks, blue_tasks, steps

def advance(position, step, button, curr_step):
    if button is None:
        return (position, False)
    elif position == button:
        return (position, step == curr_step)
    elif position < button:
        return (position + 1, False)
    elif position > button:
        return (position - 1, False)
    raise Exception('Unaccounted for case')

def push_buttons(line):
    orange_tasks, blue_tasks, total_tasks = parse_line(line)
    seconds = 0
    task_accomplished = 0
    orange_position = blue_position = 1
    if orange_tasks:
        orange_step = orange_tasks[0][0]
        orange_button = orange_tasks[0][1]
        orange_tasks = orange_tasks[1:]
    else:
        orange_step = None
        orange_button = None
    if blue_tasks:
        blue_step = blue_tasks[0][0]
        blue_button = blue_tasks[0][1]
        blue_tasks = blue_tasks[1:]
    else:
        blue_step = None
        blue_button = None

    while task_accomplished < total_tasks:
        orange_position, orange_press = advance(orange_position,
                                                orange_step,
                                                orange_button,
                                                task_accomplished + 1)
        if orange_press:
            if orange_tasks:
                orange_step = orange_tasks[0][0]
                orange_button = orange_tasks[0][1]
                orange_tasks = orange_tasks[1:]
            else:
                orange_step = None
                orange_button = None

        blue_position, blue_press = advance(blue_position,
                                            blue_step,
                                            blue_button,
                                            task_accomplished + 1)
        if blue_press:
            if blue_tasks:
                blue_step = blue_tasks[0][0]
                blue_button = blue_tasks[0][1]
                blue_tasks = blue_tasks[1:]
            else:
                blue_step = None
                blue_button = None

        if orange_press or blue_press:
            task_accomplished += 1

        seconds += 1

    return seconds

with open('A-large.in', 'r') as fh:
    data = fh.read()

lines = [row for row in data.split('\n') if row]
cases = int(lines[0])

result = ''
for problem in range(1, cases + 1):
    seconds = push_buttons(lines[problem])
    print 'Case #%s: %s' % (problem, seconds)
    result += 'Case #%s: %s\n' % (problem, seconds)

result = result.strip() # trailing newline

with open('A-large.out', 'w') as fh:
    fh.write(result)
