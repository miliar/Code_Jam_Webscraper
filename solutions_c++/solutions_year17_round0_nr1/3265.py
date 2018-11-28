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

void solve() {
  string s;
  int K;
  cin >> s >> K;
  const int N = s.size();

  int res = 0;
  for (int i = 0; i < N - K + 1; i++) {
    if (s[i] == '-') {
      res++;
      REP(j, K) {
        s[i + j] = s[i + j] == '+' ? '-' : '+';
      }
    }
  }
  bool ok = true;
  REP(i, N) ok = ok && (s[i] ==  '+');

  if (ok) {
    cout << res << endl;
  } else {
    cout << "IMPOSSIBLE" << endl;
  }
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
