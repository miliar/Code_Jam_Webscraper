#include <iostream>
using namespace std;
typedef long long ll;
int main() {
  int t, tt;
  ll k, n, s, g1, g2, g2cnt;
  cin >> t;
  for (tt = 1; tt <= t; tt++) {
    cin >> n >> k;
    cout << "Case #" << tt << ": ";
    if (k == 1) {
      cout << n / 2 << " " << (n - 1) / 2 << endl;
    } else {
      s = 1;
      while ((s + 1) * 2 - 1 < k) s = (s + 1) * 2 - 1;
      g1 = (n - s) / (s + 1);
      g2 = g1 + 1;
      g2cnt = (n - s) % (s + 1);
      k -= s;
      if (k <= g2cnt) cout << g2 / 2 << " " << (g2 - 1) / 2 << endl;
      else cout << g1 / 2 << " " << max(g1 - 1, 0LL) / 2 << endl;
    }
  }
  return 0;
}
