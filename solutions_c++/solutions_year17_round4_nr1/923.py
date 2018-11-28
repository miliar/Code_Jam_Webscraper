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
int g[N];
int best[N + 1][N + 1][N + 1][4];
int f(int numLeft, int gs)
{
    return (numLeft - gs + 4) % 4;
}
int solve(int n)
{
    int num[4] = {0, 0, 0, 0};
    for (int i = 0; i < n; ++i)
    {
        ++num[g[i] % 4];
    }
    for (int i = 0; i <= num[1]; ++i)
    {
        for (int j = 0; j <= num[2]; ++j)
        {
            for (int k = 0; k <= num[3]; ++k)
            {
                for (int p = 0; p < 4; ++p)
                {
                    best[i][j][k][p] = i + j + k > 0 ? INT_MAX : 0;
                }
            }
        }
    }
    for (int i = 0; i <= num[1]; ++i)
    {
        for (int j = 0; j <= num[2]; ++j)
        {
            for (int k = 0; k <= num[3]; ++k)
            {
                if (i + j + k == 0)
                {
                    continue;
                }
                for (int p = 0; p < 4; ++p)
                {
                    if (i > 0)
                    {
                        best[i][j][k][p] = min(best[i][j][k][p], (p != 0 ? 1 : 0) + best[i - 1][j][k][f(p, 1)]);
                    }
                    if (j > 0)
                    {
                        best[i][j][k][p] = min(best[i][j][k][p], (p != 0 ? 1 : 0) + best[i][j - 1][k][f(p, 2)]);
                    }
                    if (k > 0)
                    {
                        best[i][j][k][p] = min(best[i][j][k][p], (p != 0 ? 1 : 0) + best[i][j][k - 1][f(p, 3)]);
                    }
                }
            }
        }
    }
    return n - best[num[1]][num[2]][num[3]][0];
}
int main()
{
    ios_base::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for (int cc = 1; cc <= tc; ++cc)
    {
        int n, p;
        cin >> n >> p;
        for (int i = 0; i < n; ++i)
        {
            cin >> g[i];
        }
        int res;
        if (p == 2)
        {
            int s = 0;
            for (int i = 0; i < n; ++i)
            {
                if (g[i] % 2 != 0)
                {
                    ++s;
                }
            }
            res = n - s / 2;
        }
        else if (p == 3)
        {
            int n1 = 0;
            int n2 = 0;
            for (int i = 0; i < n; ++i)
            {
                if (g[i] % 3 == 1)
                {
                    ++n1;
                }
                else if (g[i] % 3 == 2)
                {
                    ++n2;
                }
            }
            int s = min(n1, n2);
            for (int i = 0; i < max(n1, n2) - min(n1, n2); ++i)
            {
                if (i % 3 != 0)
                {
                    ++s;
                }
            }
            res = n - s;
        }
        else
        {
            res = solve(n);
        }
        cout << "Case #" << cc << ": " << res << "\n";
    }
    return 0;
}
