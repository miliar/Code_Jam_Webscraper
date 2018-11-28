#include <stdio.h>
#include <string.h>

int T, N, K, Cnt;
char S[1002];

int main(void) {

    int i, j, k, ok;

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(i=1 ; i<=T ; i++) {
        scanf("%s %d",S+1,&K);
        N=strlen(S+1);
        Cnt=0;
        for(j=1 ; j<=N-K+1 ; j++)
            if(S[j]=='-') {
                Cnt++;
                for(k=j ; k<=j+K-1 ; k++) {
                    if(S[k]=='+')
                        S[k]='-';
                    else
                        S[k]='+';
                }
            }
        ok=1;
        for(j=N-K+2 ; j<=N && ok ; j++) {
            if(S[j]=='-')
                ok=0;
        }
        printf("Case #%d: ",i);
        if(ok)
            printf("%d\n",Cnt);
        else
            printf("IMPOSSIBLE\n");
    }

    return 0;
}
