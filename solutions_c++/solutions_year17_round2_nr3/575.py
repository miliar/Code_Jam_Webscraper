/*
 * Author: Vladislav Belov
 */
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

void solution();

int main()
{
    ios::sync_with_stdio(false);
#ifdef HOME
    freopen("C.in", "rt", stdin);
    freopen("C2.out", "wt", stdout);
    clock_t start = clock();
#endif
    solution();
#ifdef HOME
    cerr << "Total time: " << fixed << setprecision(3) << double(clock() - start) / double(CLOCKS_PER_SEC) << endl;
#endif
    return EXIT_SUCCESS;
}

typedef long long ll;
#define int ll

#define N 128
#define Q 128
#define INF 1e18
#define EPS 1e-9
int n, q, e[N], s[N], g[N][N];
int from[Q], to[Q];

char u[N];
double g2[N][N], l[N];

void solve()
{
    for (int k = 0; k < n; ++k)
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
            {
                if (g[i][k] == -1 || g[k][j] == -1 || i == j)
                    continue;
                int value = g[i][k] + g[k][j];
                if (g[i][j] == -1 || g[i][j] > value)
                    g[i][j] = value;
            }
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
        {
            g2[i][j] = -1.0;
            if (g[i][j] == -1 || i == j)
                continue;
            if (e[i] >= g[i][j])
                g2[i][j] = double(g[i][j]) / double(s[i]);
        }
    for (int t = 0; t < q; ++t)
    {
        for (int i = 0; i < n; ++i)
            u[i] = 0, l[i] = INF;
        l[from[t]] = 0;
        for (;;)
        {
            int index = -1;
            for (int i = 0; i < n; ++i)
            {
                if (u[i])
                    continue;
                if (index == -1 || l[index] > l[i])
                    index = i;
            }
            if (index == -1)
                break;
            u[index] = 1;
            for (int i = 0; i < n; ++i)
            {
                if (g[index][i] == -1 || g2[index][i] < 0.0 || i == index)
                    continue;
                l[i] = min(l[i], l[index] + g2[index][i]);
            }
        }
        cout << " " << setprecision(9) << fixed << l[to[t]];
    }
}

void solution()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; ++t)
    {
        cerr << t + 1 << endl;
        cout << "Case #" << t + 1 << ":";
        cin >> n >> q;
        for (int i = 0; i < n; ++i)
            cin >> e[i] >> s[i];
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j)
                cin >> g[i][j];
        for (int i = 0; i < q; ++i)
        {
            cin >> from[i] >> to[i];
            --from[i];
            --to[i];
        }
        solve();
        cout << '\n';
    }
}
