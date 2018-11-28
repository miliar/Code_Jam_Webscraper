#include<cstdio>
#include<algorithm>
using namespace std;
double ma,k,s,d;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    int i,t,j,n;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        ma=0;
        scanf("%lf %d",&d,&n);
        for(i=0;i<n;i++){
            scanf("%lf %lf",&k,&s);
            ma=max(ma,(d-k)/s);
        }
        printf("Case #%d: %lf\n",j,d/ma);
    }
    return 0;
}
