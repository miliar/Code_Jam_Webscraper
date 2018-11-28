#include<bits/stdc++.h>
using namespace std;
const int N=1004;
double k[N];
double s[N];
int main()
{
    freopen("i.in","r",stdin);
    freopen("o.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int x=1;x<=t;x++)
    {
        int n;
        double d;
        scanf("%lf %d",&d,&n);
        double mx=0,tm;
        for(int i=1;i<=n;i++)
        {
            scanf("%lf %lf",&k[i],&s[i]);
            tm=(d-k[i])/s[i];
            mx=max(mx,tm);


        }
        double ans=d/mx;
        printf("Case #%d: %0.8lf\n",x,ans);

    }
    return 0;
}
