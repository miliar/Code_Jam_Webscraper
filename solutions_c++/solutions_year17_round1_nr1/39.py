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

#define MAXN 55
int N, M;
char m[MAXN][MAXN];

bool empty(int r) {
  if (r < 0 || r >= N) return false;
  REP(j, M) if (m[r][j] != '?') return false;
  return true;
}

int main(int argc, char *argv[]) {
  int T;
  scanf("%d", &T);
  FOR(t, 1, T) {
    scanf("%d%d", &N, &M);
    REP(i, N) scanf("%s", m[i]);
    REP(i, N) if (!empty(i)) {
      int l = i - 1, r = i + 1;
      while (empty(l)) l--;
      while (empty(r)) r++;
      REP(j, M) if (m[i][j] != '?') {
        int l2 = j - 1, r2 = j + 1;
        while (l2 >= 0 && m[i][l2] == '?') l2--;
        while (r2 <  M && m[i][r2] == '?') r2++;
        FOR(a, l + 1, r - 1) FOR(b, l2 + 1, r2 - 1) m[a][b] = m[i][j];
      }
    }
    printf("Case #%d:\n", t);
    REP(i, N) printf("%s\n", m[i]);
  }
  return 0;
}
