#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  ll t;
  cin >> t;
  for (int q = 0; q < t; ++q) {
    string s;
    ll k;
    cin >> s >> k;
    ll curcnt = 0;
    ll ans = 0;
    bool isno = false;
    vector<ll> delcnt(s.size() + 1);
    for (int i = 0; i < s.size(); ++i) {
      curcnt -= delcnt[i];
      if ((curcnt & 1) && s[i] == '+' || !(curcnt & 1) && s[i] == '-') {
        if (i < s.size() - k + 1) {
          curcnt++;
          delcnt[i + k]++;
          ans++;
        } else {
          isno = true;
        }
      }
    }
    cout << "Case #" << q + 1 << ": ";
    if (isno) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }
  return 0;
}