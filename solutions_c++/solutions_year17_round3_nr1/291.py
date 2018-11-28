#include <bits/stdc++.h>

using namespace std;

using ld = long double;

const int N = 1010;
ld r[N], h[N], aux[N];

int main() {
  ios::sync_with_stdio(false);
  cout.setf(ios::fixed);
  cout.precision(10);
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int n, k;
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
      cin >> r[i] >> h[i];
    }
    ld ans = -1;
    for (int i = 0; i < n; ++i) {
      int cont = 0;
      for (int j = 0; j < n; ++j) {
        if (j != i and r[j] <= r[i]) aux[cont++] = r[j] * h[j];
      }
      if (cont < k - 1) continue;
      sort(aux, aux + cont, greater<ld>());
      ld cand = 0;
      cand += M_PI * r[i] * r[i];
      cand += 2 * M_PI * r[i] * h[i];
      for (int j = 0; j < k - 1; ++j) {
        cand += 2 * M_PI * aux[j];
      }
      ans = max(cand, ans);
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
}
