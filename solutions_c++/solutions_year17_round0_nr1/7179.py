#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <cstring>

using namespace std;

const int N = 1020;

int x[N][N];
int K, n;

void init()
{
  string s;
  cin >> s >> K;
  n = s.length();
  memset(x, 0, sizeof(x));
  for (int i=0; i<n; ++i)
  {
    for (int j=max(i-K+1, 0); j<=min(i, n-K); ++j)
      x[i][j] = 1;
    x[i][n] = (s[i] == '-');
  }
}

void work()
{
  for (int i=0; i<n; ++i)
  {
    int m = 0;
    for (int j=0; j<n; ++j)
      if (x[i][j] > 0)
      {
        m = i;
        break;
      }
    if (x[i][m] == 0)
      continue;
    for (int j=0; j<n; ++j)
      if (j!=i && x[j][m] == 1)
      {
        for (int k=0; k<=n; ++k)
          x[j][k] ^= x[i][k];
      }
  }
  // Check possibility
  bool ok = true;
  int sum = 0;
  for (int i=0; i<n; ++i)
  {
    if (x[i][n] == 0)
      continue;
    ++sum;
    bool hasone = false;
    for (int j=0; j<n; ++j)
      if (x[i][j] == 1)
      {
        hasone = true;
        break;
      }
    if (!hasone)
      ok = false;
  }
  if (!ok)
    cout << "IMPOSSIBLE" << endl;
  else
    cout << sum << endl;
}

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int T;
  cin >> T;
  for (int i=1; i<=T; ++i)
  {
    cout << "Case #" << i << ": ";
    init();
    work();
  }
}
