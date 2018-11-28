#include <string.h>
#include <cstdio>
char s[10010];

int main(){
    int T, K, len;
    scanf("%d",&T);
    for(int tc = 1; tc <= T; tc++){
        scanf("%s%d",s,&K);
        printf("Case #%d: ",tc);
        len = strlen(s);
        int flip = 0;
        for(int i = 0; i < len;i++){
            if(s[i] != '+') {
                if(i+K > len) {
                    flip = -1; break;
                }
                flip++;
                for(int j = i; j < i+K; j++) {
                    s[j] = (s[j] == '+' ? '-' : '+');
                }
            }
        }
        if(flip == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n",flip);
    }
}
