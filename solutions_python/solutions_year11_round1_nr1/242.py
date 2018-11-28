# Problem A. FreeCell Statistics

current = -1 # 현재 문제 번호

with open('input.txt') as a_file:

    for a_problemset in a_file: # Case #current : turn

        current += 1

        if current == 0: # 문제 수를 구하기 위해 딱 한번 실행. 사실 필요없음.
            number_of_problem = a_problemset.strip()
            continue
        
        problem = a_problemset.split()

        N = int(problem[0]) # 최대 카드 수 N

        #print(N)

        d_win = int(problem[1])
        d_lose = 100 - int(problem[1])

        t_win = int(problem[2])
        t_lose = 100 - int(problem[2])

        #print(d_lose)

        from fractions import gcd

        d_gcd = 1 # 오늘 게임 비율 구하기 위한 최대공약수
        #if d_win is not 0 and d_lose is not 0 :
        d_gcd = gcd(d_win,d_lose)

        t_gcd = 1
        t_gcd = gcd(t_win,t_lose)

        #print(d_gcd)

        if d_win is not 0 :
            d_win = d_win / d_gcd
        if d_lose is not 0 :
            d_lose = d_lose / d_gcd

        if t_win is not 0 :
            t_win = t_win / t_gcd
        if t_lose is not 0 :
            t_lose = t_lose / t_gcd


        result = '' # asnwer
        if N < d_win + d_lose : # 횟수가 도저히 적으면
            result = 'Broken'
            print('N')

        #숫자가 충분히 크고 
        elif (t_win == 1 and t_lose == 0) or (t_win == 0 and t_lose == 1): # 토탈이 100%, 0%

            if d_win == t_win and d_lose == t_lose :  # 오늘승과 토탈승이 같으면 가능
                result = 'Possible'
                print('d == t')
            else :
                result = 'Broken'
                print('d != t')

        #숫자가 충분히 크고 토탈이 1이나 0이 아니면
        else :
            result = 'Possible'
            print('else')

        
        with open('output.txt', mode='a') as o_file:
            o_file.write('Case #')
            o_file.write(str(current))
            o_file.write(': ')
            o_file.write(str(result))
            o_file.write('\n')
