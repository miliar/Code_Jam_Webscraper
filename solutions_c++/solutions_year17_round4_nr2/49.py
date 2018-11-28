#include <cstdio>
#include <algorithm>
#include <utility>
#include <cmath>

int main()
{
  int T;
  scanf("%d", &T);
  for (int t=1; t<=T; t++)
  {
    int N, C, M;
    scanf("%d%d%d", &N, &C, &M);
    int P[1001] = {}, B[1001] = {};
    for (int i = 0 ; i < M; i++)
    {
      int p, b;
      scanf("%d%d", &p, &b);
      P[p-1]++;
      B[b]++;
    }
    int Y = 0;
    for (int i = 1; i <= C; i++)
      Y = std::max(Y, B[i]);
    int cum = 0;
    for (int i = 0; i < N; i++)
    {
      cum += P[i];
      Y = std::max(Y, (cum+i)/(i+1));
    }
    int Z = 0;
    cum = 0;
    for (int i = 0; i < N; i++)
    {
      if (P[i] > Y)
        Z += P[i]-Y;
    }
    printf("Case #%d: %d %d\n", t, Y, Z);
  }
}