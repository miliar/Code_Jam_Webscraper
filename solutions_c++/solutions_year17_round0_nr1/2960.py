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
int const INF = 0x3fffffff;
int solve_inner(int i, string &s, const int K)
{
    if (i + K - 1 == s.size())
    {
        return count(s.begin(), s.end(), '+') == s.size()
            ? 0
            : INF;
    }
    int c = 0;
    if (s[i] == '-')
    {
        for (int j = i; j < i + K; ++j)
        {
            s[j] = (s[j] == '-' ? '+' : '-');
        }
        c = 1;
    }
    return c + solve_inner(i + 1, s, K);
}
int solve(string &s, const int K)
{
    return solve_inner(0, s, K);
}
int main()
{
    ios_base::sync_with_stdio(false);
    int tc;
    cin >> tc;
    for (int cc = 1; cc <= tc; ++cc)
    {
        string s;
        int k;
        cin >> s >> k;
        int r = solve(s, k);
        cout << "Case #" << cc << ": ";
        if (r < INF)
        {
            cout << r << endl;
        }
        else
        {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
