#include <bits/stdc++.h>

using namespace std;

const int N = 1e3 + 10;
typedef long long LL;
typedef pair<LL, LL> ii; 
LL r[N], h[N];
vector<ii> ar;

int main2() {
  int n, k;
  cin >> n >> k;
  for (int i = 0; i < n; ++i) {
    cin >> r[i] >> h[i];
  }
  ar.resize(n);
  for (int i = 0; i < n; i++) {
    ar[i] = {2*r[i]*h[i], r[i]};
  }
  sort(ar.begin(), ar.end());
  reverse(ar.begin(), ar.end());
  for (ii e : ar) {
    //cerr << e.first << "-" << e.second << "\n";
  }
  LL ans = 0, curr;
  for (int i = 0; i < n; i++) {
    LL r0 = ar[i].second;  // last
    curr = r0 * r0 + ar[i].first;
    int taken = 1, idx = 0;
    while (taken < k && idx < n) {
      if (ar[idx].second <= r0 && idx != i) {
        ++taken;
        curr += ar[idx].first;
        //cerr << "taken " << ar[idx].second << " ";
      }
      ++idx;
    }
    //cerr << "\n";
    if (taken == k) {
      //cerr << curr  - r0 * r0 << "\n";
      ans = max(ans, curr);
    }
  }
  printf("%.10lf\n", M_PI * (double) ans);
  return 0;
}

int main() {
  int T; cin >> T;
  for (int qq = 1; qq <= T; ++qq) {
    printf("Case #%d: ", qq);
    main2();
  }
  return 0;
}
