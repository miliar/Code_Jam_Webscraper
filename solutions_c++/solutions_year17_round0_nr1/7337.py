#include <cstdio>
#include <cstring>

int main(void) {
    int T, K, len, flag, cnt;
    char S[1005];

    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas) {
        scanf("%s %d", S, &K);

        len = strlen(S);
        flag = cnt = 0;
        for(int i = 0; i <= len-K; ++i) {
            if(S[i] == '-') {
                for(int j = 0; j < K; ++j) {
                    S[i+j] = S[i+j] == '-' ? '+' : '-';
                }
                ++cnt;
            }
        }
        for(int i = 1; i <= K; ++i) {
            if(S[len-i] == '-') {
                flag = 1;
                break;
            }
        }

        if(flag == 0) printf("Case #%d: %d\n", cas, cnt);
        else printf("Case #%d: IMPOSSIBLE\n", cas);
    }


    return 0;
}
