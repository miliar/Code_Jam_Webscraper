//created by missever

#include<bits/stdc++.h>
#define MAX 1000000007
using namespace std;
typedef long long LL;
typedef pair<double,double> P;
P f[1005];

bool cmp(const P &a,const P &b)
{
    return a.first < b.first;
}

int main(){
    //freopen("A-large.in","r",stdin);
    //freopen("A-small-attempt.out","w",stdout);
    int t,n,d,i,j,k;
    scanf("%d",&t);
    for(int cas = 1;cas <= t; cas++)
    {
        scanf("%d%d",&d,&n);
        for(i = 0;i < n; i++) scanf("%lf%lf",&f[i].first,&f[i].second);
        sort(f,f + n,cmp);
        double T = 0.0;
        double ans = -1;
        for(i = n - 1;i > 0; i--)
        {
            double e = 1e16;
            int x = -1;
            for(j = 0;j < i; j++)
            {
                if(f[j].second <= f[j + 1].second) continue;
                double u = (f[j + 1].first - f[j].first) / (f[j].second - f[j + 1].second);
                if(u < e && f[j].first + f[j].second * u <= d) e = u,x = j;
            }
            if(x == -1) break;
            else
            {
                T += e;
                for(j = 0,k = 0;j <= i; j++)
                {
                    if(j == x) continue;
                    f[k++] = P(f[j].first + f[j].second * e,f[j].second);
                }
            }
        }
        T += (d - f[0].first) / f[0].second;
        ans = d / T;
        printf("Case #%d: %.8f\n",cas,ans);
    }
    return 0;
}
