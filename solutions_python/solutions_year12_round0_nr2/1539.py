def solution(case):
    input = f_in.readline()
    values = map(int,input.split(' '))
    [no_contestants, no_suprises, best_result] = [values[0], values[1], values[2]]

    contestant_score = [0]*no_contestants

    for i in range(0,no_contestants):
        contestant_score[i] = values[3+i]

    contestant_score.sort()
    used_suprises = 0
    winners = 0
            
    for i in range(no_contestants-1,-1,-1):
        delta = best_result - (contestant_score[i] - best_result)/2.0
        
        if delta <= 1:
            winners += 1
            continue
        elif delta > 2:
            continue
        else:
            if used_suprises == no_suprises:
                break
            if not(contestant_score[i] == 0 or contestant_score[i] == 30 or contestant_score[i] == 1 or contestant_score[i] == 29):
                used_suprises += 1
                winners +=1
                
    answer = winners

    if case > 0:
        f_out.write('\n')
    f_out.write('Case #'+str(case)+' '+str(answer))

path = 'C:\Code Jam'
f_in = open(path+'\B-small-attempt0.in','r')
f_out = open(path+'\out.in','w')
no_cases = int(f_in.readline())

for i in range(no_cases):
    solution(i)

f_in.close
f_out.close



   
    
