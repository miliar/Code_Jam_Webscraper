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
  string S;
  int K;
  cin >> S >> K;

  int result = 0;
  for (int i = 0; i <= S.size() - K; ++i) {
    if (S[i] != '-') {
      continue;
    }

    ++result;
    for (int j = 0; j < K; ++j) {
      if (S[i + j] == '-') {
        S[i + j] = '+';
      } else {
        S[i + j] = '-';
      }
    }
  }

  if (find(S.begin(), S.end(), '-') == S.end()) {
    cout << result << endl;
  } else {
    cout << "IMPOSSIBLE" << endl;
  }
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
