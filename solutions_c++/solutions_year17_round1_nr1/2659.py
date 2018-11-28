#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char mat[30][20];
int m, n;

int bd[26][4];

bool vis[26];

void up(int c) {
  int &d = bd[c][0];
  while (d > 0) {
    for (int i = bd[c][1]; i <= bd[c][2]; ++i) {
      if (mat[d - 1][i] != '?') return;
    }
    --d;
    for (int i = bd[c][1]; i <= bd[c][2]; ++i) {
      mat[d][i] = char(c + 'A');
    }
  }
}

void down(int c) {
  int &d = bd[c][3];
  while (d < m - 1) {
    for (int i = bd[c][1]; i <= bd[c][2]; ++i) {
      if (mat[d + 1][i] != '?') return;
    }
    ++d;
    for (int i = bd[c][1]; i <= bd[c][2]; ++i) {
      mat[d][i] = char(c + 'A');
    }
  }
}

void left(int c) {
  int &d = bd[c][1];
  while (d > 0) {
    for (int i = bd[c][0]; i <= bd[c][3]; ++i) {
      if (mat[i][d - 1] != '?') return;
    }
    --d;
    for (int i = bd[c][0]; i <= bd[c][3]; ++i) {
      mat[i][d] = char(c + 'A');
    }
  }
}

void right(int c) {
  int &d = bd[c][2];
//  printf("right %d\n", c);
  while (d < n - 1) {
    for (int i = bd[c][0]; i <= bd[c][3]; ++i) {
//      printf("check %d %d %c\n", i, d + 1, mat[i][d+1]);
      if (mat[i][d + 1] != '?') return;
    }
    ++d;
    for (int i = bd[c][0]; i <= bd[c][3]; ++i) {
      mat[i][d] = char(c + 'A');
    }
  }
}

int main() {
  freopen("/Users/yogy/ClionProjects/untitled/A-small-attempt0.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/A.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  while (T--) {
    scanf("%d%d", &m, &n);
    for (int i = 0; i < 26; ++i) {
      bd[i][0] = bd[i][1] = 100;
      bd[i][2] = bd[i][3] = -1;
    }
    for (int i = 0; i < m; ++i) {
      scanf("%s", mat[i]);
      for (int j = 0; j < n; ++j) {
        if (mat[i][j] == '?') continue;
        int c = mat[i][j] - 65;
        bd[c][0] = min(bd[c][0], i);
        bd[c][1] = min(bd[c][1], j);
        bd[c][2] = max(bd[c][2], j);
        bd[c][3] = max(bd[c][3], i);
      }
    }

    for (int i = 0; i < 26; ++i) {
      if (bd[i][3] != -1) {
        for (int k = 0; k < 4; ++k) {
//          printf("bd[%d][%d] = %d\n", i, k, bd[i][k]);
        }
        for (int j = bd[i][0]; j <= bd[i][3]; ++j) {
          for (int k = bd[i][1]; k <= bd[i][2]; ++k) {
            mat[j][k] = char('A' + i);
          }
        }
      }
    }

    memset(vis, 0, sizeof(vis));

    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        int c = mat[i][j] - 65;
        if (vis[c]) continue;
        up(c);
        left(c);
        right(c);
        down(c);
        vis[c] = 1;
      }
    }

    printf("Case #%d:\n", ++tc);

    for (int i = 0; i < m; ++i) {
      printf("%s\n", mat[i]);
    }

  }
  return 0;
}