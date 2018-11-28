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
const int INF = INT_MAX >> 2;
const int V = 100;
int hd, ad, hk, ak, b, d;
int best[V + 1][V + 1][V + 1][V + 1];
int f(int hd_, int ad_, int hk_, int ak_)
{
  if (best[hd_][ad_][hk_][ak_] != -1)
  {
    return best[hd_][ad_][hk_][ak_];
  }
  int& ret = best[hd_][ad_][hk_][ak_];
  ret = INF;
  // win now
  if (ad_ >= hk_)
  {
    return ret = 1;
  }
  // debuff
  if (d != 0 && ak_ != 0 && max(ak_ - d, 0) < hd_)
  {
    ret = min(ret, 1 + f(hd_ - max(ak_ - d, 0), ad_, hk_, max(ak_ - d, 0)));
  }
  // buff
  if (b != 0 && ak_ < hd_)
  {
    ret = min(ret, 1 + f(hd_ - ak_, min(ad_ + b, hk), hk_, ak_));
  }
  // attack
  if (ak_ < hd_)
  {
    ret = min(ret, 1 + f(hd_ - ak_, ad_, hk_ - ad_, ak_));
  }
  // cure
  if (hd - ak_ > 0)
  {
    ret = min(ret, 1 + f(hd - ak_, ad_, hk_, ak_));
  }
  return ret;
}
int solve()
{
  for (int i = 0; i <= V; ++i)
  {
    for (int j = 0; j <= V; ++j)
    {
      for (int k = 0; k <= V; ++k)
      {
        for (int l = 0; l <= V; ++l)
        {
          best[i][j][k][l] = -1;
        }
      }
    }
  }
  return f(hd, ad, hk, ak);
}
int main()
{
  ios_base::sync_with_stdio(false);
  int tc;
  cin >> tc;
  for (int cc = 1; cc <= tc; ++cc)
  {
    cin >> hd >> ad >> hk >> ak >> b >> d;
    int res = solve();
    cout << "Case #" << cc << ": ";
    if (res >= INF)
    {
      cout << "IMPOSSIBLE";
    }
    else
    {
      cout << res;
    }
    cout << endl;
  }
  return 0;
}
