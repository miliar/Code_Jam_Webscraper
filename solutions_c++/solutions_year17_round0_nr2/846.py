#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <iostream>
#include <cmath>
#include <deque>
#include <queue>
#include <stack>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <complex>

#define mp(a, b) make_pair((a), (b))
#define pb(a) push_back((a))
#define pf(a) push_front((a))
#define rb() pop_back()
#define rf() pop_front()
#define sz(a) ((int)a.size())

using namespace std;

typedef long long lld;
typedef pair<int, int> pii;
typedef pair<lld, lld> pll;
typedef pair<lld, int> pli;
typedef pair<int, lld> pil;
typedef vector<vector<int>> Matrix;
typedef vector<vector<int>> Adj;
typedef vector<int> Row;
typedef complex<double> Complex;
typedef vector<Complex> Vcomplex;

const int MOD = 1e9 + 7;
const int INF = 1e9;
const lld LINF = 1e18;
const double FINF = 1e15;
const double EPS = 1e-9;
const double PI = 2.0 * acos(0.0);

lld D[20][20];
lld t[20];
int L;
lld kth(lld k, int len, int cur) {
  if (len == L+1) {
      return 0;
  }
  for (int i = cur; i <= 9; ++i) {
    if (D[len][i] >= k) {
      return t[L-len+1] * i + kth(k, len + 1, i);
    } else {
      k -= D[len][i];
    }
  }
  return LINF*2;
}

int main() {
  int T;
  cin >> T;

  t[1] = 1;
  for (int i = 2; i <= 18; ++i) t[i] = t[i-1] * 10;
  for (int tc = 1; tc <= T; ++tc) {
    cout << "Case #" << tc << ": ";
    lld N;
    cin >> N;
    L = 0;
    {
      lld K = N;
      while (K) {
        ++L;
        K /= 10;
      }
    }
    memset(D, 0, sizeof(D));
    for (int i = 0; i <= 9; ++i) D[L][i] = 1;
    for (int i = L-1; i >= 1; --i) {
      for (int j = 0; j <= 9; ++j) {
        for (int k = 0; k <= j; ++k) {
          D[i][k] += D[i+1][j];
        }
      }
    }

    lld k = -1;
    lld l = 1;
    lld r = 0;
    for (int i = 0; i <= 9; ++i) r += D[1][i];
    while (l <= r) {
      lld m = (l + r) / 2;
      lld x = kth(m, 1, 0);
      if (x <= N) {
        l = m + 1;
        k = x;
      } else {
        r = m - 1;
      }
    }
    cout << k << '\n';
  }
}
