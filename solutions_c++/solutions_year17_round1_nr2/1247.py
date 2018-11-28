#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

void computeUpLow(const vector<vector<int>>& pack, const vector<int> &r, vector<vector<int>>& up, vector<vector<int>>& low) {
  int n = pack.size(), p = pack[0].size();

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < p; ++j) {
      double l_w = pack[i][j] / (r[i] * 1.1);
      double r_w = pack[i][j] / (r[i] * 0.9);
      int l = l_w;

      if (l != 0) {
        l--;
      }

      while (l <= (r_w + 1.) && !(0.9 * l * r[i] <= pack[i][j] && pack[i][j] <= 1.1 * l * r[i]))
        ++l;
      low[i][j] = l;

      int u = r_w + 1.;
      int max_u = max(1., l_w - 1.);

      while (u >= max_u && !(0.9 * u * r[i] <= pack[i][j] && pack[i][j] <= 1.1 * u * r[i]))
        --u;
      up[i][j] = u;
    }
  }
}

bool hasIntersect(int l1, int u1, int l2, int u2) {
  if (l1 == 0 || l2 == 0)
    return false;
  if (l1 > u1 || l2 > u2)
    return false;
  if (u1 < l2 || u2 < l1)
    return false;

  return true;
}

int main() {
  int T = 0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    int n, p;
    cin >> n >> p;

    vector<int> r(n);

    for (int i = 0; i < n; ++i)
      cin >> r[i];

    vector<vector<int>> pack(n, vector<int>(p));
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < p; ++j)
        cin >> pack[i][j];
    }

    vector<vector<int>> up(n, vector<int>(p));
    vector<vector<int>> low(n, vector<int>(p));

    computeUpLow(pack, r, up, low);
    int solve = 0;

    if (n == 1) {
      for (int i = 0; i < p; ++i) {
        if (low[0][i] > 0 && low[0][i] <= up[0][i])
          solve++;
      }

    } else if (n == 2) {
      vector<int> pos(p);
      iota(pos.begin(), pos.end(), 0);

      do {
        int count = 0;
        for (int i = 0; i < p; ++i) {
          if (hasIntersect(low[0][i], up[0][i], low[1][pos[i]], up[1][pos[i]]))
            count++;
        }
        if (solve < count) {
          solve = count;
        }
      } while (next_permutation(pos.begin(), pos.end()));
    }

    cout << "Case #" << test << ": " << solve << endl;
  }
}
