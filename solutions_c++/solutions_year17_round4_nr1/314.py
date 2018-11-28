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


int N, P;
map<pair<vector<int>, int>, int> memo;

int rec(vector<int> &vec, int left_over) {
  bool done = true;
  REP2(i, 1, vec.size()) {
    if (vec[i] > 0) done = false;
  }
  
  if (done) {
    return vec[0];
  } else if (memo.count(make_pair(vec, left_over))) {
    return memo[make_pair(vec, left_over)];
  } else {
    int &res = memo[make_pair(vec, left_over)];
    REP2(i, 1, vec.size()) {
      if (vec[i] > 0) {
        vec[i]--;
        res = max(res, rec(vec, (left_over + i) % P) + (left_over == 0));
        vec[i]++;
      }
    }
    return res;
  }
}
        

void solve() {
  cin >> N >> P;
  vector<int> v(P);
  REP(i, N) {
    int g;
    cin >> g;
    v[g % P]++;
  }

  memo.clear();
  cout << rec(v, 0) << endl;
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
