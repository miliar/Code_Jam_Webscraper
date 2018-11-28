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
map<llint, map<llint, llint>> mc_hi;
map<llint, map<llint, llint>> mc_lo;
llint n, m;
pair<llint, llint> res;
void merge_(map<llint, llint> &x, map<llint, llint> &y)
{
    for (auto it = y.cbegin(); it != y.cend(); ++it)
    {
        x[it->first] += it->second;
    }
}
void f(llint c)
{
    if (c == 0)
    {
        return;
    }
    if (mc_hi.find(c) != mc_hi.end())
    {
        return;
    }
    f(c / 2);
    f((c - 1) / 2);
    mc_hi[c][c / 2] = 1;
    mc_lo[c][(c - 1) / 2] = 1;
    merge_(mc_hi[c], mc_hi[c / 2]);
    merge_(mc_hi[c], mc_hi[(c - 1) / 2]);
    merge_(mc_lo[c], mc_lo[c / 2]);
    merge_(mc_lo[c], mc_lo[(c - 1) / 2]);
}
llint g(const map<llint, llint> &mc, llint c)
{
    for (auto it = mc.crbegin(); it != mc.crend(); ++it)
    {
        if (it->second >= c)
        {
            return it->first;
        }
        c -= it->second;
    }
    return 0;
}
void solve()
{
    mc_hi.clear();
    mc_lo.clear();
    f(n);
    res.first = g(mc_hi[n], m);
    res.second = g(mc_lo[n], m);
}
int main()
{
    ios_base::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for (int cc = 1; cc <= tc; ++cc)
    {
        cin >> n >> m;
        solve();
        cout << "Case #" << cc << ": "
             << res.first << " " << res.second << endl;
    }
    return 0;
}
