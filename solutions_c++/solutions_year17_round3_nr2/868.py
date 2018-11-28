#include <bits/stdc++.h>
using namespace std;

#define in cin
#define out cout

#define REP(i,n) for(int i=0; i<n; i++)
#define REP2(i,s,e) for(int i=s; i<e; i++)
#define REPD(i,s,e,d) for(int i=s; i<=e; i+=d)
#define REPE(i,s,e) for(int i=s; i<=e; i++)
#define REPR(i,s,e) for(int i=s; i>=e; i--)

#define all(v) v.begin(), v.end()
#define pb push_back

#define ll long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define rd(n) scanf("%d", &n)

#define x first
#define y second
#define intINF 2147483647
#define llINF 9223372036854775807LL
#define MOD 1000000007

#define DAY 1440

int act[2][DAY];
int dp[2][DAY][DAY/2+2];

int start = 0;

int f(int who, int time, int Aspend)
{
    if(Aspend > DAY/2) return 1e6;

    if(time == DAY-1)
    {
        if(Aspend == DAY/2) return who != start;
        else return 1e6;
    }

    if(dp[who][time][Aspend] != -1) return dp[who][time][Aspend];
    if(act[who][time]) return 1e6;

    int t2 = f(who, time+1, Aspend + (who==0?1:0));
    int t1 = f(!who, time+1, Aspend + (who==0?0:1)) + 1;

    return dp[who][time][Aspend] = min(t1, t2);
}

void solve(int tc)
{
    int n, m; cin >> n >> m;

    memset(act, 0, sizeof(act));

    for(int i=0; i<n; i++)
    {
        int p, q; cin >> p >> q;
        for(int j=p; j<q; j++) act[0][j] = 1;
    }
    for(int i=0; i<m; i++)
    {
        int p, q; cin >> p >> q;
        for(int j=p; j<q; j++) act[1][j] = 1;
    }

    memset(dp, -1, sizeof(dp));
    start = 0;
    int t1 = f(0, 0, 1);

    memset(dp, -1, sizeof(dp));
    start = 1;
    int t2 = f(1, 0, 0);

    printf("Case #%d: %d\n", tc, min(t1, t2));
}

int main()
{
#ifndef ONLINE_JUDGE
     freopen("in.txt", "r", stdin);
     freopen("out.txt", "w", stdout);
#endif

    int tc; scanf("%d", &tc);
    for(int i=1; i<=tc; i++) solve(i);


    return 0;
}
