#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a_large_out.txt","w",stdout);
    int C=1,t,i,d,n,k,s;
    double dk,dt,dd,ans;
    ll a;
    scanf("%d",&t);
    while(t--)
    {
        dd=0;
        scanf("%d %d",&d,&n);
        for(i=0;i<n;i++)
        {
            scanf("%d %d",&k,&s);
            dk=d-k;
            dt=dk/s;
            dd=max(dt,dd);
        }
        ans=d/dd;
        printf("Case #%d: %.6lf\n",C++,ans);
    }
    return 0;
}


