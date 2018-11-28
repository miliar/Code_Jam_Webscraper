#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const int infinity = 1e9 + 9;
const long double PI = 3.141592653589793238L;

int N, P, G;
int C[7];

int main()
{
  int T;
  scanf("%d", &T);
  for (int Ti = 1; Ti <= T; Ti++)
  {
    // init
    scanf(" %d %d", &N, &P);
    for (int p = 0; p <= P; ++p)
      C[p] = 0;

    // input
    for (int n = 0; n < N; ++n) {
      scanf(" %d", &G);
      C[G % P]++;
    }

    // for (int p = 0; p < P; ++p)
    //   printf("%d %d\n", p, C[p]);

    // P = 2
    if (P == 2) {
      int ans = C[0] + C[1] / 2 + C[1] % 2;
      printf("Case #%d: %d\n", Ti, ans);
      continue;
    }

    // P = 3
    if (P == 3) {
      int combined = min(C[1], C[2]);
      C[1] -= combined;
      C[2] -= combined;
      int ans = C[0] + combined + (C[1] / 3) + (C[2] / 3);
      C[1] %= 3;
      C[2] %= 3;
      if (C[1] + C[2] > 0)
        ans++;
      printf("Case #%d: %d\n", Ti, ans);
      continue;
    }
  }
  return 0;
}
