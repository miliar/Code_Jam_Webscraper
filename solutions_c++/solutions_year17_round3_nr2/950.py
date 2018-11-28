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

int Solve0(const vector<pair<int, int>>& P) {
  if (P.size() == 1) {
    return 2;
  }

  vector<int> f(24 * 60, 0);
  for (const auto& p : P) {
    for (int i = p.first; i <= p.second; ++i) {
      f[i] = -1;
    }
  }

  int c = 0;

  for (int i = 0; i < f.size(); ++i) {
    if (f[i] != 0) {
      continue;
    }

    ++c;
    queue<int> Q;
    Q.push(i);
    f[i] = c;
    while (!Q.empty()) {
      int v = Q.front();
      Q.pop();

      {
        int u = (v + f.size() + 1) % f.size();
        if (f[u] == 0) {
          f[u] = c;
          Q.push(u);
        }
      }
      {
        int u = (v + f.size() - 1) % f.size();
        if (f[u] == 0) {
          f[u] = c;
          Q.push(u);
        }
      }
    }
  }

  int d = -1;
  for (int cc = 1; cc <= c; ++cc) {
    int cnt = count(f.begin(), f.end(), cc);
    d = max(d, cnt);
  }

  if (d >= 720) {
    return 2;
  } else {
    return 4;
  }
}

int Solve1(pair<int, int> A, pair<int, int> B) {
  return 2;
}

void Solve() {
  int AC, AJ;
  cin >> AC >> AJ;

  vector<pair<int, int>> C(AC), J(AJ);
  for (auto& p : C) {
    cin >> p.first >> p.second;
    --p.second;
  }
  for (auto& p : J) {
    cin >> p.first >> p.second;
    --p.second;
  }
  sort(C.begin(), C.end());
  sort(J.begin(), J.end());

  int result;
  if (AC == 0) {
    result = Solve0(J);
  } else if (AJ == 0) {
    result = Solve0(C);
  } else {
    result = Solve1(C[0], J[0]);
  }

  cout << result << endl;
}

int main() {
//  freopen("../Console/1.txt", "rb", stdin);
  freopen("../Console/B-small-attempt2.in", "rb", stdin);
  freopen("../Console/B-small-attempt2.out", "wb", stdout);
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
