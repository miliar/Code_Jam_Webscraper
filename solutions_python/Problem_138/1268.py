num_tests = int(raw_input())

for t in range(num_tests):
    
    case = t + 1
    
    num_blocks = int(raw_input())
    naomi_blocks = raw_input().split(' ')
    naomi_blocks.sort(reverse = True)
    ken_blocks =raw_input().split(' ')
    ken_blocks.sort(reverse = True)
    orig_naomi_blocks = list(naomi_blocks)

    naomi_score_dec = 0
    for i in range(num_blocks):
        ken_choice = float(ken_blocks[i])
        
        ind = len(naomi_blocks) - 1
        best_choice = -1
        while (ind >= 0):
            naomi_choice = float(naomi_blocks[ind])
            if(naomi_choice > ken_choice):
                best_choice = ind
                break;
            ind -= 1

        if (best_choice == -1):
            best_choice = -1

        if (float(naomi_blocks[best_choice]) > ken_choice):
            naomi_score_dec += 1
        del naomi_blocks[best_choice]

    naomi_score = 0
    naomi_blocks = orig_naomi_blocks
    for i in range(num_blocks):
        naomi_choice = float(naomi_blocks[i])
        
        ind = len(ken_blocks) - 1
        best_choice = -1
        while (ind >= 0):
            ken_choice = float(ken_blocks[ind])
            if (ken_choice > naomi_choice):
                best_choice = ind
                break;
            ind -= 1
        if (best_choice == -1):
            best_choice = -1

        if (naomi_choice > ken_choice):
            naomi_score += 1
        del ken_blocks[best_choice]

    print 'Case #' + str(case) + ': ' + str(naomi_score_dec) + ' ' + str(naomi_score)

