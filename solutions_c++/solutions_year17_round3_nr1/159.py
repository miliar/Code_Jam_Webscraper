#include <bits/stdc++.h>
using namespace std;
typedef long long Long;

const int N = 1e4;

pair<Long, Long> cakes[N]; // {r , h}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);

#ifdef Local
  freopen("test.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  // Area = PI * r_base ^ 2 + sum (hi * 2 PI ri)
  //      = PI (r_base ^ 2 + sum(2 * hi * ri))

  int t;
  cin >> t;

  for (int cs = 1; cs <= t; ++cs) {
    cout << "Case #" << cs << ": ";

    int n, k;
    cin >> n >> k;
    --k;

    for (int i = 0; i < n; ++i) {
      cin >> cakes[i].first >> cakes[i].second;
    }

    Long mx = 0;

    for (int i = 0; i < n; ++i) {
      vector<Long> possible;
      for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        if (cakes[j].first <= cakes[i].first) {
          possible.push_back(2 * cakes[j].first * cakes[j].second);
        }
      }
      sort(possible.rbegin(), possible.rend());
      if (possible.size() < k) continue;

      Long tmp = cakes[i].first * cakes[i].first
        + 2 * cakes[i].first * cakes[i].second;

      for (int j = 0; j < k; ++j) {
        tmp += possible[j];
      }
      mx = max(mx, tmp);
    }

    cout << fixed << setprecision(10) << acos(-1) * mx << '\n';
  }
}
