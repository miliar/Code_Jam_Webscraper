#include <algorithm>
#include <cassert>
#include <cstring>
#include <iostream>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cout << #x << " = " << x << endl
#define _ << " _ " <<

typedef long long llint;

const int MAX = 1010;

int a[MAX][MAX];

int main(void) {
  int TC;
  scanf("%d", &TC);
  for (int tp = 1; tp <= TC; ++tp, fflush(stdout)) {
    int N, C, M;
    scanf("%d %d %d", &N, &C, &M);
    REP(i, C) REP(j, N) a[i][j] = 0;
    
    REP(i, M) {
      int P, B;
      scanf("%d %d", &P, &B); --P, --B;
      a[B][P]++;
    }

    int ret = 0;
    int sum = 0;
    REP(i, N) {
      int K = i + 1;
      REP(j, C) sum += a[j][i];
      ret = max(ret, (sum + K - 1) / K);
    }

    REP(i, C) {
      ret = max(ret, accumulate(a[i], a[i] + N, 0));
    }

    int proms = 0;
    REP(i, N) {
      int sum = 0;
      REP(j, C) sum += a[j][i];
      proms += sum - min(ret, sum);
    }
    
    printf("Case #%d: ", tp);
    printf("%d %d\n", ret, proms);
    
  }
  return 0;
}
