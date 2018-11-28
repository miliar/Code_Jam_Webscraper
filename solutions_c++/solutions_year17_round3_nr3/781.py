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

bool Can(LD X, LD U, const vector<LD>& P) {
  for (LD p : P) {
    if (p < X) {
      LD need = X - p;
      if (need > U) {
        return false;
      }

      U -= need;
    }
  }

  return true;
}

void Solve() {
  int N, K;
  cin >> N >> K;

  LD U;
  cin >> U;

  vector<LD> P(N);
  for (LD& p : P) {
    cin >> p;
  }

  LD lo = 0, hi = 1;
  for (int step = 0; step < 100; ++step) {
    LD med = (lo + hi) / 2;
    if (Can(med, U, P)) {
      lo = med;
    } else {
      hi = med;
    }
  }

  LD result = 1;
  for (LD p : P) {
    if (p < lo) {
      result *= lo;
    } else {
      result *= p;
    }
  }

  cout.precision(10);
  cout << fixed << result << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/C-small-1-attempt0.in", "rb", stdin);
  freopen("../Console/C-small-1-attempt0.out", "wb", stdout);
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
