#include<cstdio>
#include<cstring>

int T, K;
char S[1010];
int minus[1010];

int main() {
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++) {
        scanf("%s%d", S, &K);
        
        memset(minus, 0, sizeof(minus));
        int ans = 0;
        
        int l = strlen(S), add = 0;
        for (int i = 0; i < l; i++) {
            add -= minus[i];
            if( (add % 2 == 0) && S[i] == '+' ) continue;
            if( (add % 2 == 1) && S[i] == '-' ) continue;
            if (i + K - 1 >= l) {
                ans = -1;
                break;
            }
            add++, minus[i + K]++, ans++;
        }
        printf("Case #%d: ", cas);
        if (ans == -1) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}