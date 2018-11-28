#include <cassert>
#include <cstdio>
#include <ctime>
#include <cstdlib>
#include <climits>
#include <cstddef>
#include <cctype>
#include <cmath>
#include <cstring>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <numeric>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <bitset>
#include <list>
#include <string>
#include <functional>
#include <utility>
using namespace std;
typedef long long llint;
int const N = 100;
double const INF = 1e13;
int e[N], s[N];
int g[N][N];
llint d[N][N];
double best[N][N];
void work(int n)
{
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            d[i][j] = g[i][j];
        }
    }
    for (int k = 0; k < n; ++k)
    {
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (d[i][k] == -1 || d[k][j] == -1)
                {
                    continue;
                }
                llint cur = d[i][k] + d[k][j];
                if (d[i][j] == -1 || d[i][j] > cur)
                {
                    d[i][j] = cur;
                }
            }
        }
    }
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (d[i][j] == -1)
            {
                best[i][j] = INF;
            }
            else if (e[i] >= d[i][j])
            {
                best[i][j] = 1.0 * d[i][j] / s[i];
            }
            else
            {
                best[i][j] = INF;
            }
        }
    }
    for (int k = 0; k < n; ++k)
    {
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                best[i][j] = min(best[i][j], best[i][k] + best[k][j]);
            }
        }
    }
}
int main()
{
    ios_base::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for (int cc = 1; cc <= tc; ++cc)
    {
        int n, q;
        cin >> n >> q;
        for (int i = 0; i < n; ++i)
        {
            cin >> e[i] >> s[i];
        }
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                cin >> g[i][j];
                if (i == j) {
                    g[i][j] = 0;
                }
            }
        }
        work(n);
        vector<double> ans;
        int u, v;
        while (q--)
        {
            cin >> u >> v;
            ans.push_back(best[u - 1][v - 1]);
        }
        cout << "Case #" << cc << ":";
        for (size_t i = 0; i < ans.size(); ++i)
        {
            cout << " " << fixed << setprecision(6) << ans[i];
        }
        cout << "\n";
    }
    return 0;
}
