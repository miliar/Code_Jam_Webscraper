#include <bits/stdc++.h>
using namespace std;

const int N = 30;
int n, m, t, T;
char g[N][N];

void flood(int x, int y) {
  for(int i=y-1; i>0; --i) {
    if (g[x][i] != '?') break;
    g[x][i] = g[x][y];
  }
  for(int i=y+1; i<=m; ++i) {
    if (g[x][i] != '?') break;
    g[x][i] = g[x][y];
  }
}

int main() {
  scanf("%d", &T);
  while(t++ < T) {
    scanf("%d%d", &n, &m);

    memset(g, '*', sizeof g);
    for(int i=1; i<=n; ++i)
      for(int j=1; j<=m; ++j)
        scanf(" %c", &g[i][j]);

    for(int i=1; i<=n; ++i)
      for(int j=1; j<=m; ++j)
        if (g[i][j] != '?' and g[i][j] != '*')
          flood(i, j);

    for(int i=1; i<=n; ++i)
      for(int j=1; j<=m; ++j)
        if (g[i][j] != '?' and g[i][j] != '*')

          for(int i=2; i<=n; ++i)
            for(int j=1; j<=m; ++j)
              if (g[i][j] == '?')
                g[i][j] = g[i-1][j];

    for(int i=n-1; i>=1; --i)
      for(int j=1; j<=m; ++j)
        if (g[i][j] == '?')
          g[i][j] = g[i+1][j];

    printf("Case #%d:\n", t);
    for(int i=1; i<=n; ++i) {
      for(int j=1; j<=m; ++j) {
        printf("%c", g[i][j]);
      }
      printf("\n");
    }
  }

  return 0;
}
