#include <bits/stdc++.h>
using namespace std;

bool cant[1444][2];

int dp[722][722][2];
int f(int x, int y, int z) {
  if (x == 0 && y == 0) return z;
  if (z == 0 && x == 0) return 1000000;
  if (z == 1 && y == 0) return 1000000;
  if (cant[1440-x-y][z]) return 1000000;
  if (~dp[x][y][z]) return dp[x][y][z];
  
  if (z == 0) return dp[x][y][z] = min(f(x-1, y, 0), 1 + f(x-1, y, 1));
  return dp[x][y][z] = min(f(x, y-1, 1), 1 + f(x, y-1, 0));
}

int Main() {
  int c, j;
  scanf("%d %d", &c, &j);
  
  memset(cant, 0, sizeof cant);
  int l, r;
  while (c--) {
    scanf("%d %d", &l, &r);
    for (int i=l; i<r; i++) cant[i][0] = 1;
  }
  
  while (j--) {
    scanf("%d %d", &l, &r);
    for (int i=l; i<r; i++) cant[i][1] = 1;
  }
  
  memset(dp, -1, sizeof dp);
  int ans = f(720, 720, 0);
  for (int i=0; i<1440; i++) swap(cant[i][0], cant[i][1]);
  
  memset(dp, -1, sizeof dp);
  ans = min(ans, f(720, 720, 0));
  
  printf("%d\n", ans);
  return 0;
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc=0; tc<t; ++tc) {
    printf("Case #%d: ", tc+1);
    Main();
  }
  return 0;
}
