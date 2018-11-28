#include <bits/stdc++.h>
#define pb push_back
#define fr first
#define sc second
#define mk make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
const double eps = 0.000000001;
const int MOD = 1000000009;
const int N = 1000005;
void solve(int num)
{
      ll n, dp = 0;
      int a[20] = {0}, sz;
      cin >> n;
      for (int i = 0; n; i ++, n /= 10)
            a[i] = n % 10, sz = i;
      int cnt = sz;
      while (cnt --)
      {
            dp = 0;
            for (int i = sz - 1; i >= 0; i --)
            {
                  dp *= 10ll;
                  if (a[i + 1] > dp + a[i])
                  {
                        a[i + 1] --;
                        a[i] += 10ll;
                        dp += a[i] - 9ll;
                        a[i] = 9ll;
                  }
                  else if (a[i + 1] > a[i])
                  {
                        dp -= 9ll - a[i];
                        a[i] = 9ll;
                  }
            }
      }
      n = 0;
      for (int i = sz; i >= 0; i --)
            n *= 10ll, n += a[i];
      cout << "Case #" << num << ": " << n << endl;
}
int main()
{
      freopen("B-large.in", "r", stdin);
      freopen("output.txt", "w", stdout);
      int t, n;
      cin >> t;
      n = t;
      while (t --)
            solve(n - t);
      return 0;
}


