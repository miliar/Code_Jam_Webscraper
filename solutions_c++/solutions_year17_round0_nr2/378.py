#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define RESET(c,v) memset(c, v, sizeof c)

typedef long long ll;

int T;
int N;
char S[25];
bool tidy[25];

int main() {
    scanf("%d", &T);
    REP(tc, T) {
        scanf("%s", S);
        N = strlen(S);
        RESET(tidy, false);
        tidy[N-1] = true;
        for (int i = N-2; i >= 0; i--) {
            tidy[i] = S[i] <= S[i+1] && tidy[i+1];
        }

        REP(i, N-1) {
            if (S[i] < S[i+1] || (S[i] == S[i+1] && tidy[i+1])) {
                continue;
            }
            S[i]--;
            for (int j = i+1; j < N; j++) {
                S[j] = '9';
            }
            break;
        }

        printf("Case #%d: %s\n", tc+1, S[0] == '0' ? S+1 : S);
    }
}
