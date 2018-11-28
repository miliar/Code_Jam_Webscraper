#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <vector>
#include <queue>
#include <bitset>
#include <cmath>
#include <time.h>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stdlib.h>
#include <deque>
#include <iomanip>
#include <complex>

using namespace std;

typedef long long ll;
typedef long double ld;

#define TIME (clock() * 1.0 / CLOCKS_PER_SEC)
#define rand_int ((rand() << 15) | rand())

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;
const ll prime = 239;
const ll MOD = 1e9 + 7;
const ll INF = 1e18;
const int BIG = 1e9 + 239;
const int MAX_N = 1e5 + 1;
const int MAX_T = (1 << 18);
const int MAX_LOG = 19;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};
const int tw = 4;
const int M = 100;

int dp[tw][M][M];
int dp3[tw][M][M][M];
int dp4[tw][M][M][M][M];

void solve()
{
    int n, p;
    cin >> n >> p;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    vector<int> kol(p, 0);
    for (int i = 0; i < n; i++)
        kol[a[i] % p]++;
    if (p == 2)
    {
        dp[0][0][0] = 0;
        for (int i = 1; i < p; i++)
            dp[i][0][0] = -BIG;
        for (int t = 1; t <= n; t++)
        {
            for (int x = 0; x <= min(kol[0], t); x++)
            {
                int y = t - x;
                if (y > kol[1])
                    continue;
                for (int d = 0; d < p; d++)
                {
                    dp[d][x][y] = -BIG;
                    if (x > 0)
                        dp[d][x][y] = max(dp[d][x][y], (dp[d][x - 1][y] + (d == 0)));
                    if (y > 0)
                        dp[d][x][y] = max(dp[d][x][y], (dp[(d + 1) & 1][x][y - 1] + (d == 1)));
                }
            }
        }
        int ans = 1;
        for (int x = 0; x <= n; x++)
            if (x <= kol[0] && n - x <= kol[1])
                ans = max(dp[1][x][n - x], ans);
        for (int x = 0; x <= n; x++)
            if (x <= kol[0] && n - x <= kol[1])
                ans = max(dp[0][x][n - x], ans);
        cout << ans;
        return;
    }
    if (p == 3)
    {
        dp3[0][0][0][0] = 0;
        for (int i = 1; i < p; i++)
            dp3[i][0][0][0] = -BIG;
        for (int t = 1; t <= n; t++)
        {
            for (int x = 0; x <= t; x++)
            {
                for (int z = 0; z <= t - x; z++)
                {
                    int y = t - x - z;
                    if (!(x <= kol[0] && y <= kol[1] && z <= kol[2]))
                        continue;
                    for (int d = 0; d < p; d++)
                    {
                        dp3[d][x][y][z] = -BIG;
                        if (x > 0)
                            dp3[d][x][y][z] = max(dp3[d][x][y][z], (dp3[d][x - 1][y][z] + (d == 0)));
                        if (y > 0)
                            dp3[d][x][y][z] = max(dp3[d][x][y][z], dp3[(d + 2) % 3][x][y - 1][z] + (d == 1));
                        if (z > 0)
                            dp3[d][x][y][z] = max(dp3[d][x][y][z], (dp3[(d + 1) % 3][x][y][z - 1] + (d == 2)));
                    }
                }
            }
        }
        int ans = 1;
        for (int x = 0; x <= n; x++)
            for (int y = 0; y <= n - x; y++)
                if (x <= kol[0] && y <= kol[1] && n - x - y <= kol[2])
                    ans = max(dp3[1][x][y][n - x - y], ans);
        for (int x = 0; x <= n; x++)
            for (int y = 0; y <= n - x; y++)
                if (x <= kol[0] && y <= kol[1] && n - x - y <= kol[2])
                    ans = max(dp3[0][x][y][n - x - y], ans);
        for (int x = 0; x <= n; x++)
            for (int y = 0; y <= n - x; y++)
                if (x <= kol[0] && y <= kol[1] && n - x - y <= kol[2])
                    ans = max(dp3[2][x][y][n - x - y], ans);
        cout << ans;
        return;
    }
    if (p == 4)
    {
        dp4[0][0][0][0][0] = 0;
        for (int i = 1; i < p; i++)
            dp4[i][0][0][0][0] = -BIG;
        for (int t = 1; t <= n; t++)
        {
            for (int x = 0; x <= t; x++)
            {
                for (int z = 0; z <= t - x; z++)
                {
                    for (int u = 0; u <= t - x - z; u++)
                    {
                        int y = t - x - z - u;
                        if (!(x <= kol[0] && y <= kol[1] && z <= kol[2] && u <= kol[3]))
                            continue;
                        for (int d = 0; d < p; d++)
                        {
                            dp4[d][x][y][z][u] = -BIG;
                            if (x > 0)
                                dp4[d][x][y][z][u] = max(dp4[d][x][y][z][u], (dp4[d][x - 1][y][z][u] + (d == 0)));
                            if (y > 0)
                                dp4[d][x][y][z][u] = max(dp4[d][x][y][z][u], dp4[(d + 3) % 4][x][y - 1][z][u] + (d == 1));
                            if (z > 0)
                                dp4[d][x][y][z][u] = max(dp4[d][x][y][z][u], (dp4[(d + 2) % 4][x][y][z - 1][u] + (d == 2)));
                            if (u > 0)
                                dp4[d][x][y][z][u] = max(dp4[d][x][y][z][u], (dp4[(d + 1) % 4][x][y][z][u - 1] + (d == 3)));
                        }
                    }
                }
            }
        }
        int ans = 1;
        for (int x = 0; x <= n; x++)
            for (int y = 0; y <= n - x; y++)
                for (int z = 0; z <= n - x - y; z++)
                    if (x <= kol[0] && y <= kol[1] && z <= kol[2] && n - x - y - z <= kol[3])
                        ans = max(dp4[1][x][y][z][n - x - y - z], ans);

        for (int x = 0; x <= n; x++)
            for (int y = 0; y <= n - x; y++)
                for (int z = 0; z <= n - x - y; z++)
                    if (x <= kol[0] && y <= kol[1] && z <= kol[2] && n - x - y - z <= kol[3])
                        ans = max(dp4[2][x][y][z][n - x - y - z], ans);

        for (int x = 0; x <= n; x++)
            for (int y = 0; y <= n - x; y++)
                for (int z = 0; z <= n - x - y; z++)
                    if (x <= kol[0] && y <= kol[1] && z <= kol[2] && n - x - y - z <= kol[3])
                        ans = max(dp4[0][x][y][z][n - x - y - z], ans);
        for (int x = 0; x <= n; x++)
            for (int y = 0; y <= n - x; y++)
                for (int z = 0; z <= n - x - y; z++)
                    if (x <= kol[0] && y <= kol[1] && z <= kol[2] && n - x - y - z <= kol[3])
                        ans = max(dp4[3][x][y][z][n - x - y - z], ans);
        cout << ans;
        return;
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    //freopen("small_input.txt", "r", stdin);
    freopen("small_output.txt", "w", stdout);
    //cout << fixed << setprecision(15);
    //*
    cin.sync_with_stdio(0);
    int number_of_tests;
    cin >> number_of_tests;
    for (int z = 0; z < number_of_tests; z++)
    {
        cout << "Case #" << z + 1 << ": ";
        solve();
        cout << endl;
    }
    /**/
    /*
    int number_of_tests;
    scanf("%d", &number_of_tests);
    for (int z = 0; z < number_of_tests; z++)
    {
        cout << "Case #" << z + 1 << ": ";
        solve();
        cout << "\n";
    }
    /**/
    return 0;
}
