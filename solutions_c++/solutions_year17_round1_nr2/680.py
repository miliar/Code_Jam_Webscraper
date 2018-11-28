#include <bits/stdc++.h>

using namespace std;

const int maxn = 60, maxm = 1e6 + 10;
int r[maxn], q[maxn][maxn], ptr[maxn];
pair<int, int> g[maxn];

pair<int, int> calc(int a, int b) {
  return make_pair(((a * 10 + 10) / 11 + b - 1) / b, a * 10 / 9 / b);
}

int main() {
  int test, n, p;
  cin >> test;
  for (int ca = 1; ca <= test; ++ca) {
    cin >> n >> p;
    for (int i = 0; i < n; ++i) {
      cin >> r[i];
    }
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j) {
        cin >> q[i][j];
      }
      sort(q[i], q[i] + p);
    }
    memset(ptr, 0, sizeof ptr);
    int ans = 0;
    for (bool flag = 0; !flag;) {
      int min_x = 1, max_x = maxm;
      for (int i = 0; i < n; ++i) {
        g[i] = calc(q[i][ptr[i]], r[i]);
        min_x = max(min_x, g[i].first);
        max_x = min(max_x, g[i].second);
      }
      if (max_x >= min_x) {
        ++ans;
        for (int i = 0; i < n; ++i) {
          flag |= ++ptr[i] == p;
        }
      } else {
        int min_p = 0;
        for (int i = 1; i < n; ++i) {
          if (g[i].second < g[min_p].second) {
            min_p = i;
          }
        }
        flag |= ++ptr[min_p] == p;
      }
    }
    cout << "Case #" << ca << ": " << ans << endl;
  }
  return 0;
}
