#include <bits/stdc++.h>
using namespace std;

void solve(char S[], int L, int K) {
    int ct = 0, i = 0;

    while(i < L) {
        if(S[i] == '-') {
            if(i > L - K) {
                printf("IMPOSSIBLE\n");
                return;
            }
            for(int j = 0; j < K; j++)
                S[i + j] = (S[i + j] == '-') ? '+' : '-';
            ct++;
        }
        i++;
    }

    printf("%d\n", ct);
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int T, K;
    char S[1005];

    scanf("%d", &T);

    for(int cs = 1; cs <= T; cs++) {
        scanf("%s %d", S, &K);

        int L = strlen(S);

        printf("Case #%d: ", cs);

        solve(S, L, K);
    }

    return 0;
}
