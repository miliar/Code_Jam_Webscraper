#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

char S[20];

int main(){
    freopen("/Users/eajoy/Downloads/A-large.in", "r", stdin);
    freopen("/Users/eajoy/Downloads/A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int CASE = 1; CASE <= T; ++CASE){
        int K;
        scanf(" %s %d", S, &K);
        int len = (int)strlen(S);
        int ans = 0;
        for (int i = 0; i <= len-K; ++i){
            if (S[i] == '-'){
                ++ans;
                for (int j = 0; j < K; ++j)
                    if (S[i+j] == '-') S[i+j] = '+';
                    else S[i+j] = '-';
            }
        }
        for (int i = len-K; i < len; ++i){
            if (S[i] == '-'){
                ans = -1;
                break;
            }
        }
        printf("Case #%d: ", CASE);
        if (ans == -1) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}
