// Sea the world.

#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

using namespace std;

// SELF TEMPLATE CODE BGEIN

#define SZ(x) ((int)((x).size()))
#define OUT(x) printf(#x" %d\n", x)
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define repf(i,a,b) for (int i = (a); i <= (b); ++i)
#define repd(i,a,b) for (int i = (a); i >= (b); --i)
#define repcase int t, Case = 1; for (scanf ("%d", &t); t; --t)

typedef long long int64;
typedef pair<int, int> pii;

int sgn(double x) { return (x > 1e-8) - (x < -1e-8); }
int count_bit(int x) { return x == 0? 0 : count_bit(x >> 1) + (x & 1); }

template<class T> inline void to_min(T &a, const T b) { if (b < a) a = b; }
template<class T> inline void to_max(T &a, const T b) { if (b > a) a = b; }

// SELF TEMPLATE CODE END

long long calc_tidy_total_num(long long x) {
  char buf[20];
  sprintf(buf, "%lld", x);
  long long dp[20][10][2] = {0};
  // len, pre, same
  dp[0][0][1] = 1;
  int len = strlen(buf);
  rep (i, len) {
    int cnum = buf[i] - '0';
    rep (pre, 10) rep (same, 2) {
      if (dp[i][pre][same] == 0) {
        continue;
      }
      repf (cur, pre, 9) {
        int next_same = same;
        if (same) {
          if (cur > cnum) {
            break;
          }
          next_same = (cur == cnum);
        }
        dp[i + 1][cur][next_same] += dp[i][pre][same];
      }
    }
  }
  long long ans = 0;
  rep (cur, 10) rep (same, 2) {
    ans += dp[len][cur][same];
  }
  return ans;
}

int main() {
  repcase {
    long long x;
    scanf("%lld", &x);
    long long l = 1, r = x;
    long long target = calc_tidy_total_num(x);
    while (l <= r) {
      long long mid = (l + r) >> 1;
      if (calc_tidy_total_num(mid) == target) {
        r = mid - 1;
      } else {
        l = mid + 1;
      }
    }
    printf("Case #%d: %lld\n", Case++, r + 1);
  }
  return 0;
}
