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
const LD kPi = 2.0 * acos(0.0);

struct Cake {
  int R, H;

  friend bool operator<(const Cake& lhs, const Cake& rhs) {
    if (lhs.R != rhs.R) {
      return lhs.R > rhs.R;
    }

    return lhs.H > rhs.H;
  }
};

LD Dp(int i,
      int k,
      const vector<Cake>& cakes,
      vector<vector<LD>>& dp,
      vector<vector<char>>& use) {
  if (k > i + 1) {
    return -kInf;
  }
  if (k == 0) {
    return 0;
  }
  if (i < 0) {
    return 0;
  }

  LD& result = dp[i][k];
  if (use[i][k]) {
    return result;
  }

  use[i][k] = true;
  result = Dp(i - 1, k, cakes, dp, use);
  LD value =
      Dp(i - 1, k - 1, cakes, dp, use) + 2 * kPi * cakes[i].R * cakes[i].H;
  if (k == 1) {
    value += kPi * cakes[i].R * cakes[i].R;
  }

  result = max(result, value);

  return result;
}

void Solve() {
  int N, K;
  cin >> N >> K;

  vector<Cake> cakes(N);
  for (Cake& c : cakes) {
    cin >> c.R >> c.H;
  }

  sort(cakes.begin(), cakes.end());
  vector<vector<char>> use(N, vector<char>(K + 1, false));
  vector<vector<LD>> dp(N, vector<LD>(K + 1, 0));

  LD result = Dp(N - 1, K, cakes, dp, use);
  cout.precision(10);
  cout << fixed << result << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/A-large.in", "rb", stdin);
  freopen("../Console/A-large.out", "wb", stdout);
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
