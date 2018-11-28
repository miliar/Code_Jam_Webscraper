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
int R[MAXN];
int Q[MAXN][MAXN];
int Index[MAXN];

int minServings(int Q, int R) {
  // printf("min Q: %d R: %d = %d\n", Q, R, (Q * 10 + R * 11 - 1) / (R * 11));
  return (Q * 10 + R * 11 - 1) / (R * 11);
}

int maxServings(int Q, int R) {
  // printf("max Q: %d R: %d = %d\n", Q, R, (Q * 10) / (9 * R));
  return (Q * 10) / (9 * R);
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    int N, P;
    scanf("%d%d", &N, &P);
    REP(i, N) scanf("%d", R + i);
    REP(i, N) {
      REP(j, P) scanf("%d", &(Q[i][j]));
      sort(Q[i], Q[i] + P);
    }
    REP(i, N) Index[i] = 0;
    int ans = 0;
    while (true) {
      bool ok = true;
      int m = 0, M = 0;
      REP(i, N) {
        if (Index[i] == P) { ok = false; break; }
        if ((long long)Q[i][Index[i]] * R[m] < (long long)Q[m][Index[m]] * R[i]) m = i;
        if ((long long)Q[i][Index[i]] * R[M] > (long long)Q[M][Index[M]] * R[i]) M = i;
      }
      if (!ok) break;
      // printf("m: %d M: %d\n", m, M);
      int A = maxServings(Q[m][Index[m]], R[m]);
      int B = minServings(Q[M][Index[M]], R[M]);
      if (A >= B && A > 0) {
        ans++;
        REP(k, N) Index[k]++;
      } else {
        Index[m]++;
      }
    }
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
