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
int const N = 1000;
int n, c, m;
vector <pair <int, int> > tickets;
int nl, nr;
bool g[N][N];
int l[N], r[N];
bool visited[N];
int mm[N];
int ul[N + 1], ur[N + 1];
int numRide, numPromo;
void readin()
{
    cin >> n >> c >> m;
    tickets.resize(m);
    for (int i = 0; i < m; ++i)
    {
        cin >> tickets[i].first >> tickets[i].second;
    }
}
bool dfs(int u)
{
    if (visited[u])
    {
        return false;
    }
    visited[u] = true;
    for (int v = 0; v < nr; ++v)
    {
        if (!g[u][v])
        {
            continue;
        }
        if (mm[v] == -1 || dfs(mm[v]))
        {
            mm[v] = u;
            return true;
        }
    }
    return false;
}
int match()
{
    int ret = 0;
    memset(mm, -1, sizeof(mm));
    for (int i = 0; i < nl; ++i)
    {
        memset(visited, false, sizeof(visited));
        if (dfs(i))
        {
            ++ret;
        }
    }
    return ret;
}
void solve()
{
    sort(tickets.begin(), tickets.end());
    nl = 0;
    nr = 0;
    for (int i = 0; i < m; ++i)
    {
        if (tickets[i].second == 1)
        {
            l[nl++] = tickets[i].first;
        }
        else
        {
            r[nr++] = tickets[i].first;
        }
    }
    memset(g, false, sizeof(g));
    for (int i = 0; i < nl; ++i)
    {
        for (int j = 0; j < nr; ++j)
        {
            if (l[i] != r[j])
            {
                g[i][j] = true;
            }
        }
    }
    numRide = match();
    numPromo = 0;
    memset(ul, 0, sizeof(ul));
    memset(ur, 0, sizeof(ur));
    for (int i = 0; i < nl; ++i)
    {
        ++ul[l[i]];
    }
    for (int j = 0; j < nr; ++j)
    {
        if (mm[j] == -1)
        {
            ++ur[r[j]];
        }
        else
        {
            --ul[l[mm[j]]];
        }
    }
    int zl = count_if(ul, ul + (n + 1), bind2nd(greater <int>(), 0));
    int zr = count_if(ur, ur + (n + 1), bind2nd(greater <int>(), 0));
    if (zl == 0)
    {
        numRide += accumulate(ur, ur + (n + 1), 0);
        return;
    }
    else if (zr == 0)
    {
        numRide += accumulate(ul, ul + (n + 1), 0);
        return;
    }
    assert(zl == 1 && zr == 1);
    int x = -1, y = -1;
    for (int i = 1; i <= n; ++i)
    {
        if (ul[i] > 0)
        {
            x = i;
        }
        if (ur[i] > 0)
        {
            y = i;
        }
    }
    if (x == -1 && y == -1)
    {
    }
    else if (x == -1)
    {
        numRide += ur[y];
    }
    else if (y == -1)
    {
        numRide += ul[x];
    }
    else
    {
        assert(x == y);
        if (x == 1)
        {
            numRide += ul[x] + ur[y];
        }
        else
        {
            numRide += max(ul[x], ur[y]);
            numPromo += min(ul[x], ur[y]);
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
        readin();
        solve();
        cout << "Case #" << cc << ": " << numRide << " " << numPromo << "\n";
    }
    return 0;
}
