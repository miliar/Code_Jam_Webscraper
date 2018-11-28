#include <bits/stdc++.h>

using namespace std;

const int maxn = 2000;
int tot[maxn], cnt[maxn];

int main() {
  int test, n, c, m, p, b;
  cin >> test;
  for (int ca = 1; ca <= test; ++ca) {
    cin >> n >> c >> m;
    memset(tot, 0, sizeof tot);
    memset(cnt, 0, sizeof cnt);
    while (m--) {
      cin >> p >> b;
      ++tot[b];
      ++cnt[p];
    }
    int ans1 = 0;
    for (int i = 1; i <= c; ++i) {
      ans1 = max(ans1, tot[i]);
    }
    int sum = 0;
    for (int i = 1; i <= n; ++i) {
      sum += cnt[i];
      ans1 = max(ans1, (sum + i - 1) / i);
    }
    int ans2 = 0;
    for (int i = 1; i <= n; ++i) {
      ans2 += max(0, cnt[i] - ans1);
    }
    cout << "Case #" << ca << ": " << ans1 << " " << ans2 << endl;
  }
  return 0;
}
