#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;
typedef int64_t i64;

int main() {
  i64 T;
  scanf("%lld", &T);
  for (i64 zz = 1; zz <= T; zz++) {
    i64 N, C, M;
    scanf("%lld %lld %lld", &N, &C, &M);
    vector<i64> P(M);
    vector<i64> B(M);
    vector<i64> num(N);
    vector<i64> numc(C);
    for (i64 i = 0; i < M; i++) {
      i64 p, b;
      scanf("%lld %lld", &p, &b);
      p--, b--;
      P[i] = p;
      B[i] = b;

      num[p]++;
      numc[b]++;
    }
    i64 ansy = 0;
    i64 sum = 0;
    for (i64 i = 0; i < N; i++) {
      sum += num[i];
      ansy = max(ansy, (sum + i) / (i+1));
    }
    for (i64 i = 0; i < C; i++) {
      ansy = max(ansy, numc[i]);
    }

    i64 ansz = 0;
    for (i64 i = 0; i < N; i++) {
      ansz += min(ansy, num[i]);
    }

    printf("Case #%lld: %lld %lld\n", zz, ansy, M - ansz);
  }
}
