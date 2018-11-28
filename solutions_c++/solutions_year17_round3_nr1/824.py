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
typedef long double LD;
typedef pair<LD, LD> PII;

const LD PI = 3.141592653589793238L;

LD getH(LD R, LD H) { return 2 * PI * R * H; }
LD getR(LD R) { return PI * R * R; }

LD doStuff() {
  int N, K;
  scanf("%d %d", &N, &K);
  vector<PII> X(N);
  REP(i, N) {
    int R, H;
    scanf("%d %d", &R, &H);
    X[i].first = getH(R, H);
    X[i].second = getR(R);
  }
  sort(ALL(X));
  LD result = 0;
  REP(i, N) {
    LD current = X[i].first + X[i].second;
    int cnt = 1;
    RREP(j, N) {
      if (cnt == K) break;
      if (i == j || X[j].second > X[i].second) {
        continue;
      }
      ++cnt, current += X[j].first;
      if (cnt == K) break;
    }
    if (cnt == K) result = max(result, current);
  }
  return result;
}

int main() {
  int T;
  scanf("%d", &T);
  REP(t, T) printf("Case #%d: %Lf\n", t + 1, doStuff());
  return 0;
}