#include <bits/stdc++.h>
using namespace std;

struct Node
{
    double p,s;
    bool operator < (const Node& rhs) const
    {
        return p>rhs.p;
    }
}A[1010];

int main()
{
    int T;
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;cas++)
    {
        int d,n;
        scanf("%d%d",&d,&n);
        for(int i=1;i<=n;i++) scanf("%lf%lf",&A[i].p,&A[i].s);
        sort(A+1,A+n+1);
        double t=0;
        for(int i=1;i<=n;i++)
        {
            t=max(t,(d-A[i].p)/A[i].s);
        }
        printf("Case #%d: %.6f\n",cas,d/t);
    }
    return 0;
}
