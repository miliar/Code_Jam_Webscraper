#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

map<ll, ll> mp;
ll mymin;

ll getans(ll n) {
  if (mp.count(n)) return mp[n];
  if (n - 1 < mymin) return 0;
  return mp[n] = 1 + getans((n - 1) / 2) + getans(n / 2);
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  ll t;
  cin >> t;
  for (int q = 0; q < t; ++q) {
    ll n, k;
    cin >> n >> k;
    ll l = 0;
    ll r = 1000000000;
    while (l + 1 != r) {
      ll m = (l + r) >> 1;
      mp.clear();
      mymin = m;
      if (getans(n) >= k) l = m;
      else r = m;
    }
    cout << "Case #" << q + 1 << ": " << (l + 1) / 2 << " " << (l) / 2 << endl;
  }
  return 0;
}