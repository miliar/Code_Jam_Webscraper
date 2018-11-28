#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll cal(int v, int l) {
  ll ans = 0;
  for (int i = 0; i < l; i++) {
    ans = ans * 10 + v;
  }
  return ans;
}

int main(int argc, const char *argv[]) {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; cas++) {
    ll n;
    cin >> n;
    int len = 18;
    while (cal(1, len) > n) {
      len--;
    }
    ll now = 0;
    for (int i = len; i >= 0; i--) {
      for (int j = 9; j >= 1; j--) {
        if (now + cal(j, i) <= n) {
          now = now + cal(j, i) - cal(j, i - 1);
          break;
        }
      }
    }
    printf("Case #%d: %lld\n", cas, now);
  }
  return 0;
}
