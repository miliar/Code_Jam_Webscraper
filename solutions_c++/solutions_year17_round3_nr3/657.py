#include <bits/stdc++.h>
#define REP(x, n) for (int x = 0; x < (int)(n); x++)
#define RREP(x, n) for (int x = (int)(n)-1; x >= 0; --x)
#define FOR(x, m, n) for (int x = (int)m; x < (int)(n); x++)
#define EACH(itr, cont) \
  for (typeof((cont).begin()) itr = (cont).begin(); itr != (cont).end(); ++itr)
#define ALL(X) (X).begin(), (X).end()
#define mem0(X) memset((X), 0, sizeof(X))
#define mem1(X) memset((X), 255, sizeof(X))

using namespace std;
typedef long long LL;

double doStuff() {
  int N, K, idx = 0;
  scanf("%d %d", &N, &K);
  double U;
  scanf("%lf", &U);
  vector<double> P(N + 1, 1);
  REP(i, N) scanf("%lf", &P[i]);
  sort(ALL(P));
  while (U > 0 && idx < N) {
    double need = (P[idx + 1] - P[idx]) * (idx + 1);
    fprintf(stderr, "@%d: %lf -> %lf need: %lf\n", idx, P[idx], P[idx + 1],
            need);
    if (need <= U) {
      REP(i, idx + 1) P[i] = P[idx + 1];
      U -= need, ++idx;
    } else {
      double add = U / (idx + 1);
      REP(i, idx + 1) P[i] += add;
      break;
    }
  }
  double result = 1.0;
  REP(i, N) result *= P[i], fprintf(stderr, "%lf ", P[i]);
  fprintf(stderr, "\n");
  return result;
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t, T) printf("Case #%d: %lf\n", t + 1, doStuff());
  return 0;
}