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

char s[1010];
int k;

int solve() {
  int res = 0;
  int len = strlen(s);
  for (int i = 0; i + k <= len; ++i) {
    // printf("%d %s\n", i, s);
    if (s[i] == '-') {
      rep (j, k) {
        if (s[i + j] == '+') {
          s[i + j] = '-';
        } else {
          s[i + j] = '+';
        }
      }
      ++res;
    }
  }
  rep (i, len) {
    if (s[i] != '+') {
      return -1;
    }
  }
  return res;
}

int main() {
  repcase {
    scanf("%s%d", s, &k);
    int ans = solve();
    if (ans == -1) {
      printf("Case #%d: IMPOSSIBLE\n", Case++);
    } else {
      printf("Case #%d: %d\n", Case++, ans);
    }
  }
  return 0;
}
