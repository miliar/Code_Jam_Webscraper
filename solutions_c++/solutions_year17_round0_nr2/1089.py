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
  char S[32];
  scanf("%s", S);

  bool all9 = false;
  vector<int> R;
  R.push_back(0);
  for (int i = 0; S[i]; ++i) {
    int k = S[i] - '0';
    if (all9) {
      R.push_back(9);
    } else if (R.back() <= k) {
      R.push_back(k);
    } else {
      for (int j = R.size() - 1; j > 0; --j) {
        if (R[j - 1] < R[j]) {
          --R[j];
          for (int p = j + 1; p < R.size(); ++p) {
            R[p] = 9;
          }
          all9 = true;
          R.push_back(9);
          break;
        }
      }
    }
  }

  bool leading_zero = true;
  for (const int d : R) {
    if (d != 0) {
      leading_zero = false;
    }
    if (!leading_zero) {
      putchar(d + '0');
    }
  }
  puts("");
}

int main() {
  int T = in();

  for (int TC = 1; TC <= T; ++TC) {
    printf("Case #%d: ", TC);
    solve();
  }

  return 0;
}
