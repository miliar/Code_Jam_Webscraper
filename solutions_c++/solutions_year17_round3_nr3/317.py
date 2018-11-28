#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>

using namespace std;
#define maxm  100005
#define maxn 10000
#define INF  10000
const double pi=acos(-1.0);
#define eps 1e-8
double p[maxn];

bool dcmp(double x)
{
    if(fabs(x)<eps) return 1;
    return 0;
}
int main()
{
    freopen("C-small-1-attempt0.in","r",stdin);
    freopen("C-small-1-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {

        int n,k;
        scanf("%d%d",&n,&k);
        double U;
        scanf("%lf",&U);
        for(int i=0;i<n;i++) scanf("%lf",p+i);

        sort(p,p+n);
        while(U>eps)
        {
            int i;
            for(i=1;i<n;i++)
            {
                if(dcmp(p[i]-p[i-1])==0) break;
            }
            if(i==n)
            {
                double te=U/n;
                for(int j=0;j<n;j++) p[j]+=te;
                break;
            }
            else
            {
                double t=(p[i]-p[i-1])*i;
                if(t>U)
                {
                    t=U/i;
                    for(int j=0;j<i;j++) p[j]+=t;
                    break;
                }
                else
                {
                    U-=t;
                    for(int j=0;j<i;j++) p[j]=p[i];
                }
            }
        }
        for(int i=1;i<n;i++)
        {
            //cout<<p[i]<<endl;
            p[0]*=p[i];
        }
        printf("Case #%d: %.20f\n",cas,p[0]);
    }
}
