class Bot:
    current_pos = None
    color = None
    steps = None
    
    def __init__(self, color, steps):
        self.current_pos = 1
        self.steps = steps
        self.color = color
        
    def next_step(self, lock):
        if self.steps:
            if self.current_pos == self.steps[0]:
                if lock == self.color:
                    self.steps = self.steps[1:]
                    return 1
            else:
                if self.current_pos > self.steps[0]: self.current_pos -= 1
                else: self.current_pos += 1

for _ in range(1, int(raw_input())+1):
    e = raw_input().split()
    count = 0
    lock = None
    steps = []
    steps_o = []
    steps_b = []
    co = e[0]
    e = e[1:]
    for __ in range(int(co)):
        if 'O' == e[:2][0]: steps_o.append(int(e[:2][1]))
        else: steps_b.append(int(e[:2][1]))
        steps.append(tuple(e[:2]))
        e = e[2:]
    
    b = Bot('b', steps_b)
    o = Bot('o', steps_o)
    
    if 'O' in steps[0]: lock = 'o'
    else: lock = 'b'
    
    while(steps):
        count += 1
        ret_o = o.next_step(lock)
        ret_b = b.next_step(lock)
        if ret_o is 1 or ret_b is 1:
            steps = steps[1:]
            if steps and 'O' in steps[0]: lock = 'o'
            else: lock = 'b'
    
    print 'Case #'+str(_)+':', count
    