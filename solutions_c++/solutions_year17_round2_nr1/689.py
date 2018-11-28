#include <bits/stdc++.h>
using namespace std;
int num[1009];
int x[1009];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,n,d;
    scanf("%d",&t);
    for (int test=1;test<=t;++test)
    {
        scanf("%d%d",&d,&n);
        for (int i=0;i<n;++i)
            scanf("%d%d",&x[i],&num[i]);
        long double l=0,r=1e14+4,mid;

        for (int i=0;i<1000;++i)
        {

            mid=(l+r)/2;
            bool is=true;
            long double mx=d/mid,sel;
            for (int j=0;j<n;++j)
            {
                if (num[j]>=mid)continue;
                sel=x[j]/(mid-num[j]);
                if (sel<mx)
                {
                    is=false;
                    break;
                }
            }
            if (is)
                l=mid;
            else
                r=mid;
        }
        printf("Case #%d: %.9lf\n",test,mid);
    }
}
