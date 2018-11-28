#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <ctime>
#include <iomanip>
#include <bitset>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const int N = 101;
const int inf = 100000000;

int H, A, HH, AA, B, D;
int tt;
int f[N][N][N][N], g[N][N][N][N];

int dp(int h, int hh, int a, int aa)
{
    if (hh <= 0) return 0;
    if (h <= 0) return inf;

    int &ret = f[h][hh][a][aa];
    int &flag = g[h][hh][a][aa];
    if (flag == tt) return ret;
    flag = tt;
    ret = inf;

    //attack
    ret = min(ret, dp(h - aa, hh - a, a, aa) + 1);

    //buff
    if (B > 0)
        ret = min(ret, dp(h - aa, hh, min(a + B, HH), aa) + 1);

    //cure
    ret = min(ret, dp(H - aa, hh, a, aa) + 1);

    //debuff
    if (D > 0)
        ret = min(ret, dp(h - max(aa - D, 0), hh, a, max(aa - D, 0)) + 1);

    return ret;
}

void work()
{
    cin >> H >> A >> HH >> AA >> B >> D;
    ++tt;
    int ans = dp(H, HH, A, AA);
    if (ans >= inf) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
}

int main()
{
    #ifdef LOCAL_TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ": ";
        work();
    }

    return 0;
}
