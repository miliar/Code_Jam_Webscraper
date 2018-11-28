#include <bits/stdc++.h>

using namespace std;

pair<int, int> intersect(pair<int, int> &i1, pair<int, int> &i2) {
  return make_pair(max(i1.first, i2.first), min(i1.second, i2.second));
}

int main() {
  int tc;
  cin >> tc;

  for (int t = 1; t <= tc; t++) {
    cout << "Case #" << t << ": ";

    int n, p;
    cin >> n >> p;

    vector<int> qt(n);

    for (int i = 0; i < n; i++)
      cin >> qt[i];

    vector<vector<pair<int, int>>> pkg(n, vector<pair<int, int>>(p));

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < p; j++) {
        int q;
        cin >> q;

        pkg[i][j].first = (10*q + 11*qt[i] - 1) / (11*qt[i]);
        pkg[i][j].second = (10*q) / (9*qt[i]);
      }

      sort(pkg[i].begin(), pkg[i].end());
    }

    int ans = 0;

    while (true) {
      pair<int, int> p{1, numeric_limits<int>::max()};

      bool end = false;
      int max_end = 0;

      for (int i = 0; i < n; i++) {
        if (pkg[i].size() == 0) {
          end = true;
          break;
        }

        p = intersect(p, pkg[i].back());

        if (pkg[i].back().first > pkg[max_end].back().first) {
          max_end = i;
        }
      }

      if (end)
        break;

      if (p.first <= p.second) {
        ans++;
        for (int i = 0; i < n; i++)
          pkg[i].pop_back();
      } else {
        pkg[max_end].pop_back();
      }
    }

    cout << ans << endl;
  }

  return 0;
}
