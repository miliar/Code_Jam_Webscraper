import sys

def get_shortest_time(tasks):
    time_elapsed = 0

    o_pos = 1
    b_pos = 1

    # Make separate task lists
    o_tasks = []
    b_tasks = []
    for task in tasks:
        if task[0] == 'B':
            b_tasks.append(int(task[1]))
        elif task[0] == 'O':
            o_tasks.append(int(task[1]))

    turns = [task[0] for task in tasks]

    while len(o_tasks) or len(b_tasks) > 0:
        button_pushed = False
        if len(o_tasks) > 0:
            if o_pos == o_tasks[0]:
                if turns[0] == 'O':
                    o_tasks.pop(0)
                    turns.pop(0)
                    button_pushed = True
            else:
                delta = 1 if o_pos < o_tasks[0] else -1
                o_pos += delta

        if len(b_tasks) > 0:
            if b_pos == b_tasks[0]:
                if turns[0] == 'B':
                    if button_pushed == False:
                        b_tasks.pop(0)
                        turns.pop(0)
            else:
                delta = 1 if b_pos < b_tasks[0] else -1
                b_pos += delta

        time_elapsed += 1
            
    return time_elapsed

if __name__ == '__main__':
    in_path = sys.argv[1]
    with open(in_path, 'r') as in_file:
        in_file.next()
        case = 1
        for line in in_file:
            raw_data = line.split()[1:]
            tasks = [raw_data[i:i+2] for i in range(0, len(raw_data), 2)]
            
            solution = get_shortest_time(tasks)

            print "Case #%s: %s" % (case, solution)
            case += 1