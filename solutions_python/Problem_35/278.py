# Qual 2009 B

import sys

STATE_READ_NUM_MAPS = 1
STATE_READ_DIMENSIONS = 2
STATE_READ_ALTITUDES = 3


class Case(object):
    
    def __init__(self, case_no):
        self.case_no = case_no
        self.x_dim = 0
        self.y_dim = 0
        self.altitudes = []
        self.basins = []
        self.sinks_to = []
        
    def set_dims(self, x, y):
        self.x_dim = x
        self.y_dim = y
        for i in range(y):
            row = []
            row2 = []
            for j in range(x):
                row.append(None)
                row2.append(None)
            self.sinks_to.append(row)
            self.basins.append(row2)

    def pp_altitudes(self):
        out = ''
        for row in self.altitudes:
            out+= '%s\n' % row
        return out

    def pp_sinks_to(self):
        out = ''
        for row in self.sinks_to:
            out+= '%s\n' % row
        return out

    def pp_basins(self):
        out = ''
        for row in self.basins:
            if out:
                out += '\n'
            out_row = ''
            for char in row:
                if out_row:
                    out_row += ' '
                out_row += char    
            out += out_row
        return out

    def output(self):
        return 'Case #%s:\n%s' % (self.case_no, self.pp_basins())

    def __repr__(self):
        return '<Case %s %s %s %s %s>' % (self.case_no, self.x_dim, 
                                    self.y_dim, self.altitudes, self.sinks_to)



def process_input(file_name):
    all_cases = []
    f = file(file_name)
    state = STATE_READ_NUM_MAPS
    case_no = 1
    case = Case(case_no)
    all_cases.append(case)
    for line in f.readlines():
        if line[-1] == '\n':
            line = line[:-1]
        if state == STATE_READ_NUM_MAPS:
            num_maps = int(line)
            state = STATE_READ_DIMENSIONS
        elif state == STATE_READ_DIMENSIONS:
            y_dim, x_dim = [int(i) for i in line.split(' ')]
            case.set_dims(x_dim, y_dim)
            state = STATE_READ_ALTITUDES
            num_altitude_lines_remaining = case.y_dim
        else:
            case.altitudes.append([int(i) for i in line.split(' ')])
            num_altitude_lines_remaining -= 1
            if num_altitude_lines_remaining == 0:
                case_no += 1
                case = Case(case_no)
                all_cases.append(case)
                state = STATE_READ_DIMENSIONS
            
    return all_cases[:-1]


def get_sinks(case):
    for y in range(case.y_dim):
        for x in range(case.x_dim):
            try:
                get_sink(case, x, y)
                
            except Exception, ex:
                print 'failed in ', x,y, ex
                1/0

    
    for y in range(case.y_dim):
        for x in range(case.x_dim):
            print case.sinks_to[y][x]

def get_sink(case, x, y):
    if case.sinks_to[y][x]:
        return
    dest_x, dest_y = get_immediate_destination(case, x, y)
    if dest_x == x and dest_y == y:
        case.sinks_to[y][x] = (x,y)
        print x,y,'is a sink'
        print case.sinks_to[y]
        return 
    print 'idest for %s %s is %s %s' % (x,y,dest_x,dest_y)
    if case.sinks_to[dest_y][dest_x]:
        case.sinks_to[y][x] = case.sinks_to[dest_y][dest_x]
        return
    else:
         print 'idest2 for %s %s is %s %s' % (x,y,dest_x,dest_y)
         get_sink(case, dest_x, dest_y)
         assert case.sinks_to[dest_y][dest_x]
         case.sinks_to[y][x] = case.sinks_to[dest_y][dest_x]
         return
    raise Exception()
    
def get_immediate_destination(case, x, y):
    local_height = case.altitudes[y][x]
    minimum_height = local_height - 1
    surrounding_cells = get_surrounding_cells(case, x, y)
    print 'surrounding cells for ',x,y,'is', surrounding_cells
    possible_drain_cells = []
    for i,j in surrounding_cells:
        height = case.altitudes[j][i]
        if height < minimum_height:
            minimum_height = height
            possible_drain_cells = [(i,j)]
        elif height == minimum_height:
            possible_drain_cells.append((i,j))
    print 'possible_drain_cells for ',x,y,'is', possible_drain_cells
    if len(possible_drain_cells) == 0:
        return x,y
    elif len(possible_drain_cells) == 1:
        return possible_drain_cells[0]
    else:
        if (x, y-1) in possible_drain_cells:
            return (x, y-1)
        elif (x-1, y) in possible_drain_cells:
            return (x-1, y)
        elif (x+1, y) in possible_drain_cells:
            return (x+1, y)
        elif (x, y+1) in possible_drain_cells:
            return (x, y+1)
        else:
            raise Exception()


def get_surrounding_cells(case,x,y):
    cells = []
    if y-1 >= 0:
        cells.append((x, y-1))
    if y+1 < case.y_dim:
        cells.append((x, y+1))
    if x-1 >= 0:
        cells.append((x-1, y))
    if x+1 < case.x_dim:
        cells.append((x+1, y))
    return cells


def label_basins(case):
    sinks_to_basin_label = {}
    next_label = 'a'
    for y in range(case.y_dim):
        for x in range(case.x_dim):
            print x,y
            sinks_to = case.sinks_to[y][x]
            print sinks_to
            if sinks_to not in sinks_to_basin_label:
                sinks_to_basin_label[sinks_to] = next_label
                next_label = chr(ord(next_label) + 1)
                print next_label
            case.basins[y][x] = sinks_to_basin_label[sinks_to]




def test_get_surrounding_cells():
    case = Case(1)
    case.set_dims(3,3)
    print get_surrounding_cells(case,2,2)


if __name__ == '__main__':


    test_get_surrounding_cells()
    #sys.exit(0)

    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'

    all_cases = process_input(input_file_name)

    case = all_cases[0]
    print case.pp_altitudes()
    #print get_immediate_destination(case, 0, 0)
    #print get_immediate_destination(case, 1, 1)
    #print get_immediate_destination(case, 2, 2)

    get_sink(case, 1, 1)
    get_sink(case, 0, 1)
    get_sink(case, 2, 1)
    print case.pp_sinks_to()
    #sys.exit(0)

    for case in all_cases:
        get_sinks(case)
        label_basins(case)

    output_file = file(output_file_name, 'w')
    for case in all_cases:
        print case.pp_altitudes()
        print case.pp_sinks_to()
        print case.pp_basins()
        #print case.output()
        output_file.write(case.output() + '\n')
    output_file.close()
