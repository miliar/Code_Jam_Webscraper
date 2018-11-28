#include <bits/stdc++.h>
using namespace std;

int f[111][111][111][4];

int dp(int x, int y, int z, int rem)
{
  if (x + y + z == 0)
    return 0;
  int &res = f[x][y][z][rem];
  if (res >= 0)
    return res;
  res = 0;
  if (x) res = max(res, dp(x - 1, y, z, (rem + 1) % 4));
  if (y) res = max(res, dp(x, y - 1, z, (rem + 2) % 4));
  if (z) res = max(res, dp(x, y, z - 1, (rem + 3) % 4));
  if (!rem) res++;
  return res;
}

int main()
{
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << endl;
    int cnt[5] = {0}, x, n, p;
    cin >> n >> p;
    for (int i = 0; i < n; i++)
    {
      cin >> x;
      cnt[x % p]++;
    }
    int ans = cnt[0];
    if (p == 2) ans += (cnt[1] + 1) / 2;
    else if (p == 3)
    {
      int pair = min(cnt[1], cnt[2]);
      ans += pair + (cnt[1] + cnt[2] - pair * 2 + 2) / 3;
    }
    else
    {
      memset(f, -1, sizeof f);
      ans = dp(cnt[1], cnt[2], cnt[3], 0) + cnt[0];
    }
    cout << "Case #" << iTest << ": " << ans << endl;
  }
}