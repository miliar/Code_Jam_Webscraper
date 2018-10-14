class Snapper:
    """
    Google Codejam problem 1:
    Snappers are power intermediaries that control current.
    Snappers may be ON or OFF, and may only change state when powered.
    Snappers keep track of their connections, and connections must support
    the function call is_on()
    """

    def __init__(self, snapper_in=None, state='OFF'):
        """
        Only 'ON' for state means on.
        """
        self.state = state
        self.snapper_in = snapper_in

    def is_on(self):
        """
        Returns True if on and snapper_in is on, False otherwise
        """
        if self.state == 'ON' and self.snapper_in.is_on():
            return True
        return False

    def toggle(self):
        """
        Toggles if snapper_in.is_on() returns True, otherwise does nothing
        """

        if self.snapper_in.is_on():
            if self.is_on(): self.state = 'OFF'
            else: self.state = 'ON'

class PowerSource:
    """
    Powersource to complement Snapper
    """
    def __init__(self, powered=False):
        self.powered = powered

    def is_on(self):
        return self.powered

    def toggle(self):
        if self.powered:
            self.powered = False
            return
        self.powered = True

def testCase(snappers, snaps):
    snapper_array = []
    power = PowerSource(True)
    if (snappers <= 0): return 'ON'
    snapper_array.append(Snapper(power))

    for i in range(snappers - 1):
        previous_snapper = snapper_array[-1]
        #print previous_snapper
        snapper_array.append(Snapper(snapper_in=previous_snapper))
    #return snapper_array
    for i in range(snaps):
        for s in range(len(snapper_array)):
            snapper_array[-(s+1)].toggle()

    if snapper_array[-1].is_on(): return 'ON'
    else: return 'OFF'

def parse_input_and_run(input_file="", output_file=""):
    import sys
    if input_file == "": raise Exception
    in_file = open(input_file)
    if output_file == '': out_file = sys.stdout
    else: out_file = open(output_file, 'w')
    line = in_file.readline()
    line = in_file.readline()
    case_count = 1
    out_format = 'Case #%i: %s \n'
    while line:
        data = line.split(' ')
        if len(data) < 2: out_file.write(out_format % (case_count, 'OFF'))
        else:
            test_result = testCase(int(data[0]), int(data[1]))
            out_file.write(out_format % (case_count, test_result))

        line = in_file.readline()
        case_count += 1


parse_input_and_run('C:/Documents and Settings/az822pm/Desktop/A-small-attempt1.in', 'C:/out.out')
            
        
        
        

