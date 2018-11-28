#include<bits/stdc++.h>

using namespace std;
const double pi=acos(-1);
struct node{double r,h;} a[100010];
int n,k;
priority_queue<double, vector<double>, greater<double> > h;
bool cmp(node a,node b)
{
    return a.r<b.r;
}

double sqr(double x)
{
    return x*x;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int cas;
    scanf("%d",&cas);
    for (int tt=1; tt<=cas; tt++)
    {
        scanf("%d%d",&n,&k);
        for (int i=1; i<=n; i++)
            scanf("%lf%lf",&a[i].r,&a[i].h);
        sort(a+1,a+1+n,cmp);
        while (!h.empty()) h.pop();
        double s=0,ans=0;
        for (int i=1; i<=k; i++)
        {
            double x=2.0*pi*a[i].r*a[i].h;
            h.push(x);
            s+=x;
        }
        ans=max(ans,s+sqr(a[k].r)*pi);
        for (int i=k+1; i<=n; i++)
        {
            double x=h.top(),y=2.0*pi*a[i].r*a[i].h;
            h.pop(); h.push(y);
            s=s+y-x;
            ans=max(ans,s+sqr(a[i].r)*pi);
        }
        printf("Case #%d: %.9lf\n",tt,ans);
    }
}
