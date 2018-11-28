#include <stdio.h>

int T, D, N, K[1001], S[1001];
double A[1001], Max;

int main(void) {

    int i, j;

    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(i=1 ; i<=T ; i++) {
        scanf("%d %d",&D,&N);
        Max=0;
        for(j=1 ; j<=N ; j++) {
            scanf("%d %d",&K[j],&S[j]);
            A[j]=(double)(D-K[j])/S[j];
            if(Max<A[j])
                Max=A[j];
        }
        printf("Case #%d: %.9lf\n",i,D/Max);
    }

    return 0;
}
