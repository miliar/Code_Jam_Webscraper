#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define RESET(c,v) memset(c, v, sizeof c)

typedef long long ll;

int T;
int N, K;
char S[1005];

int main() {
    scanf("%d", &T);
    REP(tc, T) {
        scanf("%s %d", S, &K);
        N = strlen(S);

        int res = 0;
        REP(i, N-K+1) {
            if (S[i] == '-') {
                res++;
                REP(j, K) {
                    S[i+j] = '+' + '-' - S[i+j];
                }
            }
        }
        REP(i, N) {
            if (S[i] == '-') {
                res = -1;
                break;
            }
        }

        printf("Case #%d: ", tc+1);
        if (res == -1) {
            puts("IMPOSSIBLE");
        } else {
            printf("%d\n", res);
        }
    }
}
