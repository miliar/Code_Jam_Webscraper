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

int calc(vector<int> P, vector<int> B, int mb, int N) {
  vector<int> counter(N);
  REP(i, P.size()) {
    counter[P[i] - 1]++;
  }
  int total_promoted = 0;
  int current_promoted = 0;
  for (int i = N - 1; i >= 0; i--) {
    if (counter[i] + current_promoted <= mb) {
      current_promoted = 0;
    } else if (counter[i] <= mb) {
      current_promoted = max(0, current_promoted - (mb - counter[i]));
    } else {
      total_promoted += counter[i] - mb;
      current_promoted += counter[i] - mb;
    }
  }
  
  if (current_promoted == 0) {
    return total_promoted;
  } else {
    return -1;
  }
}

void solve() {
  int N, M, C;
  cin >> N >> C >> M;
  vector<int> P(M);
  vector<int> B(M);
  REP(i, M) {
    cin >> P[i] >> B[i];
  }
  int lb = 0;
  map<int, int> counter;
  REP(i, M) {
    lb = max(lb, counter[B[i]]++);
  }
  int ub = M;
  while (ub - lb > 1) {
    int mb = (ub + lb) / 2;
    if (calc(P, B, mb, N) < 0) {
      lb = mb;
    } else {
      ub = mb;
    }
  }
  cout << ub << " " << calc(P, B, ub, N) << endl;
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
