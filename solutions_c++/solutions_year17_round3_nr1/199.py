#include <bits/stdc++.h>

using namespace std;

#define _FILES
#define PB push_back
#define MP make_pair
#define M_PI  3.14159265358979323846

typedef long long ll;
typedef pair<int,int> pii;

const int MAXN = 1005;
long long dp[MAXN][MAXN][2];
pair<ll,ll> pancakes[MAXN];

double solve()
{
    int n,k;
    ll ans;
    cin>>n>>k;
    memset(dp,0,sizeof(dp));
    for (int i=0;i<n;i++)
    {
        cin>>pancakes[i].first>>pancakes[i].second;
    }
    sort(pancakes, pancakes + n);
    dp[0][1][1] = 2*pancakes[0].first*pancakes[0].second;
    for (int i=0;i<n-1;i++)
    {
        for (int cur=0;cur<=k;cur++)
        {
            if ((!dp[i][cur])&&(cur)) continue;
            dp[i+1][cur][0] = max(dp[i+1][cur][0],max(dp[i][cur][0],dp[i][cur][1]));
            dp[i+1][cur+1][1] = max(dp[i+1][cur+1][1],max(dp[i][cur][0],dp[i][cur][1])+2*pancakes[i+1].first*pancakes[i+1].second);
        }
    }
    ans = 0;
    for (int i=k-1;i<n;i++)
    {
        ans = max(ans, dp[i][k][1] + pancakes[i].first*pancakes[i].first);
    }

    return ans*M_PI;
}

int main()
{
    ios_base::sync_with_stdio(false);

    #ifdef _FILES
        freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif // _FILES
    int T;
    cin>>T;
    for (int test=1;test<=T;test++)
    {
        cout<<setprecision(8)<<fixed<<"Case #"<<test<<": "<<solve()<<endl;
    }

    return 0;
}
