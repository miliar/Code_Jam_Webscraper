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

struct Item {
  int l, r;

  friend bool operator<(const Item& lhs, const Item& rhs) {
    if (lhs.r - lhs.l != rhs.r - rhs.l) {
      return lhs.r - lhs.l < rhs.r - rhs.l;
    }

    return lhs.l > rhs.l;
  }
};

void Solve() {
  int N, K;
  cin >> N >> K;

  priority_queue<Item> Q;
  int Y, Z;
  Q.push({0, N - 1});
  for (int i = 0; i < K; ++i) {
    Item v = Q.top();
    Q.pop();

    int c = (v.l + v.r) / 2;

    if (i == K - 1) {
      Y = max(0, v.r - c);
      Z = max(0, c - v.l);
    }

    if (v.l <= c - 1) {
      Q.push({v.l, c - 1});
    }
    if (c + 1 <= v.r) {
      Q.push({c + 1, v.r});
    }
  }

  cout << Y << ' ' << Z << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/C-small-2-attempt0.in", "rb", stdin);
  freopen("../Console/C-small-2-attempt0.out", "wb", stdout);
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
