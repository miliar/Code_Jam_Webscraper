#include<bits/stdc++.h>
#define PB(u)  push_back(u)
#define AA   first
#define BB   second
#define inf 0x3f3f3f3f
using namespace std ;
#define MAX 100005
#define sz size()
typedef long long ll ;
typedef pair<int,int> PII ;
const double eps=1e-8;
const double pi=acos(-1.0);
const int mod=1e9+7;

double p[100];

int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int T,cas=1;
    cin>>T;
    while(T--)
    {
        int n,w;
        cin>>n>>w;
        double u;
        scanf("%lf",&u);
        for(int i=0;i<n;i++)
            scanf("%lf",&p[i]);
        double l=0,r=1;
        while(r-l>eps)
        {
            double m=(l+r)/2;
            double sum=0;
            for(int i=0;i<n;i++)
            {
                if(p[i]<m)
                    sum+=(m-p[i]);
            }
            if(sum>u)
                r=m;
            else
                l=m;
        }
        for(int i=0;i<n;i++)
            if(p[i]<l) p[i]=l;
        double ans=1;
        for(int i=0;i<n;i++)
            ans*=p[i];
        printf("Case #%d: %.10f\n",cas++,ans);
    }
    return 0 ;
}

