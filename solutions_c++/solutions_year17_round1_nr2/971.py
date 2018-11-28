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
pair<int, int> f(int r, int pg)
{
  pair<int, int> ret(0, -1);
  for (int cur = r, i = 1; ; cur += r, ++i)
  {
    if (cur - cur / 10 <= pg && cur + cur / 10 >= pg)
    {
      if (ret.first == 0)
      {
        ret.first = i;
      }
      ret.second = i;
    }
    if (cur - cur / 10 > pg)
    {
      break;
    }
  }
  return ret;
}
int solve(const vector<pair<int, int>> &v1, const vector<pair<int, int>> &v2)
{
  vector<size_t> a(v1.size());
  for (auto i = 0; i < v1.size(); ++i)
  {
    a[i] = i;
  }
  int ret = -1;
  do
  {
    int cur = 0;
    for (auto i = 0; i < v1.size(); ++i)
    {
      if (v1[a[i]].second < v2[i].first || v1[a[i]].first > v2[i].second)
      {
        continue;
      }
      cur += 1;
    }
    ret = max(ret, cur);
  } while (next_permutation(a.begin(), a.end()));
  return ret;
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
    vector<int> r(n);
    for (int i = 0; i < n; ++i)
    {
      cin >> r[i];
    }
    vector<vector<int>> packages(n, vector<int>(p));
    vector<vector<pair<int, int>>> bd(n, vector<pair<int, int>>(p));
    for (int i = 0; i < n; ++i)
    {
      for (int j = 0; j < p; ++j)
      {
        cin >> packages[i][j];
        bd[i][j] = f(r[i], packages[i][j]);
      }
    }
    int res;
    if (n == 1)
    {
      res = count_if(
          bd[0].begin(),
          bd[0].end(),
          [](const pair<int, int> &pr)
          {
            return pr.first <= pr.second;
          });
    }
    else
    {
      res = solve(bd[0], bd[1]);
    }
    cout << "Case #" << cc << ": " << res << endl;
  }
  return 0;
}
