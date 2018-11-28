#include<bits/stdc++.h>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define ll long long
#define pil pair<int,ll>
#define pli pair<ll,int>
#define pll pair<ll,ll>
#define all(v) v.begin(),v.end()
#define inf 1000000000
double dp[1011][1011];
const double pi=acos(-1.0);
int main()
{
    freopen("inp.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cs=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,i,j,k;
        vector< pair<double,double> >v;
        scanf("%d %d",&n,&k);
        for(i=0; i<n; i++)
        {
            double r,h;
            scanf("%lf %lf",&r,&h);
            v.pb(mp(r,h));
        }
        sort(all(v));
        reverse(all(v));
        if(k==1)
        {
            double ans=0.0;
            for(i=0; i<n; i++)
                ans=max(ans,2*pi*v[i].f*v[i].s+pi*v[i].f*v[i].f);
            printf("Case #%d: %.10lf\n",cs,ans);
            cs++;
            continue;
        }
        for(i=0; i<=n; i++)
            for(j=0; j<=k; j++)
                dp[i][j]=0.0;
        dp[0][1]=2*pi*v[0].f*v[0].s+pi*v[0].f*v[0].f;
        for(i=1;i<n;i++)
        {
            for(j=1;j<=k;j++)
            {
                if(j==1)
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+2*pi*v[i].f*v[i].s+pi*v[i].f*v[i].f);
                else
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+2*pi*v[i].f*v[i].s);
            }
        }
        printf("Case #%d: %.10lf\n",cs,dp[n-1][k]);
        cs++;
    }
    return 0;
}
