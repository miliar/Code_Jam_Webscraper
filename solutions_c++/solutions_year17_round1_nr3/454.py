#include <bits/stdc++.h>
#define last ost
#define next nst

using namespace std;

const int MaxN = 100 + 1;
const int INF = 1e9;

bool used[MaxN][MaxN][MaxN][MaxN];
int dp[MaxN][MaxN][MaxN][MaxN];

int B, DDD, Hd, Hk, Ad, Ak;

int rec(int H, int D, int h, int d)
{

    if(used[H][D][h][d])
        return dp[H][D][h][d];

    dp[H][D][h][d] = INF;
    used[H][D][h][d] = true;

    {
        int hh = h - D;
        if(hh < 1)
            dp[H][D][h][d] = min(dp[H][D][h][d], 1);
        else
        {
            int HH = H - d;
            if(HH > 0)
                dp[H][D][h][d] = min(dp[H][D][h][d], 1 + rec(HH, D, hh, d));
        }
    }

    if(D + B <= 100)
    {
        int hh = h;
        int HH = H - d;
        if(HH > 0)
            dp[H][D][h][d] = min(dp[H][D][h][d], 1 + rec(HH, D + B, hh, d));
    }

    if(H < Hd)
    {
        int hh = h;
        int HH = Hd - d;
        if(HH > 0)
            dp[H][D][h][d] = min(dp[H][D][h][d], 1 + rec(HH, D, hh, d));
    }

    if(d > 0)
    {
        int dd = max(d - DDD, 0);
        int hh = h;
        int HH = H - dd;
        if(HH > 0)
            dp[H][D][h][d] = min(dp[H][D][h][d], 1 + rec(HH, D, hh, dd));
    }

    return dp[H][D][h][d];
}

void solve(int CASE)
{
    cout << "CASE #" << CASE << ": ";

    memset(used, 0, sizeof(used));

    cin >> Hd >> Ad >> Hk >> Ak >> B >> DDD;
    int ans = rec(Hd, Ad, Hk, Ak);

    if(ans == INF)
        cout << "IMPOSSIBLE\n";
    else
        cout << ans << '\n';
    return;
}

main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    for(int t1 = 1; t1 <= t; ++t1)
        solve(t1);
    return 0;
}
