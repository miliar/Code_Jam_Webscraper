#include <cstdio>
#include <algorithm>
using namespace std;

const int maxN = 1e3 + 7;

int T, D, N, k, s;

int main()
{
  scanf("%d", &T);
  for (int cou = 1; cou <= T; cou ++) {
    double t = 0;
    scanf("%d%d", &D, &N);
    
    for (int i = 0; i < N; i ++) {
      scanf("%d%d", &k, &s);
      t = max(t, ((double)(D - k)) / s);
    }

    printf("Case #%d: %lf\n", cou, D / t);
  }
}
