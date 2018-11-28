#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

ll e10[20];

ll bt(ll N, ll R, int l, int p) {
  if (R > N) return -1LL;
  if (p < 0) return R;

  for (int i=9; i>=l; --i) {
    ll tmp = bt(N, R + e10[p]*i, i, p - 1);
    if (tmp != -1LL) {
      return tmp;
    }
  }

  return -1;
}

int main() {
  int T;
  cin >> T;

  e10[0] = 1LL;
  for (int i=1; i<=18; ++i) {
    e10[i] = e10[i-1] * 10LL;
  }

  /*
  for (ll i=1; i<=1000; ++i) {
    int p=0;
    while (p < 19 && e10[p++] < i);
    --p;

    cout << i << ": " << bt(i, 0ll, 0, p) << endl;
  }
  */

  ll N;
  for (int i=0; i<T; ++i) {
    cin >> N;

    int p = 0;
    while (p < 19 && e10[p++] < N);
    --p;

    cout << "Case #" << i + 1 << ": " << bt(N, 0LL, 0, p) << endl;
  }

  return 0;
}
