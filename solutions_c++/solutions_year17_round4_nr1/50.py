#include <cstdio>
#include <algorithm>
#include <utility>
#include <cmath>
#include <cassert>

int ans[101][101][101][4];

int bf(int* C, int P, int pos = 0)
{
  int res = 0;
  for (int i = 1; i < P; i++)
  {
    if (!C[i]) continue;
    C[i]--;
    res = std::max(res, bf(C, P, (pos+i)%P) + (pos==0));
    C[i]++;
  }
  return res;
}

int main()
{
  for (int i = 0; i <= 100; i++)
  for (int j = 0; j <= 100; j++)
  for (int k = 0; k <= 100; k++)
  for (int d = 0; d <= 3; d++)
  {
    #define M(x) ans[i][j][k][d] = std::max(ans[i][j][k][d], x)
    if (i) M(ans[i-1][j][k][(d+1)%4] + (d==0));
    if (j) M(ans[i][j-1][k][(d+2)%4] + (d==0));
    if (k) M(ans[i][j][k-1][(d+3)%4] + (d==0));
    #undef M
  }
  
  int T;
  scanf("%d", &T);
  for (int t=1; t<=T; t++)
  {
    int N, P;
    scanf("%d%d", &N, &P);
    int C[4] = {};
    for (int i = 0; i < N; i++)
    {
      int G;
      scanf("%d", &G);
      C[G%P]++;
    }
    int res = C[0];// + bf(C, P);
    
    if (P == 2)
      res += (C[1]+1)/2;
    else if (P == 3)
    {
      int m = std::min(C[1], C[2]);
      res += m;
      C[1] -= m; C[2] -= m;
      res += (C[1]+C[2]+2)/3;
    }
    else
    {
      res += ans[C[1]][C[2]][C[3]][0];
    }
    
    printf("Case #%d: %d\n", t, res);
  }
}