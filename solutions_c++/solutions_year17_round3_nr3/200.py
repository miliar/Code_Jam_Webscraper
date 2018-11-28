#include <bits/stdc++.h>

#define all(x) x.begin(),x.end()
using namespace std;

typedef long long ll;
typedef long double ld;

int run() {
  ll n, k;
  cin >> n >> k;
  vector<ld> mas(n + 1);
  ld allsum = 0;
  cin >> allsum;
  ld callsum = allsum;
  for (int i = 0; i < n; ++i) {
    cin >> mas[i];
  }
  mas[n] = 1;
  sort(all(mas));
  ld mys = 0;
  ld ans = -1;
  for (int i = 0; i < n; ++i) {
    ld nd = mas[i + 1] - mas[i];
    nd *= i + 1;
    if (allsum < nd + 1e-8) {
      ld can = allsum / (i + 1);
      ld curans = 1;
      for (int j = 0; j < n; ++j) {
        if (j <= i) curans *= mas[i] + can;
        else curans *= mas[j];
      }
      ans = curans;
      break;
    } else {
      allsum -= nd;
    }
  }
  cout << fixed << setprecision(50) << ans << endl;
  return 0;
}

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ll t;
  cin >> t;
  for (int q = 0; q < t; ++q) {
    cout << "Case #" << q + 1 << ": ";
    run();
  }
  return 0;
}