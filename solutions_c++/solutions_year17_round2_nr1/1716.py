#include "bits/stdc++.h"
using namespace std;
typedef long long ll;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,t;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        printf("Case #%d: ",t);
        int k,n,i;
        double d=0;
        cin>>k>>n;
        for(i=0;i<n;i++)
        {
            int x,y;
            scanf("%d%d",&x,&y);
            d=max(d,(k-x)*1.0/y);
        }
        printf("%.6f\n",k*1.0/d);
    }
    return 0;
}
