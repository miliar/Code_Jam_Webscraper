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

int f[4][N][N][N], g[4][N][N][N], gxx, p;

int dfs(int rest, vector<int> a)
{
    int cnt = a[0] + a[1] + a[2];
    if (cnt == 0) return 0;
    int& flag = g[rest][a[0]][a[1]][a[2]];
    int& ret = f[rest][a[0]][a[1]][a[2]];
    if (flag == gxx) return ret;
    flag = gxx;
    ret = -inf;
    if (a[0] > 0) {
        --a[0];
        ret = max(ret, dfs((rest - 1 + p) % p, a) + (rest == 0));
        ++a[0];
    }
    if (a[1] > 0) {
        --a[1];
        ret = max(ret, dfs((rest - 2 + p) % p, a) + (rest == 0));
        ++a[1];
    }
    if (a[2] > 0) {
        --a[2];
        ret = max(ret, dfs((rest - 3 + p) % p, a) + (rest == 0));
        ++a[2];
    }
    return ret;
}

void work()
{
    ++gxx;
    int n, ans = 0;
    cin >> n >> p;
    vector<int> j;
    for (int i = 0; i < 4; ++i)
        j.pb(0);
    for (int i = 1; i <= n; ++i)
    {
        int x;
        cin >> x;
        x %= p;
        if (x == 0) ++ans;
        else ++j[x - 1];
    }
    cout << dfs(0, j) + ans << endl;
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
