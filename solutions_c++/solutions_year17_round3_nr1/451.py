#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
#include<map>
#include<vector>
#include<set>
#include<cmath>
using namespace std;
#define LL long long

const double pi=acos(-1.0);
int t,n,k;

struct node
{
    double r,h;
    double s;
}p[1005];

bool cmp(node a,node b)
{
    return a.s>b.s;
}

int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d",&t);
    int z=1;
    while(t--)
    {
        scanf("%d %d",&n,&k);
        for(int i=0;i<n;++i)
        {
            scanf("%lf %lf",&p[i].r,&p[i].h);
            p[i].s=2*pi*p[i].r*p[i].h;//cout<<p[i].s<<endl;
        }
        sort(p,p+n,cmp);
        double sum=0;
        double maxx=0;
        for(int i=0;i<n;++i)
        {
            double r=p[i].r;
            double base=pi*r*r;
            int cnts=0;
            sum=p[i].s+base;
            for(int j=0;j<n;++j)
            {
                if(cnts>=k-1) break;
                if(i==j) continue;
                if(p[j].r>r) continue;
                sum+=p[j].s;
                cnts++;
            }
            maxx=max(maxx,sum);
        }
        printf("Case #%d: %.9f\n",z++,maxx);
    }
}
