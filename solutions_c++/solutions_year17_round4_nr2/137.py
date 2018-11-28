/* Written by Filip Hlasek 2017 */
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <iostream>

#define FOR(i, a, b)   for (int i = (a); i <= (b); i++)
#define FORD(i, a, b)  for (int i = (a); i >= (b); i--)
#define REP(i, b)      for (int i =  0 ; i <  (b); i++)

using namespace std;

#define MAXN 1111
int N, C, M;
int tickets[MAXN];
int cnt[MAXN];

int possible(int R) {
  int ans = 0, leftovers = 0;
  FORD(i, N - 1, 0) {
    if (cnt[i] > R) {
      ans += cnt[i] - R;
      leftovers += cnt[i] - R;
    } else {
      leftovers = max(0, leftovers - (R - cnt[i]));
    }
  }
  if (leftovers) return -1;
  return ans;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%d%d%d", &N, &C, &M);
    REP(i, C) tickets[i] = 0;
    REP(i, N) cnt[i] = 0;
    REP(i, M) {
      int p, b;
      scanf("%d%d", &p, &b);
      cnt[p - 1]++;
      tickets[b - 1]++;
    }
    int l = 0, r = M;
    REP(i, C) l = max(l, tickets[i]);
    while (l < r) {
      int m = (l + r) / 2;
      if (possible(m) >= 0) r = m;
      else l = m + 1;
    }
    printf("Case #%d: %d %d\n", t, l, possible(l));
  }
  return 0;
}
