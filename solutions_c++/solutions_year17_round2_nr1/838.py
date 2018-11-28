#include <cstdio>
#include <algorithm>
int K[1009];
int S[1009];
long double req[1009];

int main(){
    freopen("A-large (1).in","r",stdin);
    freopen("1bAlargeout.out","w",stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++){
        int D, N;
        scanf("%d %d", &D, &N);
        long double maxtime = 0;
        for (int i = 0; i < N; i++){
            scanf("%d %d", &K[i], &S[i]);
            req[i]  = (long double)(D-K[i])/S[i];
            if (i==0) maxtime = req[i];
            else maxtime = std::max(maxtime,req[i]);
        }
        printf("Case #%d: %.7f\n", t, D/(double)maxtime);
    }
}
