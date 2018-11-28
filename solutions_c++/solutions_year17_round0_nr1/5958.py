#include <stdio.h>
#include <string.h>

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("large-output.txt", "w", stdout);
    int tc; scanf("%d", &tc);
    for(int testCase = 1; testCase <= tc; testCase++){
        char S[1100]={0,}; scanf("%s", S);
        int K; scanf("%d", &K);
        int len = (int)strlen(S), res = 0;
        for(int i = 0; i <= len - K; i++){
            if(S[i] == '-'){
                res++;
                for(int j = i; j < i+K; j++){
                    S[j] = (S[j] == '-')?'+':'-';
                }
            }
        }
        bool possible = true;
        for(int i = len - K + 1; i < len; i++){
            if(S[i] == '-') possible = false;
        }
        
        printf("Case #%d: ", testCase);
        if(possible)
            printf("%d\n", res);
        else
            printf("IMPOSSIBLE\n");
    }
}
