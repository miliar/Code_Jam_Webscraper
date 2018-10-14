INPUT = {
    'data': ('string', 'linearray')
}

OUTPUT = "[%s]"

TEST = ('''\
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
''','''\
Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []
''')

def main(data):
    invoke = data[-1]
    sep1 = int(data[0]) + 1
    combines_raw = data[1:sep1]
    opposites_raw = data[sep1+1:-2]
    
    combines = dict()
    for combine in combines_raw:
        combines[combine[:2]] = combine[2]
        combines[combine[1:-4:-1]] = combine[2]    
    
    opposites = dict()
    for opposite in opposites_raw:
        for i in range(2):
            if not opposites.has_key(opposite[i]):
                opposites[opposite[i]] = []
            opposites[opposite[i]].append(opposite[1-i])
  
    element_list = []
    
    def clears(el):
        if opposites.has_key(el):
            for o in opposites[el]:
                if o in element_list:
                    return True
        else:
            return False
    
    for el in invoke:
        element_list.append(el)
        last_two = ''.join(element_list[-2:])
        
        if combines.has_key(last_two):
            element_list.pop()
            element_list.pop()
            element_list.append(combines[last_two])
        elif clears(el):
            # clear element list            
            element_list[:] = []
        
    return ', '.join(element_list)