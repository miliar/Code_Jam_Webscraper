#include <algorithm>
#include <iomanip>
#include <chrono>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::chrono;

using horse_t = pair<int, int>;

int main() {
  auto start = high_resolution_clock::now();

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);
  cout << fixed << setprecision(10);

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    int n, q;
    cin >> n >> q;
    vector<horse_t> vh(n);
    for (int i = 0; i < n; ++i)
      cin >> vh[i].first >> vh[i].second;

    vector<vector<long long>> g(n, vector<long long>(n));
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < n; ++j)
        cin >> g[i][j];

    for (int k = 0; k < n; ++k) {
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
          if (g[i][k] == -1)
            continue;
          if (g[k][j] == -1)
            continue;
          long long new_dist = g[i][k] + g[k][j];
          if (g[i][j] == -1 || g[i][j] > new_dist)
            g[i][j] = new_dist;
        }
      }
    }

    cout << "Case #" << test << ":";

    for (int qid = 0; qid < q; ++qid) {
      int s, f;
      cin >> s >> f;
      --s;
      --f;

      vector<bool> used(n, false);
      vector<long double> dist(n, -1);
      dist[s] = 0;

      while (true) {
        int from = -1;
        for (int i = 0; i < n; ++i) {
          if (used[i] || dist[i] < 0)
            continue;

          if (from == -1 || dist[from] > dist[i])
            from = i;
        }

        if (from == -1)
          break;

        used[from] = true;

        for (int to = 0; to < n; ++to) {
          if (g[from][to] != -1 && vh[from].first >= g[from][to]) {
            long double new_dist = dist[from] + 1.0 * g[from][to] / vh[from].second;
            if (dist[to] == -1 || dist[to] > new_dist)
              dist[to] = new_dist;
          }
        }
      }

      cout << " " << dist[f];
    }
    cout << endl;
  }

  cerr << "Total execution time : " << duration_cast<milliseconds>(high_resolution_clock::now() - start).count() << " ms" << endl;

  return 0;
}
