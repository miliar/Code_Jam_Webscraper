// Author: Naresh
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <cstring>
#include <memory.h>
#include <cassert>

using namespace std;

#define all(a) a.begin(), a.end()
#define rep(i, a, b) for (int i = (a); i < (b); ++i)
#define irep(i, a, b) for (int i = (a); i >= (b); --i)
#define iter(i, v) for (auto &i : (v))
typedef long long ll;

#define gc getchar_unlocked
template <class T>
inline T readnum() {
  int i = gc(), f = 1;
  for (; i < '0' || i > '9'; i = gc())
    if (i == '-') {
      f = -1;
      i = gc();
      break;
    }
  T ret = 0;
  for (; i >= '0' && i <= '9'; i = gc()) {
    ret = ret * 10 + (i - '0');
  }
  return f * ret;
}
// utility methods to read input.
inline int si() { return readnum<int>(); }
inline ll sll() { return readnum<ll>(); }

int dis[100][100];
int DI[100], SP[100];
int to[100], from[100];

int lin[100];

double dp[100][100];

double solve(int x, int h, int N) {
    if (x == N-1) {
        return 0;
    }
    double& ans = dp[x][h];
    if (ans > -1.5) {
        return ans;
    }

    int traveled = lin[x] - lin[h];
    int onep = traveled + dis[x][x+1] <= DI[h];
    int twoPossible = dis[x][x+1] <= DI[x];
    if (!onep && !twoPossible) {
        return ans = -1;
    }
    double one = 0.0, two = 0.0;
    if (onep) {
        one = solve(x+1, h, N);
        onep = onep && one > -0.5;
    }
    if (twoPossible) {
        two = solve(x+1, x, N);
        twoPossible = twoPossible && two > -0.5;
    }
    if (!onep && !twoPossible) {
        return ans = -1;
    }
    if (onep && twoPossible) {
      return ans = min(one + dis[x][x + 1] / (1.0 * SP[h]),
                       two + dis[x][x + 1] / (1.0 * SP[x]));
    }
    if (onep) {
        return ans = one + dis[x][x+1]/(1.0*SP[h]);
    }
    return ans = two + dis[x][x+1]/(1.0*SP[x]);
}

int main() {

    int T = si();
    rep(t,0, T) {
        int N = si();
        int Q = si();
        rep(i,0, N) {
            DI[i] = si();
            SP[i] = si();
        }
        rep(i, 0, N) rep(j, 0, N) dis[i][j] = si();

        lin[0] = 0;
        rep(i, 1, N)
            lin[i] = lin[i-1] + dis[i-1][i];
        rep(i,0, Q) {
            from[i] = si();
            to[i] = si();
        }
        rep(i, 0, 100) rep(j,0, 100) dp[i][j] = -2.0;
        double ans = solve(0, 0, N);
        printf("Case #%d: %.9lf\n", t+1, ans);
    }
}
