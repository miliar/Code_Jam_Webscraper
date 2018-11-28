#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iterator>
#include <cassert>
#include <cmath>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> pi;

typedef struct node {
  int s, e, p;

  bool operator<(const node& rhs) const {
    return s < rhs.s;
  }
}node;

bool mustTake[24*61][2];
const int totalDay = 24 * 60;

int memo[totalDay + 1][721][2][2];

int solve(int min, int totalZero, bool withZero, bool starter) {
  if (totalZero > 720) {
    return 1 << 28;
  }
  if (min == totalDay) {
    if (totalZero != 720) {
      return 1 << 28;
    }
    if (withZero && starter != 0) {
      return 1 << 28;
    }
    if (!withZero && starter != 1) {
      return 1 << 28;
    }
    return 0;
  }
  if (withZero && mustTake[min][1]) {
    return 1 << 28;
  }
  if (!withZero && mustTake[min][0]) {
    return 1 << 28;
  }
  int& ret = memo[min][totalZero][withZero][starter];
  if (ret != -1) return ret;
  int a7a = solve(min + 1, totalZero + withZero, !withZero, starter) + 1;
  int leave = solve(min + 1, totalZero + withZero, withZero, starter);
  if (a7a < leave) {
    ret = a7a;
  } else {
    ret = leave;
  }
  return ret;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  ios::sync_with_stdio(false);
  cin.tie(0);

  int T, a, b, s, e;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cin >> a >> b;
    memset(mustTake, 0, sizeof mustTake);
    memset(memo, -1, sizeof memo);
    for (int i = 0; i < a; i++) {
      cin >> s >> e;
      for (int j = s; j < e; j++) {
        mustTake[j][1] = true;
      }
    }
    for (int i = 0; i < b; i++) {
      cin >> s >> e;
      for (int j = s; j < e; j++) {
        mustTake[j][0] = true;
      }
    }
    cout << "Case #" << tt << ": " << min(solve(0, 0, 0, 1), solve(0, 0, 1, 0)) << endl;
  }

  return 0;
}
