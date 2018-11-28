#include <stdio.h>
#include <algorithm>
#define N 50
using namespace std;


int n,k;
double add;
double p[N+5];
void solve (void)
{
    int i,j;
    double avg,ans,sum;

    sort(p,p+n);

    sum=add;
    for(i=0;i<n;i++){
        sum+=p[i];
        avg=sum/(i+1);

        if(i==n-1 || avg <= p[i+1]) break;
    }

    ans=1;

    for(j=i+1;j<n;j++)
        ans *= p[j];
    for(j=i;j>=0;j--)
        ans *= avg;

    printf("%.6f\n",ans);


    return ;
}
int main (void)
{
    int i,j,T;

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    scanf("%d",&T);

    for(i=0;i<T;i++){
        scanf("%d %d",&n,&k);
        scanf("%lf",&add);
        for(j=0;j<n;j++)
            scanf("%lf",&p[j]);
        printf("Case #%d: ",i+1);
        solve();
    }

    return 0;
}
