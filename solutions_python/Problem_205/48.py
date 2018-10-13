import math

INF = 10 ** 10

IN = open('input.txt', 'r')
OUT = open('output.txt', 'w')

NUM_TESTS = int(IN.readline())

for test in xrange(NUM_TESTS):
    dragon_hp, dragon_atk, knight_hp, knight_atk, BUFF, DEBUFF = map(int,IN.readline().split())
    
    def execute_defense(d, off):
        count = 0
        hp = dragon_hp
        atk = knight_atk
        cure = False
        
        while d > 0:
            if hp <= atk - DEBUFF:
                if cure:
                    return INF
                hp = dragon_hp
                cure = True
            else:
                atk -= DEBUFF
                if atk < 0:
                    atk = 0
                d -= 1
                cure = False
            hp -= atk
            count += 1
                
        while off > 1:
            if hp <= atk:
                if cure:
                    return INF
                hp = dragon_hp
                cure = True
            else:
                off -= 1
                cure = False
            hp -= atk
            count += 1
        
        return count + 1
    
    # find the best offense strategy
    if BUFF == 0:
        offense_best = (knight_hp - 1) / dragon_atk + 1
    else:
        '''buff_guess = int((math.sqrt(knight_hp * BUFF) - dragon_atk) / BUFF)
        offense_best = (knight_hp - 1) / (dragon_atk + BUFF * buff_guess) + 1 + buff_guess
        
        buff = buff_guess
        while True:
            buff += 1
            offense = (knight_hp - 1) / (dragon_atk + BUFF * buff) + 1 + buff
            if offense < offense_best:
                offense_best = offense
            elif offense > offense_best:
                break
        buff = buff_guess
        while buff > 0:
            buff -= 1
            offense = (knight_hp - 1) / (dragon_atk + BUFF * buff) + 1 + buff
            if offense < offense_best:
                offense_best = offense
            elif offense > offense_best:
                break'''
        offense_best = 10 ** 10
        for buff in xrange(0, 100):
            offense = (knight_hp - 1) / (dragon_atk + BUFF * buff) + 1 + buff
            if offense < offense_best:
                offense_best = offense
                
    #print offense_best
    
    # find the best defense strategy
    if DEBUFF == 0:
        defense_best = execute_defense(0, offense_best)
    else:
        '''debuff_guess = (knight_atk-1) / DEBUFF + 1
        defense_best = execute_defense(debuff_guess, offense_best)
        debuff = debuff_guess
        while debuff > 0:
            debuff -= 1
            defense = execute_defense(debuff_guess, offense_best)
            if defense < defense_best:
                defense_best = defense
            elif defense > defense_best:
                break'''
        defense_best = 10 ** 10
        for debuff in xrange(0, (knight_atk-1) / DEBUFF + 2):
            defense = execute_defense(debuff, offense_best)
            # print debuff, defense
            if defense < defense_best:
                defense_best = defense
    
    answer = defense_best
    if defense_best == INF:
        answer = 'IMPOSSIBLE'
    OUT.write('Case #{}: {}\n'.format(test+1, answer))
    print test+1, answer

IN.close()
OUT.close()
