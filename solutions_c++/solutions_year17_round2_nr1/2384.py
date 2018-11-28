#include <bits/stdc++.h>




using namespace std;
#define MAXN 10001
double d, n;

int calc(double s) {
}
void solve() {
  cin >> d >> n;
  double mx = 0;
  for (int i = 0; i < n; ++i) {
    double k, s;
    cin >> k >> s;
    if (k < d) {
      mx = max(mx, (d-k)/s);
    }
  }
  printf("%.6f\n", d/mx);
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  int n;
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    printf("Case #%d: ", i);
    solve();
  }
  return 0;
}
