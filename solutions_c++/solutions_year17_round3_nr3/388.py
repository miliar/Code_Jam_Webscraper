#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
const double eps=1e-8;
const int mod=1e9+7;
const double pi=acos(-1.0);
const int N=1e5+5;
const int M=100;

double p[55];
int main()
{
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("C-small-1-attempt0.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        printf("Case #%d: ", ca++);
        int n, k;
        double u;
        scanf("%d%d%lf", &n, &k, &u);
        for(int i=0;i<n;i++)
            scanf("%lf", &p[i]);
        sort(p, p+n);
        p[n]=1.0;
        while(fabs(u)>eps)
        {
            for(int i=1;i<=n;i++)
            {
                if(p[i]!=p[i-1])
                {
                    double c=p[i]-p[i-1];
                    double d=min(c*i,u);
                    u-=d;
                    for(int j=0;j<i;j++)
                        p[j]+=d/i;
                    break;
                }
            }
        }
        double ans=1;
        for(int i=0;i<n;i++)
            ans*=p[i];
        printf("%.6f\n", ans);
    }
    return 0;
}

