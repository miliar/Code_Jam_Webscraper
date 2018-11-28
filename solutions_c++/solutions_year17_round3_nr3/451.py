
#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

#define MEM(a,x) memset(a,x,sizeof a)
#define eps 1e-8
#define MOD 10009
#define MAXN 10010
#define MAXM 100010
#define INF 99999999
#define ll long long
#define bug cout<<"here"<<endl
#define fread freopen("C-small-1-attempt0.in","r",stdin)
#define fwrite freopen("out.txt","w",stdout)

using namespace std;

int sig(double x) {return (x>eps) - (x<-eps);}
int n,k;
double u;
double p[60];

int main()
{
//    fread;
//    fwrite;
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++)
    {
        scanf("%d%d",&n,&k);
        scanf("%lf",&u);
        double pro=0.0;
        for(int i=0;i<n;i++)
            scanf("%lf",&p[i]),
            pro+=p[i];
        pro+=u;
        printf("Case #%d: ",t);
        if(sig(pro/n-1.0)>=0)
        {

            printf("%lf\n",1.0);
            continue;
        }
        double l=0.0,r=1.0,m;
        for(int z=0;z<1000;z++)
        {
            m=(l+r)*0.5;
            double x=0.0;
            for(int i=0;i<n;i++)
                x+=max(0.0,m-p[i]);
            if(sig(x-u)<0) l=m;
            else r=m;
        }
        double ans=1.0;
        for(int i=0;i<n;i++)
            ans*=max(r,p[i]);
        printf("%.8lf\n",ans);
    }

    return 0;
}

