#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;
#define maxm  100005
#define maxn 10000
#define INF  10000
const double pi=acos(-1.0);
struct node
{
    int r,h;
}a[maxn],b[maxn];

bool cmp(node x,node y)
{
    return x.r>y.r;
}

bool cmp2(node x,node y)
{
    return 1ll*x.r*x.h>1ll*y.r*y.h;
}
int n,m;
long long solve(int idx)
{
    long long ret=1ll*a[idx].r*a[idx].r+2ll*a[idx].r*a[idx].h;
    int tot=0;
    for(int i=idx+1;i<n;i++)
    {
       b[tot++]=a[i];
    }
    sort(b,b+tot,cmp2);
    for(int i=0;i<m-1;++i)
        ret+=2ll*b[i].r*b[i].h;
    return ret;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {

        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
        {
            scanf("%d%d",&a[i].r,&a[i].h);
        }
        sort(a,a+n,cmp);
        long long ans=0;
        for(int i=0;i<n;i++)
        {
            if(i+m-1>=n) break;
            ans=max(ans,solve(i));
        }
        printf("Case #%d: %.20f\n",cas,ans*pi);
    }
}
