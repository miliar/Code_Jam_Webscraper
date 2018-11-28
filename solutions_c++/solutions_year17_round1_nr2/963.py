#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef pair<int, int> pr;

const int N = 64;
int n, m;
vector<pr> serving_counts[N];
bool viz[N][N];
int r[N];

int find_path(int i, int low, int high) {
  if (i == n) {
    return true;
  }
  for (int j = 0; j < serving_counts[i].size(); ++j) {
    pr p = serving_counts[i][j];
    if (p.first > high) {
      break;
    }
    if (p.second >= low) {
      if (!viz[i][j] && find_path(i + 1, max(low, p.first), min(high, p.second))) {
        viz[i][j] = true;
        return true;
      }
    }
  }
  return false;
}

int main() {
  int T; cin >> T;
  for (int t = 0; t < T; ++t) {
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
      cin >> r[i];
    }
    for (int i = 0; i < n; ++i) {
      serving_counts[i].clear();
    }
    memset(viz, 0, sizeof(viz));

    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < m; ++j) {
        int amt; cin >> amt;
        int high_k = floor(amt / (0.9 * r[i]));
        int low_k = ceil(amt / (1.1 * r[i]));

        if (low_k <= high_k) {
          serving_counts[i].push_back(pr(low_k, high_k));
        }
      }
      sort(serving_counts[i].begin(), serving_counts[i].end());
    }

    int ret = 0;
    for (auto p : serving_counts[0]) {
      if (find_path(1, p.first, p.second)) {
        ++ret;
      }
    }

    printf("Case #%d: %d\n", t + 1, ret);
  }
}
