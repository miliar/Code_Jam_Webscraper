#include<stdio.h>
#include<string.h>
#define N (1010)
char s[N], k;
int main(){
    int T;
    scanf("%d",&T);
    int u = '+' + '-';
    for (int tc = 1; tc <= T ; tc++){
        printf("Case #%d: ",tc);
        scanf("%s%d",s,&k);
        int l = strlen(s), ans = 0;
        for (int i = 0; i <= l - k; i++){
            if (s[i] == '-'){
                for (int j = i + 1; j < i + k; j++){
                    s[j] = (char)((int)u - (int)s[j]);
                }
                ans++;
            }
        }
        for (int p = l - k + 1; p < l; p++){
            if (s[p] == '-'){
                ans = -1;
                break;
            }
        }
        if (~ans){
            printf("%d\n",ans);
        }
        else {
            printf("IMPOSSIBLE\n");
        }
    }
        
}