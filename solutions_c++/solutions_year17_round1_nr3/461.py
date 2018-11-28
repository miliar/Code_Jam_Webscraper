#include <bits/stdc++.h>

using namespace std;

using ll = long long;

const ll INF = numeric_limits<ll>::max();

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
      ll hd, ad, hk, ak, b, d;
      cin >> hd >> ad >> hk >> ak >> b >> d;

      ll ans = INF;
      for (int deb = 0; deb < 101; deb++) {
        for (int buf = 0; buf < 101; buf++) {
          ll h1 = hd;
          ll a1 = ad;
          ll h2 = hk;
          ll a2 = ak;
          ll sub = 0;
          int cdeb = deb;
          int cbuf = buf;

          while (true) {
            sub++;
            if (sub > 100000) break;
            if (sub > ans) break;
            if (a2 - (cdeb ? d : 0) >= h1 and h2 > a1) {
              h1 = hd;
            } else if (cdeb) {
              a2 = max(a2 - d, 0ll);
              cdeb--;
            } else if (cbuf) {
              a1 += b;
              cbuf--;
            } else {
              h2 -= a1;
            }

            if (h2 <= 0) break;

            h1 -= a2;

            if (h1 <= 0) break;
          }

          if (h2 <= 0) ans = min(ans, sub);
        }
      }

      cout << "Case #" << tc << ": ";
      if (ans < INF) {
        cout << ans << endl;
      } else {
        cout << "IMPOSSIBLE" << endl;
      }
  }

}
