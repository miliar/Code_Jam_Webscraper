#include<cstdio>
#include<cstring>

int main() {
    int T, K, t = 0;
    char S[1010];
    scanf("%d", &T);
    while(T--) {
        scanf("%s%d", S, &K);
        int len = strlen(S);
        int ans = 0;
        for(int i = 0; i < len-K; i++) {
            if(S[i] == '+') continue;
            ans++;
            for(int j = i; j < i+K; j++) {
                S[j] = (S[j] == '+') ? '-' : '+';
            }
        }

        bool possi = true;
        char left = S[len-1];
        for(int i = len-K; i < len && possi; i++) {
            if(left != S[i]) possi = false;
        }

        if(left == '-') ans++;

        printf("Case #%d: ", ++t);
        if(!possi) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
