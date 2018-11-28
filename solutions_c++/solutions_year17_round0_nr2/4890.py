#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int maxn = 20;

int dp[maxn][maxn][2];

string n;
int sz;

bool go(int ind, int d, bool f)
{
    if (dp[ind][d][f] != -1) return dp[ind][d][f];
    if (ind == sz - 1) return dp[ind][d][f] = 1;
    dp[ind][d][f] = 0;
    if (f)
    {
        if (n[ind + 1] >= d)
            dp[ind][d][f] |= go(ind + 1, n[ind + 1], 1);
        for (int nx = d; nx < n[ind + 1]; ++nx) dp[ind][d][f] |= go(ind + 1, nx, 0);
    }
    else
    {
        for (int nx = d; nx < 10; ++nx) dp[ind][d][f] |= go(ind + 1, nx, 0);
    }
    return dp[ind][d][f];
}

void take (int ind, int d, bool f, string &res)
{
    res += d + '0';
    if (ind == sz - 1) return;
    if (f)
    {
        if (dp[ind + 1][n[ind + 1]][1]){
            take(ind + 1, n[ind + 1], 1, res);
            return;
        }
        for (int nx = n[ind + 1] - 1; nx >= d; --nx)
        {
            if (dp[ind + 1][nx][0] == 1)
            {
                take(ind + 1, nx, 0, res);
                break;
            }
        }
    }
    else
    {
        for (int nx = 9; nx >= d; --nx)
        {
            if (dp[ind + 1][nx][0])
                take(ind + 1, nx, 0, res);
            break;
        }
    }
}

void solve(int x)
{
    memset(dp, -1, sizeof dp);

    cin >> n;
    sz = n.size();

    for (int i = 0; i < (int)n.size(); ++i) n[i] -= '0';

    for (int d = n[0]; d >= 0; --d)
        go(0, d, d == n[0]);

    string res;
    for (int d = 9; d >= 0; --d)
    {
        if (dp[0][d][0] == 1)
        {
            take(0, d, 0, res);
            break;
        }

        if (dp[0][d][1] == 1)
        {
            take(0, d, 1, res);
            break;
        }
    }

    cout << "Case #" << x << ": ";
    bool ok = false;
    for (int i = 0; i < (int)res.size(); ++i)
    {
        if (!ok)
        {
            if (res[i] == '0') continue;
            else
            {
                cout << res[i];
                ok = true;
            }
        }
        else
            cout << res[i];
    }
    if (!ok) cout << 0;
    cout << '\n';
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
        solve(i);
    return 0;
}
