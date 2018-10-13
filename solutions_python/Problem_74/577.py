# -*- coding: utf-8 -*-

t = int(raw_input())

def list_op(li):
    return [(li[j], int(li[j+1])) for j in xrange(0, len(li), 2)]

def solve(operations):
    seconds = 0
    position_o = 1
    position_b = 1
    queue_o = []
    queue_b = []
    task_o = 0
    task_b = 0
    for op in operations:
        if op[0] == 'O':
            queue_o.append(op[1])
        else:
            queue_b.append(op[1])
    next_task = operations.pop(0)
    while True:
        if not next_task:
            next_task = operations.pop(0)
        # Orange
        if (not task_o) and queue_o: 
            task_o = queue_o.pop(0)
        if position_o == task_o:
            if next_task[0] == 'O':
                next_task = 0
                task_o = 0
        else:
            if position_o < task_o:
                position_o += 1
            else:
                position_o -= 1
        # Blue
        if (not task_b) and queue_b:
            task_b = queue_b.pop(0)
        if position_b == task_b:
            if next_task and next_task[0] == 'B':
                next_task = 0
                task_b = 0
        else:
            if position_b < task_b:
                position_b += 1
            else:
                position_b -= 1
        seconds += 1
        if (not next_task) and (not operations):
            break
    return seconds
for i in xrange(1, t + 1):
    nrp = raw_input().split(' ')
    n = nrp[0]
    rp = nrp[1:]
    operations = list_op(rp)
    res = solve(operations)
    print 'Case #%d: %d' % (i, res)
