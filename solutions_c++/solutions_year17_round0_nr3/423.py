#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll cal(ll n, ll mid, map<ll, ll> &mp) {
  if (n <= mid) {
    return 0;
  }
  if (!mp[n]) {
    mp[n] = 1 + cal((n - 1) / 2, mid, mp) + cal(n / 2, mid, mp);
  }
  return mp[n];
}

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    ll n, k;
    cin >> n >> k;
    ll low = 0, high = n;
    while (low <= high) {
      map<ll, ll> mp;
      ll mid = (low + high) / 2;
      if (cal(n, mid, mp) >= k) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }
    printf("Case #%d: %lld %lld\n", cas, (high + 1) / 2, high / 2);
  }
  return 0;
}
