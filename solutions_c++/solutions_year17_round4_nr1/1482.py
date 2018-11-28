#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int T, N, P;
int rem[4];

int main(){
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        memset(rem, 0, sizeof(rem));
        scanf("%d%d", &N, &P);
        for(int i = 0; i < N; i++){
            int g;
            scanf("%d", &g);
            rem[g % P]++;
        }

        int cnt = rem[0];
        if (P == 2){
            cnt += rem[1] / 2;
            cnt += rem[1] % 2;
        }
        if (P == 3){
            int a = min(rem[1], rem[2]);
            cnt += a;
            rem[1] -= a, rem[2] -= a;
            cnt += rem[1] / 3 + rem[2] / 3;
            cnt += min(1, rem[1] % 3 + rem[2] % 3);
        }
        if (P == 4){
            //(1,3)
            int a = min(rem[1], rem[3]);
            cnt += a;
            rem[1] -= a, rem[3] -= a;

            //(2,2)
            a = rem[2] / 2;
            cnt += a;
            rem[2] -= a * 2;

            //(1,1,2)
            a = min(rem[1] / 2, rem[2]);
            cnt += a;
            rem[1] -= a * 2, rem[2] -= a;

            //(2,3,3)
            a = min(rem[2], rem[3] / 2);
            cnt += a;
            rem[2] -= a, rem[3] -= a * 2;

            //(1,1,1,1)
            a = rem[1] / 4;
            cnt += a;
            rem[1] %= 4;

            //(3,3,3,3)
            a = rem[3] / 4;
            cnt += a;
            rem[3] %= 4;

            //remain
            cnt += min(1, rem[1] % 4 + rem[2] % 4 + rem[3] % 4);
        }
        printf("Case #%d: %d\n", t, cnt);
    }
    return 0;
}
