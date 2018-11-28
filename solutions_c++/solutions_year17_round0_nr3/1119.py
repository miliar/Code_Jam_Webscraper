#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <utility>
#include <numeric>
#include <algorithm>
#include <bitset>
#include <complex>
#include <array>
#include <list>
#include <stack>
#include <valarray>

using namespace std;

typedef unsigned uint;
typedef long long Int;
typedef unsigned long long UInt;

const int INF = 1001001001;
const Int INFLL = 1001001001001001001LL;

template<typename T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }
template<typename T> void chmin(T& a, T b) { if (a > b) a = b; }
template<typename T> void chmax(T& a, T b) { if (a < b) a = b; }
int in() { int x; scanf("%d", &x); return x; }
double fin() { double x; scanf("%lf", &x); return x; }
Int lin() { Int x; scanf("%lld", &x); return x; }

void solve() {
  Int N = lin();
  Int K = lin();

  map<Int, Int, greater<Int>> S, T;
  S[N] = 1;

  while (true) {
    T.clear();
    for (const auto p : S) {
      Int v = p.first - 1;
      if (K <= p.second) {
        printf("%lld %lld\n", v - v / 2, v / 2);
        return;
      }
      K -= p.second;
      T[v / 2] += p.second;
      T[v - v / 2] += p.second;
    }
    T.swap(S);
  }
}

int main() {
  int T = in();

  for (int TC = 1; TC <= T; ++TC) {
    printf("Case #%d: ", TC);
    solve();
  }

  return 0;
}
