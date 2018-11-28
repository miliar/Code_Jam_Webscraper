#include <cstdio>
#include <algorithm>

using namespace std;

#define ll long long

const int N = 60;

int n,p;
int r[N],q[N][N];
int c[N];

inline int solve () {
  scanf ("%d %d", &n, &p);
  for (int i = 0;i < n;i ++) {
    scanf ("%d", &r[i]);
  }
  for (int i = 0;i < n;i ++) {
    for (int j = 0;j < p;j ++) {
      scanf ("%d", &q[i][j]);
    }
    c[i] = 0;
    sort (q[i], q[i] + p);
  }

  int ans = 0;
  for (ll k = 1;;) {
    int end = 0;
    for (int i = 0;i < n;i ++) {
      ll x = k * r[i];
      while (c[i] < p and 9 * x > 10 * q[i][c[i]]) {
        c[i] ++;
      }
      if (c[i] >= p) {
        end = 2;
        break;
      }
      if (10 * q[i][c[i]] > 11 * x) {
        end = 1;
        break;
      }
    }
    if (end == 0) {
      ans ++;
      for (int i = 0;i < n;i ++) {
        c[i] ++;
      }
    } else if (end == 1) {
      k ++;
    } else {
      break;
    }
  }

  return ans;
}

int main () {
  int t;
  scanf ("%d", &t);

  for (int i = 1;i <= t;i ++) {
    printf ("Case #%d: %d\n", i, solve ());
  }
}
