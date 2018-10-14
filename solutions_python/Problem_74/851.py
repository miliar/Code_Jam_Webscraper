INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large.out'

def read_input():
    f = open(INPUT_FILE, 'r')
    num_test_cases = int(f.readline())
    
    for i in range(num_test_cases):
        yield f.readline().split()[1:]
        
    f.close()

def write_output(outputs):
    f = open(OUTPUT_FILE, 'w')
    f.write('\n'.join(outputs))
    f.write('\n')
    f.close()

class Robot(object):
    position = 1
    target = -1
    
    def __init__(self, colour):
        self.colour = colour
    
    def _get_next(self, agenda, colour):
        for item in agenda:
            if item[0] == colour:
                return int(item[1])
    
    def do_action(self, agenda):
        if self.target == -1:
            self.target = self._get_next(agenda, self.colour)
        if self.target is not None:
            if self.position == self.target:
                
                return 0 == agenda.index((self.colour, str(self.position)))
            else:
                self.position += \
                    (self.target - self.position) \
                    / abs(self.target - self.position)

if __name__ == '__main__':
    outputs = []
    for test_case in read_input():
        orange = Robot('O')
        blue = Robot('B')
        seconds = 0
        agenda = []
        for i in range(0, len(test_case), 2):
            agenda.append((test_case[i], test_case[i+1]))
        
        while len(agenda):
            orange_can_do = orange.do_action(agenda)
            blue_can_do = blue.do_action(agenda)
            
            if orange_can_do or blue_can_do:
                del agenda[0]
            if orange_can_do:
                orange.target = -1
            if blue_can_do:
                blue.target = -1
            
            seconds += 1
        
        outputs.append('Case #%d: %d' % (len(outputs)+1, seconds))
    
    write_output(outputs)