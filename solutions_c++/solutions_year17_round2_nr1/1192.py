#include<bits/stdc++.h>
using namespace std;
struct horse
{
    int k;
    int s;
};
horse h[1002];
bool cmp(horse a,horse b)
{
    return a.k>b.k;
}
int main()
{
freopen("A-large.in","r",stdin);
freopen("a-b.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cases=1;cases<=t;cases++)
    {
        int n,d;
        scanf("%d%d",&d,&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&h[i].k,&h[i].s);
        }
        sort(h,h+n,cmp);
        double ti=-1;
        for(int i=0;i<n;i++)
        {
            double nowt=1.0*(d-h[i].k)/h[i].s;
            if(nowt>ti)ti=nowt;
        }
        printf("Case #%d: %.6lf\n",cases,d/ti);
    }
    return 0;
}
