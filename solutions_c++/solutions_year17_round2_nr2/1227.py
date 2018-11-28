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

void Solve() {
  int N;
  cin >> N;

  int R, O, Y, G, B, V;
  cin >> R >> O >> Y >> G >> B >> V;

  pair<int, char> X[3];
  X[0] = {R, 'R'};
  X[1] = {Y, 'Y'};
  X[2] = {B, 'B'};

  sort(begin(X), end(X));
  string result;

  while (X[1].first > 0) {
    result.push_back(X[2].second);
    result.push_back(X[1].second);
    --X[2].first;
    --X[1].first;
  }

  if (X[2].first > X[0].first) {
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  while (X[2].first > 0) {
    result.push_back(X[2].second);
    result.push_back(X[0].second);
    --X[2].first;
    --X[0].first;
  }

  string real;
  int pos = 0;
  while (pos < result.size() && X[0].first > 0) {
    real.push_back(result[pos]);
    ++pos;
    real.push_back(X[0].second);
    --X[0].first;
  }
  while (pos < result.size()) {
    real.push_back(result[pos]);
    ++pos;
  }
  while (X[0].first > 0) {
    real.push_back(X[0].second);
    --X[0].first;
  }

  for (int i = 0; i < N; ++i) {
    int ni = (i + 1) % N;
    if (real[i] == real[ni]) {
      cout << "IMPOSSIBLE" << endl;
      return;
    }
  }

  cout << real << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/B-small-attempt3.in", "rb", stdin);
  freopen("../Console/B-small-attempt3.out", "wb", stdout);
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
