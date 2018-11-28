
def test_sequence(sequence):
    
    sequence = sequence.split()
    tests = []
    buttons = int(sequence[0])
    for i in range(buttons):
        tests.append((sequence[1+2*i], int(sequence[2+2*i])))
    orange = robot("O")
    blue = robot("B")
    count = 0
    
    #print orange
    #print blue
    #print tests, "\n================================================"
    while tests:
        if tests[0][0] == "O":#Orange's turn
            if orange.move_if_req(tests):
                blue.move_towards_button(tests)
            else:
                blue.move_if_req(tests)
        else: #Blue's turn
            if blue.move_if_req(tests):
                orange.move_towards_button(tests)
            else:
                orange.move_if_req(tests)
        
        
        count += 1
        #print tests
    return count
    
class robot(object):
    def __init__(self, color):

        self.pos = 1
        self.color = color
        
    def __str__(self):
        return self.color +  str(self.pos)
    
    def is_at_button(self, pos):
        if pos[0] == self.color and pos[1] == self.pos:
            return True
        

    def move_if_req(self, tests):
        """Return True if a button is pressed"""
        if not tests:
            return
        if tests[0][0] == self.color: # next test is for robot
            if tests[0][1] == self.pos: # currently at button position
                tests.pop(0)
                #print "%s pressed button at %d" %(self.color, self.pos)
                return True
            else:
                self.move_towards_button(tests)
        else: # next test is for the other robot
            
            self.move_towards_button(tests)
            
            
    def move_towards_button(self, tests):
        next_button = self.my_next_button(tests)
        if next_button:
            if next_button > self.pos:
                self.pos += 1
            elif next_button < self.pos:
                self.pos -= 1
            #print "%s moved to %d" %(self.color, self.pos)
            
    def my_next_button(self, tests):
        for i in range(len(tests)):
            if tests[i][0] == self.color:
                return tests[i][1]
        return
    
if __name__ == "__main__":
    name = raw_input("Input file:")
    input_file = open(name + ".in")
    output_file = open(name + ".txt", "w")
    input_file.readline()
    line = input_file.readline()
    case = 1
    while line:
        output_file.write("Case #%d: %d\n" %(case, test_sequence(line)))
        line = input_file.readline()
        case += 1
    input_file.close()
    output_file.close()
