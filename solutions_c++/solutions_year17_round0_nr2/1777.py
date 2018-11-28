#include <bits/stdc++.h>

using namespace std;

#define _FILES
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef pair<int,int> pii;

ll dp[25][10][2];

ll getCount(ll n)
{
    ll ans;
    memset(dp,0,sizeof(dp));
    dp[0][9][0] = 1;
    for (int i=1;i<25;i++)
    {
        //<
        for (int cur=0;cur<(n%10);cur++)
        {
            for (int prev=cur;prev<10;prev++)
            {
                dp[i][cur][0] += dp[i-1][prev][0]+dp[i-1][prev][1];
            }
        }

        //==
        for (int prev=(n%10);prev<10;prev++)
        {
            dp[i][n%10][0] += dp[i-1][prev][0];
            dp[i][n%10][1] += dp[i-1][prev][1];
        }

        //>
        for (int cur=(n%10)+1;cur<10;cur++)
        {
            for (int prev=cur;prev<10;prev++)
            {
                dp[i][cur][1] += dp[i-1][prev][0]+dp[i-1][prev][1];
            }
        }

        n /= 10;
    }
    ans = 0;
    for (int i=0;i<10;i++) ans+=dp[24][i][0];
    --ans;
    return ans;
}

ll solve()
{
    ll n,lg,rg,mid,c;
    cin>>n;
    c = getCount(n);
    lg = 1;
    rg = n;
    while (rg-lg>1)
    {
        mid = (lg+rg)/2;
        if (getCount(mid)<c) lg = mid; else rg = mid;
    }
    return rg;
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
        cout<<"Case #"<<test<<": "<<solve()<<endl;
    }
    return 0;
}
