#include <bits/stdc++.h>

using namespace std;

char S[1010];

int main() {

    // freopen("A-large.in", "r", stdin);
    // freopen("A-large.out", "w", stdout);

    int T, K, i, j, ans, k = 0;

    scanf("%d", &T);
    while(T--) {
        scanf("%s%d", S, &K);
        ans = 0;
        for(i=0;S[i];i++) {
            if (S[i] == '-') {
                ans++;
                for(j=i;S[j]&&j<i+K;j++)
                    S[j] = S[j] == '+' ? '-' : '+';
                if (j < i+K) {
                    ans = -1;
                    break;
                }
            }
        }
        printf("Case #%d: ", ++k);
        if (ans == -1)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);
    }

    return 0;
}
