INPUT = r'D:\Repository\CodeJamQualification\D.in'
OUTPUT = r'D:\Repository\CodeJamQualification\D.out'

import random

def decode(line):
    line_items = line.split(r' ')
    result = []
    for item in line_items:
        result.append(float(item))
    return result

def get_naomi_war_choose(naomi_blocks):
    index = random.randint(0, len(naomi_blocks) - 1)
    mass = naomi_blocks[index]
    return index, mass

def get_naomi_dwar_choose(naomi_blocks, ken_blocks):
    index = random.randint(0, len(naomi_blocks) - 1)
    mass = naomi_blocks[index]

    # Choose fake mass.
    fake_mass = mass
    if max(ken_blocks) > mass:
        fake_mass = max(ken_blocks) - 0.000001
    return index, fake_mass

def get_naomi_dwar2_choose(naomi_blocks, ken_blocks):

    # Try min-min strategy.
    naomi_min = min(naomi_blocks)
    naomi_max = max(naomi_blocks)
    ken_min = min(ken_blocks)
    ken_max = max(ken_blocks)
    if naomi_min < ken_min:
        for i in xrange(len(naomi_blocks)):
            if naomi_blocks[i] == naomi_min:
                return i, ken_max - 0.000001

    if naomi_min > ken_min:
        for i in xrange(len(naomi_blocks)):
            if naomi_blocks[i] == naomi_min:
                return i, ken_max + 0.000001

    # Min-min nad max-max fails. Go main line.
    #index = 1000000
    #mass = 2.0
    #for i in xrange(len(naomi_blocks)):
    #    current_mass = naomi_blocks[i]
    #    if current_mass > ken_max:
    #        if current_mass < mass:
    #            index = i
    #            mass = current_mass

    #return index, mass

def get_ken_choose(naomi_choose, ken_blocks):
    can_beat_naomi = False
    naomi_mass = naomi_choose[1]

    # Find min.
    index = 0
    mass = ken_blocks[0]
    for i in xrange(len(ken_blocks)):
        current_mass = ken_blocks[i]
        if current_mass < mass:
            index = i
            mass = current_mass
        if current_mass > naomi_mass:
            can_beat_naomi = True

    # Can we beat Naomi?
    if not can_beat_naomi:
        return index, mass

    index = 1000000
    mass = 2.0
    for i in xrange(len(ken_blocks)):
        current_mass = ken_blocks[i]
        if current_mass > naomi_mass:
            if current_mass < mass:
                index = i
                mass = current_mass
    return index, mass

def get_naomi_war_outcome(N, naomi_blocks, ken_blocks):
    _naomi_blocks = list(naomi_blocks)
    _ken_blocks = list(ken_blocks)
    outcome = 0
    for i in xrange(N):
        naomi_choose = get_naomi_war_choose(_naomi_blocks)
        ken_choose = get_ken_choose(naomi_choose, _ken_blocks)
        if _naomi_blocks[naomi_choose[0]] >= _ken_blocks[ken_choose[0]]:
            outcome += 1
        del _naomi_blocks[naomi_choose[0]]
        del _ken_blocks[ken_choose[0]]
    return outcome

def get_naomi_dwar_outcome(N, naomi_blocks, ken_blocks):
    _naomi_blocks = list(naomi_blocks)
    _ken_blocks = list(ken_blocks)
    outcome = 0
    for i in xrange(N):
        naomi_choose = get_naomi_dwar2_choose(_naomi_blocks, _ken_blocks)
        ken_choose = get_ken_choose(naomi_choose, _ken_blocks)
        if _naomi_blocks[naomi_choose[0]] >= _ken_blocks[ken_choose[0]]:
            outcome += 1
        del _naomi_blocks[naomi_choose[0]]
        del _ken_blocks[ken_choose[0]]
    return outcome

def process_single_case(index, input, output):
    print 'Case #', (index + 1)

    # Play both games.
    N = int(input.readline())
    naomi_blocks = decode(input.readline())
    ken_blocks = decode(input.readline())
    war_outcome = get_naomi_war_outcome(N, naomi_blocks, ken_blocks)
    dwar_outcome = get_naomi_dwar_outcome(N, naomi_blocks, ken_blocks)
    print dwar_outcome, war_outcome
    output.write('Case #' + str(index + 1) + ': ' + str(dwar_outcome) + ' ' + str(war_outcome) + '\n')

with open(INPUT, 'r') as input:
    input.seek(0)
    with open(OUTPUT, 'w') as output:
        cases = int(input.readline())
        print 'Cases:', cases
        for i in xrange(cases):
            process_single_case(i, input, output)