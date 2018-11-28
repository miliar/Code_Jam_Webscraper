#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

typedef long long LL;

int T, K, n;
string S;

LL to_mask(const vector<bool>& vec) {
  LL ret = 0;
  for (int i = 0; i < vec.size(); ++i) {
    ret <<= 1ll;
    if (vec[i]) {
      ret |= 1ll;
    }
  }
  return ret;
}

vector<bool> from_mask(LL msk) {
  vector<bool> vec(n, false);
  for (int i = 0; i < n; ++i) {
    if (msk & 1ll) {
      vec[n - 1 - i] = true;
    }
    msk >>= 1ll;
  }
  return vec;
}


int solve_small() {
  queue<pair<LL, int> > q;
  unordered_set<LL> vis;
  vector<bool> vec(n, false);
  for (int i = 0; i < n; ++i) {
    if (S[i] == '-') {
      vec[i] = true;
    }
  }
  LL init = to_mask(vec);
  if (init == 0ll) {
    return 0;
  }

  q.push(make_pair(init, 0));
  vis.insert(init);

  while (!q.empty()) {
    pair<LL, int> e = q.front();
    q.pop();
    vector<bool> v = from_mask(e.first);

    for (int i = 0; i + K <= n; ++i) {
      for (int j = 0; j < K; ++j) {
        v[i+j] = !v[i+j];
      }
      LL msk = to_mask(v);
      if (msk == 0ll) {
        return e.second + 1;
      }
      if (vis.count(msk) == 0) {
        vis.insert(msk);
        q.push(make_pair(msk, e.second + 1));
      } 
      for (int j = 0; j < K; ++j) {
        v[i+j] = !v[i+j];
      }
    }
  }
  return -1;
}

int solve() {
  vector<bool> cake(n, false);
  for (int i = 0; i < n; ++i) {
    if (S[i] == '-') {
      cake[i] = true;
    }
  }
  int sol = 0;
  for (int i = 0; i + K <= n; ++i) {
    if (!cake[i]) {
      continue;
    }
    for (int j = 0; j < K; ++j) {
      cake[i+j] = !cake[i+j]; 
    }
    ++sol;
  }

  for (int i = 0; i < n; ++i) {
    if (cake[i]) {
      return -1;
    }
  }
  return sol;
}

int main() {
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> S >> K;
    n = S.length();
    //int sol = solve_small();
    int sol = solve();
    cout << "Case #" << t << ": ";
    if (sol == -1) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      cout << sol << endl;
    }
  }
  return 0;
}