// aarifshuvo   ``CSEJU

#include <bits/stdc++.h>
#define ll long long
#define pb push_back
#define SZ(x) ((int)(x).size())
#define scl(x) scanf("%lld", &x)
#define scll(x,y) scanf("%lld %lld", &x, &y)
#define all(x) (x).begin(),(x).end()
#define mem(a,d) memset(a,d,sizeof a)
#define REP(i,n) for(int i=0;i<n;i++)
#define REV(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define pri(a) cout<<a<<endl
#define prii(a,b) cout<<a<<" "<<b<<endl
using namespace std;

#define inf 12345678912

vector <int> digs;
ll n;
ll dp[19][3];

ll go(ll i, ll issmall, ll prev, ll sum)
{
    sum = sum*10 + prev;

    if(i==SZ(digs))
    {
        return sum;
    }

    if(dp[i][issmall]!=-1) return dp[i][issmall];

    ll hi = (issmall) ? 9:digs[i];

    dp[i][issmall] = 0;

    for(int j=hi; j>=0; j--)
    {
        if(prev<=j)
            dp[i][issmall] =max(dp[i][issmall], go(i+1, issmall|j<hi,j,sum));
    }
    return dp[i][issmall];
}

ll makeandgo(ll n)
{
    digs.clear();
    if(!n) digs.pb(0);

    while(n)
    {
        digs.pb(n%10);
        n/=10;
    }
    reverse(all(digs));

  //  REP(i,SZ(digs)) pri(digs[i]);
    mem(dp,-1);
    ll ans = go(0,0,0,0);
    return ans;
}


int main()
{
   freopen("D:/gjam17/inp.txt", "r" , stdin);
    freopen("D:/gjam17/out.txt", "w", stdout);

    ll t,cs=0;
    scl(t);
    while(t--)
    {
        scl(n);

        printf("Case #%lld: %lld\n", ++cs, makeandgo(n));
    }

    return 0;
}
