#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <cinttypes>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

using LD = double;
const LD kInf = 1.0E15;

struct Horse {
  int max_dist, speed;
};

LD Dp(int i,
      int j,
      int start,
      const vector<Horse>& H,
      const vector<vector<int>>& D,
      vector<vector<LD>>& dp,
      vector<vector<char>>& used) {
  if (i == start && j == start) {
    return 0;
  }
  if (i <= j) {
    return kInf;
  }
  if (i < start || j < start) {
    return kInf;
  }

  LD& r = dp[i][j];
  if (used[i][j]) {
    return r;
  }

  used[i][j] = true;
  r = kInf;

  int64_t dist = 0;
  for (int k = j + 1; k <= i; ++k) {
    dist += D[k - 1][k];
  }
  if (dist <= H[j].max_dist) {
    LD cost = (LD) dist / H[j].speed;
    for (int k = start; k <= j; ++k) {
      r = min(r, Dp(j, k, start, H, D, dp, used));
    }

    r = min(kInf, r + cost);
  }

  return r;
}

vector<LD> Calc(int start,
                const vector<Horse>& H,
                const vector<vector<int>>& D) {
  int N = H.size();
  vector<LD> result(N, kInf);
  result[start] = 0;

  vector<vector<LD>> dp(N, vector<LD>(N, 0));
  vector<vector<char>> used(N, vector<char>(N, false));
  for (int i = start + 1; i < N; ++i) {
    for (int j = start; j < i; ++j) {
      result[i] = min(result[i], Dp(i, j, start, H, D, dp, used));
    }
  }

  return result;
}

void Solve() {
  int N, Q;
  cin >> N >> Q;

  vector<Horse> H(N);
  for (Horse& h : H) {
    cin >> h.max_dist >> h.speed;
  }

  vector<vector<int>> D(N, vector<int>(N));
  for (int i = 0; i < N; ++i) {
    for (int j = 0; j < N; ++j) {
      cin >> D[i][j];
    }
  }

  vector<vector<LD>> R(N, vector<LD>(N, -1));

  for (int q = 0; q < Q; ++q) {
    int u, v;
    cin >> u >> v;
    --u;
    --v;

    if (R[u][v] > -1) {
      cout.precision(10);
      cout << fixed << R[u][v] << ' ';
    }

    auto result = Calc(u, H, D);
    for (int i = u; i < N; ++i) {
      R[u][i] = result[i];
    }

    cout.precision(10);
    cout << fixed << R[u][v] << ' ';
  }

  cout << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
    freopen("../Console/C-small-attempt0.in", "rb", stdin);
    freopen("../Console/C-small-attempt0.out", "wb", stdout);
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int T;
  cin >> T;
  for (int tc = 0; tc < T; ++tc) {
    cout << "Case #" << tc + 1 << ": ";
    Solve();
  }

  return 0;
}
