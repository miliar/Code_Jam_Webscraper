#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

const int INF = 1000000000;
// double EPS = 1e-12;
const int MOD = 1000000007;

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    int t;
    int Hd, Ad, Hk, Ak, B, D;
    scanf("%d", &t);
    for (int tt=0 ; tt<t ; tt++) {
        scanf("%d %d %d %d %d %d", &Hd, &Ad, &Hk, &Ak, &B, &D);

        int number_of_attack = INF;
        int run_buff = 0;
        while (1) {
            int tmp = Hk / Ad;
            if (Hk % Ad > 0) tmp++;
            number_of_attack = min(number_of_attack, tmp + run_buff);
            if (B==0 || Ad > Hk) break;
            Ad += B;
            run_buff++;
        }
//        printf("Number of Attack: %d\n", number_of_attack);
        int ans = INF;
        for (int debuff=0 ; debuff <= 100 ; debuff++) {
            int current_Hd = Hd;
            int count = 0;
            int run_debuff = 0;
            int run_attack = 0;
            int current_knight_attack = Ak;
            while (count < 500) {
                if (run_attack == number_of_attack - 1) {
                    count++;
                    break;
                }

                if (run_debuff < debuff && current_Hd > current_knight_attack-D) {
                    run_debuff++;
                    current_knight_attack -= D;
                }
                else if (current_Hd <= current_knight_attack) {     // cure
                    current_Hd = Hd;
                }
                else {
                    if (run_debuff < debuff) { // debuff
                        run_debuff++;
                        current_knight_attack -= D;
                    }
                    else if (run_attack < number_of_attack) {  // attack
                        run_attack++;
                    }

//                    printf("XXXXXXX %d %d\n", run_attack, number_of_attack);
                    if (run_attack >= number_of_attack) break;
                }
                count++;
                current_Hd -= current_knight_attack;
//                printf("currentHD: %d\n", current_Hd);
                if (current_Hd <= 0) {
                    count = INF;
                    break;
                }
            }
            if (count < 500 && count < ans) ans = count;
        }
        if (ans == INF) {
            printf("Case #%d: IMPOSSIBLE\n", tt+1);
        }
        else {
            printf("Case #%d: %d\n", tt+1, ans);
        }
    }
}
