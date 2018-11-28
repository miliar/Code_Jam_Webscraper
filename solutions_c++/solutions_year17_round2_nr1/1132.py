#include<stdio.h>
#include<algorithm>

using namespace std; 

int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int cases, N ,T, i;
    double K, S, D, an;
    scanf("%d",&T);
    for(cases=1; cases<=T; cases++){
        scanf("%lf%d",&D,&N);
        an = -1;
        for(i=1;i<=N;i++){
            scanf("%lf%lf",&K,&S);
            an = an == -1 ? D/((D-K)/S) : min(an, D/((D-K)/S));
        }
        printf("Case #%d: %lf\n", cases, an);
    }
    
    return 0; 
} 
 
