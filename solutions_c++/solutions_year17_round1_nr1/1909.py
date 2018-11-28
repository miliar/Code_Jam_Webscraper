#include <bits/stdc++.h>

using namespace std;

char mat[100][100];

int main() {
  int t, r, c;
  scanf("%d", &t);

  for (int cas = 1; cas <= t; ++cas) {
    scanf("%d %d", &r, &c);
    for (int i = 0; i < r; ++i) {
      scanf("%s", mat[i]);
    }

    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        if (mat[i][j] != '?') {
          int k = i + 1;
          char lett = mat[i][j];
          while (k < r && mat[k][j] == '?')
            mat[k++][j] = lett;
          k = i - 1;
          while (k >= 0 && mat[k][j] == '?')
            mat[k--][j] = lett;
        }
      }
    }

    for (int i = 0; i < c; ++i)
      for (int j = i + 1; j < c && mat[0][j] == '?'; ++j)
        for (int k = 0; k < r; ++k)
          mat[k][j] = mat[k][i];

    for (int i = c - 1; i >= 0; i--)
      for (int j = i - 1; j >= 0 && mat[0][j] == '?'; --j)
        for (int k = 0; k < r; ++k)
          mat[k][j] = mat[k][i];

    printf("Case #%d:\n", cas);
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j)
        putchar(mat[i][j]);
      putchar('\n');
    }
  }

  return 0;
}
