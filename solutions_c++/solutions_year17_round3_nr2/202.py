#include <bits/stdc++.h>

using namespace std;

#define _FILES
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef pair<int,int> pii;

const int MAXN = 1500;
const int INF = 1e9;

int dp[MAXN][MAXN][2];
bool p[MAXN][MAXN][2], canC[MAXN], canJ[MAXN];

int solve()
{
    int ac, aj, l, r, ans;
    cin>>ac>>aj;
    memset(canC,true,sizeof(canC));
    memset(canJ,true,sizeof(canJ));
    for (int i=0;i<ac;i++)
    {
        cin>>l>>r;
        for (int j=l;j<r;j++) canC[j] = false;
    }

    for (int i=0;i<aj;i++)
    {
        cin>>l>>r;
        for (int j=l;j<r;j++) canJ[j] = false;
    }
    for (int i=0;i<1440;i++)
    {
        for (int j=0;j<MAXN;j++) dp[i][j][0] = dp[i][j][1] = INF;
    }

    memset(p,false,sizeof(p));
    if (canC[0])
    {
        p[0][1][0] = true;
        dp[0][1][0] = 0;
    }

    if (canJ[0])
    {
        p[0][0][1] = true;
        dp[0][0][1] = 0;
    }

    for (int i=0;i<1440;i++)
    {
        for (int m=0;m<=720;m++)
        {
            if (p[i][m][0])
            {
                if (canC[i+1])
                {
                    p[i+1][m+1][0] = true;
                    dp[i+1][m+1][0] = min(dp[i+1][m+1][0],dp[i][m][0]);
                }

                if (canJ[i+1])
                {
                   p[i+1][m][1] = true;
                   dp[i+1][m][1] = min(dp[i+1][m][1],dp[i][m][0] + 1);
                }
            }

            if (p[i][m][1])
            {
                if (canC[i+1])
                {
                    p[i+1][m+1][0] = true;
                    dp[i+1][m+1][0] = min(dp[i+1][m+1][0], dp[i][m][1] + 1);
                }

                if (canJ[i+1])
                {
                   p[i+1][m][1] = true;
                   dp[i+1][m][1] = min(dp[i+1][m][1],dp[i][m][1]);
                }
            }
        }

    }
    ans = INF;
    if (p[1439][720][0]) ans = min(ans,dp[1439][720][0] + dp[1439][720][0]%2);
    if (p[1439][720][1]) ans = min(ans,dp[1439][720][1] + dp[1439][720][1]%2);
    return ans;
}
int main()
{
    ios_base::sync_with_stdio(false);

    #ifdef _FILES
        freopen("B-large.in","r",stdin);
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
