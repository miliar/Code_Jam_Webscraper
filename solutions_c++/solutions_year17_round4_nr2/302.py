#include <bits/stdc++.h>

using namespace std;

const int N = 150;

int a[N];

int main() {
  int tt;
  cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    int n, c, m;
    cin >> n >> c >> m;
    vector<vector<int>> V(n);
    vector<int> quants(c, 0);
    for (int i = 0; i < m; ++i) {
      int p, b;
      cin >> p >> b;
      --p; --b;
      V[p].emplace_back(b);
      quants[b]++;
    }
    int cota = 0;
    for (int x : quants) cota = max(cota, x);
    int s = 0;
    for (int i = 0; i < n; ++i) {
      s += V[i].size();
      while ((i + 1) * cota < s) ++cota;
    }
    int cost = 0;
    for (int i = n - 1; i >= 0; --i) {
      if (V[i].size() > cota) cost += V[i].size() - cota;
    }
    cout << "Case #" << t << ": " << cota << ' ' << cost << endl;
  }
}
