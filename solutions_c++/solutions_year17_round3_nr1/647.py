#include <cstdio>
#include <algorithm>

using namespace std;

const double pi=3.14159265359;

struct troll
{
    int r,h;
};

struct punct
{
    double val;
    int poz;
};

troll v[1010];
punct v1[1010];

int cmp1(troll a,troll b)
{
    return a.r>b.r;
}

int cmp2(punct a,punct b)
{
    return a.val>b.val;
}

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int t,n,k;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%d%d",&n,&k);
        double sol=0;
        for(int i=1;i<=n;i++)
            scanf("%d%d",&v[i].r,&v[i].h);
        sort(v+1,v+n+1,cmp1);
        for(int i=1;i<=n;i++)
        {
            v1[i].val=2*pi*v[i].r*v[i].h*1.0;
            v1[i].poz=i;
        }
        sort(v1+1,v1+n+1,cmp2);
        for(int i=1;i<=n;i++)
        {
            double r=pi*v[i].r*v[i].r*1.0+2*pi*v[i].r*v[i].h*1.0;
            int c=1;
            for(int j=1;j<=n;j++)
            {
                if(c==k) break;
                if(v1[j].poz>i) {r+=v1[j].val;c++;}
            }
            if(c==k) sol=max(sol,r);
        }
        printf("Case #%d: %.10f\n",test,sol);
    }
    return 0;
}
