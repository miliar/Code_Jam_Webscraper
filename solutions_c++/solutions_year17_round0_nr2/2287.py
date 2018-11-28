#include <bits/stdc++.h>

using namespace std;

using ll = long long;

bool isTidy(ll x) {
  ll ld = 9;
  while(x) {
    ll d = x % 10ll;
    x /= 10ll;
    if (d > ld) return false;
    ld = d;
  }
  return true;
}

ll solve(ll n) {
  ll ans = 1ll;

  ll suf = 0;
  ll x = n;
  ll p = 1ll;
  while (x) {
    ll pref = x / 10ll;
    ll d = x % 10ll;

    if (d) {
      ll c = pref * p * 10ll + (d - 1ll) * p + suf;
      if (isTidy(c)) {
        ans = max(ans, c);
      }
    }

    suf = suf * 10ll + 9ll;
    x = pref;
    p *= 10ll;
  }

  return ans;
}

void test() {
  ll ans = 1ll;
  for (int n = 1; n < 1.e7; n++) {
    if (isTidy(n)) ans = n;
    if (solve(n + 1ll) != ans) {
      cout << "Wrong answer for " << n << endl;
    }
  }
}

int main() {
  //test();
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    ll n;
    cin >> n;
    ll ans = solve(n + 1ll);
    cout << "Case #" << tc << ": " << ans << '\n';
  }
}
