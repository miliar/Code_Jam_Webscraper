#include <bits/stdc++.h>
using namespace std;

int n, c, m, cntSeat[1010], cntBuyer[1010];

int ok(int rides)
{
  for (int i = 1, seats = 0; i <= n; i++)
  {
    seats += rides;
    if (seats < cntSeat[i])
      return 0;
    seats -= cntSeat[i];
  }
  return 1;
}

int solve(int rides)
{
  int res = 0;
  for (int i = 1; i <= n; i++)
    if (rides < cntSeat[i])
      res += cntSeat[i] - rides;
  return res;
}

int main()
{
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << endl;
    memset(cntSeat, 0, sizeof cntSeat);
    memset(cntBuyer, 0, sizeof cntBuyer);
    int x, y;
    cin >> n >> c >> m;
    for (int i = 0; i < m; i++)
    {
      cin >> x >> y;
      cntSeat[x]++;
      cntBuyer[y]++;
    }

    int low = 1, high = m - 1, ans = m;
    for (int i = 1; i <= c; i++)
      low = max(low, cntBuyer[i]);
    while (low <= high)
    {
      int mid = (low + high) / 2;
      if (ok(mid))
      {
        ans = mid;
        high = mid - 1;
      }
      else low = mid + 1;
    }
    cout << "Case #" << iTest << ": " << ans << ' ' << solve(ans) << endl;
  }
}