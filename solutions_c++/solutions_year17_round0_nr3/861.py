#include <stdio.h>

int T, Lev;
long long N, K, S, L;

int main(void) {

    int i, j;
    long long t, k;

    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);
    for(i=1 ; i<=T ; i++) {
        scanf("%lld %lld",&N,&K);
        t=1;
        for(Lev=1 ; K>t ; Lev++) {
            K-=t;
            t<<=1;
        }
        S=0;
        L=1;
        for(j=1 ; j<Lev ; j++) {
            if(N%2) {
                t=L=2*L+S;
                k=S;
            }
            else {
                t=L;
                k=L+2*S;
            }
            L=t;
            S=k;
            N>>=1;
        }
        if(K<=L)
            N--;
        else
            N-=2;
        printf("Case #%d: %lld %lld\n",i,N-(N/2),N/2);
    }

    return 0;
}
