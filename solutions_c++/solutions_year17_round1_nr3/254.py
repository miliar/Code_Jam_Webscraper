#include <cstdio>
#include <algorithm>
#define MAX_TURN 500
#define INF 1000000

int main(){
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-small.out", "w", stdout);

    int T, Hd, Ad, Hk, Ak, B, D;

    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        scanf("%d%d%d%d%d%d", &Hd, &Ad, &Hk, &Ak, &B, &D);

        int ans = MAX_TURN;
        for(int debuff = 0; debuff <= 100; debuff++)
        for(int buff = 0; buff <= 100; buff++){
            if(B == 0 && buff > 1) break;
            if(D == 0 && debuff > 1) break;

            int HPd = Hd, ATKd = Ad, HPk = Hk, ATKk = Ak;
            int B_count = buff, D_count = debuff;

            for(int turn = 1; turn < MAX_TURN; turn++){
                if(D_count > 0){
                    if(HPd <= ATKk - D) // Cure
                        HPd = Hd - ATKk;
                    else{ // Debuff
                        ATKk -= D;
                        HPd -= ATKk;
                        D_count--;
                    }
                }
                else if(B_count > 0){
                    if(HPd <= ATKk) // Cure
                        HPd = Hd - ATKk;
                    else{ // Buff
                        ATKd += B;
                        HPd -= ATKk;
                        B_count--;
                    }
                }
                else{
                    if(HPd <= ATKk && HPk > ATKd) // Cure
                        HPd = Hd - ATKk;
                    else{
                        HPk -= ATKd;
                        HPd -= ATKk;

                        if(HPk <= 0){
                            ans = std::min(ans, turn);
                            break;
                        }
                    }
                }
            }
        }

        printf("Case #%d: ", t);
        if(ans == MAX_TURN)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
}
