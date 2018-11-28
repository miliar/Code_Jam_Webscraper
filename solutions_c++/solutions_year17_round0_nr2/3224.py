#include <bits/stdc++.h>
#include <cassert>
#include <cctype>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <tuple>
#include <typeinfo>
#include <unordered_set>
#include <unordered_map>
#include <vector>
using namespace std;

#define REP2(i, m, n) for(int i = (int)(m); i < (int)(n); i++)
#define REPD(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define REP(i, n) REP2(i, 0, n)
#define ALL(c) (c).begin(), (c).end()
#define PB(e) push_back(e)
#define FOREACH(i, c) for(auto i = (c).begin(); i != (c).end(); ++i)
#define MP(a, b) make_pair(a, b)
#define BIT(n, m) (((n) >> (m)) & 1)

typedef long long ll;

template <typename S, typename T> ostream &operator<<(ostream &out, const pair<S, T> &p) {
  out << "(" << p.first << ", " << p.second << ")";
  return out;
}

template <typename T> ostream &operator<<(ostream &out, const vector<T> &v) {
  out << "[";
  REP(i, v.size()){
    if (i > 0) out << ", ";
    out << v[i];
  }
  out << "]";
  return out;
}

void dfs(ll num, int pos, int digit, ll N, ll P[], ll &res) {
  if (res != -1) {
    return;
  } else if (pos == -1) {
    res = num;
    return;
  }

  for (int i = 9; i >= digit; i--) {
    ll next_num = num + i * P[pos];
    if (next_num <= N) {
      dfs(next_num, pos - 1, i, N, P, res);
    }
  }
}

void solve() {
  ll N;
  ll P[20];
  P[0] = 1;
  for (int i = 1; i < 20; i++) {
    P[i] = P[i - 1] * 10;
  }

  cin >> N;
  ll res = -1;
  dfs(0, 18, 0, N, P, res);
  cout << res << endl;
}

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  REP(i, T) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
