import heapq

def solve_attack_only(hd, MHd,Ad,Hk,Ak):
    turn = 0
    while turn < 201:
        must_attack = (Hk+Ad-1)//Ad
        if Ak == 0:
            return turn + must_attack
        out = (hd+Ak-1)//Ak
        if must_attack <= out:
            return turn + must_attack
        if out <= 1:
            return float('inf')

        turn += (hd+Ak-1)//Ak - 1
        Hk -= ((hd+Ak-1)//Ak - 1) * Ad
        turn += 1 # cure
        hd = MHd - Ak
    print(turn)
    bearable = (MHd+Ak-1)//Ak - 1
    if bearable <= 1:
        if must_attack <= bearable + 1:
            return must_attack
        return float('inf')
    routine = must_attack//bearable
    if must_attack % bearable == 0:
        return routine * (bearable+1) - 1
    else:
        return routine * (bearable+1) + must_attack%bearable

def solve(Hd,Ad,Hk,Ak,B,D):
    ret = float('inf')
    max_d = 0 if D==0 else (Ak+D-1)//D
    max_b = 0 if B==0 else 100
    for d in range(max_d*2+1):
        hd = Hd
        ak = Ak
        for i in range(d):
            if hd - max(0, ak-D) <= 0:
                hd = Hd
            else:
                ak = max(0, ak-D)
            hd -= ak
        ad = Ad
        for b in range(max_b*2+1):
            if b == 0:
                # if d+solve_attack_only(hd, Hd, ad, Hk, ak) < ret:
                #     print(d,b , ':', hd, Hd, ad, Hk, ak, '-->', d+solve_attack_only(hd, Hd, ad, Hk, ak))
                ret = min(d+solve_attack_only(hd, Hd, ad, Hk, ak), ret)
                continue
            if hd - ak <= 0:
                hd = Hd
            else:
                ad = ad+B
            hd -= ak
            # if d+b+solve_attack_only(hd, Hd, ad, Hk, ak) < ret:
                # print(d,b , ':', hd, Hd, ad, Hk, ak, '-->', d+b+solve_attack_only(hd, Hd, ad, Hk, ak))
            ret = min(d+b+solve_attack_only(hd, Hd,ad,Hk,ak), ret)
    return ret if ret != float('inf') else 'IMPOSSIBLE'

def solve2(Hd,Ad,Hk,Ak,B,D):
    
    hq = []
    heapq.heappush(hq, (0,Hd,Ad,Hk,Ak,[]))
    while hq:
        turn, hd,ad,hk,ak,path = heapq.heappop(hq)
        if hk <= 0:
            return turn
        if turn != 0:
            hd -= ak
        if hd <= 0:
            continue
        for p in ['Attack', 'Buff', 'Cure', 'Debuff']:
            if p == 'Attack':
                if ad <= 0:
                    continue
                heapq.heappush(hq, (turn+1,hd,ad,hk-ad,ak,path +['A']))
            elif p =='Buff':
                if ad > hk or B==0:
                    continue
                heapq.heappush(hq, (turn+1,hd,ad+B,hk,ak,path +['B']))
            elif p == 'Cure':
                if Hd <= ak*2 or hd==Hd:
                    continue
                heapq.heappush(hq, (turn+1,Hd,ad,hk,ak,path+['C']))
            else:
                if ak == 0 or D==0:
                    continue
                heapq.heappush(hq, (turn+1,hd,ad,hk,max(0,ak-D),path+['C']))
    return 'IMPOSSIBLE'

def print_answer(t, ans):
    tmpl = 'Case #{0}: {1}'
    print(tmpl.format(t+1, ans))

if __name__ == '__main__':
    # print(solve_attack_only(2,4,3,7,1))
    # exit()
    T = int(input())
    for _ in range(T):
        Hd,Ad,Hk,Ak,B,D = map(int, input().split())
        ans = solve(Hd,Ad,Hk,Ak,B,D)
        # ans2 = solve2(Hd,Ad,Hk,Ak,B,D)
        # if ans != ans2:
        #     print(Hd,Ad,Hk,Ak,B,D , '-->',ans, ans2)
        print_answer(_, ans)
    
    # for a in range(1,12):
    #     for b in range(1,12):
    #         for c in range(12):
    #             for d in range(12):
    #                 ans = solve(a,1,b,1,d,b)
    #                 ans2 = solve2(a,1,b,1,d,b)
    #                 if ans != ans2:
    #                     print(a,1,b,1,d,b , '-->',ans, ans2, solve_attack_only(a,a,1,b,1))
    #                     exit()
