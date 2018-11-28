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

using LD = long double;

struct Horse {
  int pos, speed;
};

void Solve() {
  int D, N;
  cin >> D >> N;

  vector<Horse> H(N);
  for (Horse& h : H) {
    cin >> h.pos >> h.speed;
  }

  sort(H.begin(), H.end(), [](const Horse& lhs, const Horse& rhs) {
    if (lhs.pos != rhs.pos) {
      return lhs.pos < rhs.pos;
    }
    return lhs.speed < rhs.speed;
  });

  LD tm = (D - H[N - 1].pos) / ((LD) H[N - 1].speed);
  for (int i = N - 2; i >= 0; --i) {
    LD cand = (D - H[i].pos) / ((LD) H[i].speed);
    tm = max(tm, cand);
  }

  cout.precision(10);
  cout << fixed << D / tm << endl;
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
