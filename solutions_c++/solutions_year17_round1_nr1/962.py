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
void solve(int r, int c, vector<string> &cake)
{
  for (int i = 0; i < r; ++i)
  {
    if (count(cake[i].begin(), cake[i].end(), '?') == c)
    {
      continue;
    }
    char last = '?';
    for (int j = 0; j < c; ++j)
    {
      if (cake[i][j] == '?')
      {
        continue;
      }
      for (int k = j - 1; k >= 0 && cake[i][k] == '?'; --k)
      {
        cake[i][k] = cake[i][j];
      }
      last = cake[i][j];
    }
    for (int j = c - 1; j >= 0 && cake[i][j] == '?'; --j)
    {
      cake[i][j] = last;
    }
  }
  string last = "";
  for (int i = 0; i < r; ++i)
  {
    if (count(cake[i].begin(), cake[i].end(), '?') == c)
    {
      continue;
    }
    for (int j = i - 1; j >= 0 && count(cake[j].begin(), cake[j].end(), '?') == c; --j)
    {
      cake[j] = cake[i];
    }
    last = cake[i];
  }
  for (int i = r - 1; i >= 0; --i)
  {
    if (count(cake[i].begin(), cake[i].end(), '?') == c)
    {
      cake[i] = last;
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
    int r, c;
    cin >> r >> c;
    vector<string> cake(r);
    for (int i = 0; i < r; ++i)
    {
      cin >> cake[i];
    }
    solve(r, c, cake);
    cout << "Case #" << cc << ": \n";
    copy(cake.begin(), cake.end(), ostream_iterator<string>(cout, "\n"));
  }
  return 0;
}
