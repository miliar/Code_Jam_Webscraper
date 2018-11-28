#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;
const int MAXN = 105;

int MOD;
int dp[MAXN][MAXN][MAXN][4];

int solve(int a[], int rem)
{
    //DEBUG(a[1]);
    //DEBUG(a[2]);
    //DEBUG(a[3]);

    if (a[1] + a[2] + a[3] == 0) return 0;
    if (dp[ a[1] ][ a[2] ][ a[3] ][ rem ] == -1)
    {
        int res = (rem == 0) ? 1 : 0;
        int x = 0;

        for (int i = 1; i < MOD; i++)
        {
            if (a[i] == 0) continue;
            a[i]--;
            int rem2 = (MOD + rem - i) % MOD;
            x = max(x, solve(a, rem2));
            a[i]++;
        }

        dp[ a[1] ][ a[2] ][ a[3] ][ rem ] = res + x;
    }

    return dp[ a[1] ][ a[2] ][ a[3] ][ rem ];
}

int main()
{
    freopen("inputA.in" , "r" , stdin );
    freopen("outputA.out" , "w" , stdout );

    int T;
    cin >> T;

    for (int _t = 1 ; _t <= T; _t++ )
    {
        int N;
        cin >> N >> MOD;

        int M = N + 1;
        for (int i = 0; i < M * M * M; i++)
        {
            int t = i;
            int x = t % M; t /= M;
            int y = t % M; t /= M;
            int z = t % M; t /= M;

            dp[x][y][z][0] = -1;
            dp[x][y][z][1] = -1;
            dp[x][y][z][2] = -1;
            dp[x][y][z][3] = -1;
        }

        int a[4] = {0, 0, 0, 0};
        int ans = 0;
        for (int i = 0; i < N; i++)
        {
            int g;
            cin >> g;
            g %= MOD;

            if (g == 0)
            {
                ans++;
            }
            else
            {
                a[g]++;
            }
        }

        cout << "Case #" << _t << ": " << ans + solve(a, 0) << endl;
    }

    return 0;
}
