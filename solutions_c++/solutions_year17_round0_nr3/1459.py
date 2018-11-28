#include <bits/stdc++.h>
using namespace std;

int main()
{
  int test;
  cin >> test;
  for (int iTest = 1; iTest <= test; iTest++)
  {
    cerr << "Running test " << iTest << endl;
    long long n, k, ans;
    cin >> n >> k;
    map <long long,long long> m;
    m[n] = 1;
    while (1)
    {
      auto u = *m.rbegin();
      // cout << u.first << ' ' << u.second << endl;
      if (u.second >= k)
      {
        ans = u.first;
        break;
      }

      m.erase(u.first);
      long long l = (u.first - 1) / 2, r = u.first - 1 - l;
      if (l) m[l] += u.second;
      if (r) m[r] += u.second;
      k -= u.second;
    }

    cout << "Case #" << iTest << ": ";
    cout << ans / 2 << ' ' << (ans - 1) / 2 << endl;
  }
}