#include <stdio.h>

bool back(char mat[52][52], int r, int c) {
  int foundI = 0, foundJ = 0;
  for(int i = 1; i <= r; i++) {
    for(int j = 1; j <= c; j++) {
      if (mat[i][j] == '*') {
        foundI = i;
        foundJ = j;
      }
    }
  }
  if (foundI == 0) {
    bool visited[52][52];
    for (int i = 1; i <= r; i++) {
      for (int j = 1; j <= c; j++) {
        visited[i][j] = false;
      }
    }
    for (int i = 1; i <= r; i++) {
      for (int j = 1; j <= c; j++) {
        if (mat[i][j] == '-') {
          for (int jj = j + 1; mat[i][jj] != '#'; jj++) {
            visited[i][jj] = true;
          }
          for (int jj = j - 1; mat[i][jj] != '#'; jj--) {
            visited[i][jj] = true;
          }
        } else if (mat[i][j] == '|') {
          for (int ii = i + 1; mat[ii][j] != '#'; ii++) {
            visited[ii][j] = true;
          }
          for (int ii = i - 1; mat[ii][j] != '#'; ii--) {
            visited[ii][j] = true;
          }
        }
      }
    }
    /*
    for(int i = 1; i <= r; i++) {
      for(int j = 1; j <= c; j++) {
        printf("%c", mat[i][j]);
      }
      printf("\n");
    }//*/
    for (int i = 1; i <= r; i++) {
      for (int j = 1; j <= c; j++) {
        if (mat[i][j] == '.' && !visited[i][j])
          return false;
      }
    }
    return true;
  } else {
    mat[foundI][foundJ] = '|';
    if (back(mat, r, c))
      return true;
    mat[foundI][foundJ] = '-';
    if (back(mat, r, c))
      return true;
    return false;
  }
}

int main() {
  freopen("C.in", "r", stdin);
  freopen("C.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int r, c;
    scanf("%d%d", &r, &c);
    char mat[52][52];
    for(int j = 0; j <= c + 1; j++) {
      mat[0][j] = '#';
      mat[r + 1][j] = '#';
    }
    for(int i = 1; i <= r; i++) {
      scanf("%s", mat[i] + 1);
      mat[i][0] = '#';
      mat[i][c + 1] = '#';
    }
    for(int i = 1; i <= r; i++) {
      for(int j = 1; j <= c; j++) {
        if (mat[i][j] == '|' || mat[i][j] == '-')
          mat[i][j] = '*';
      }
    }
    bool impossible = false;
    int counter;
    int oldI, oldJ;
    for(int i = 1; i <= r; i++) {
      for(int j = 0; j <= c + 1; j++) {
        if (mat[i][j] == '#') {
          counter = 0;
        } else {
          if (mat[i][j] == '*') {
            counter++;
            if (counter > 1) {
              mat[oldI][oldJ] = '|';
              mat[i][j] = '|';
            }
            oldI = i;
            oldJ = j;
          }
        }
      }
    }
    for(int j = 1; j <= c; j++) {
      for(int i = 0; i <= r + 1; i++) {
        if (mat[i][j] == '#') {
          counter = 0;
        } else {
          if (mat[i][j] == '*' || mat[i][j] == '|') {
            counter++;
            if (counter > 1) {
              if (mat[oldI][oldJ] == '|' || mat[i][j] == '|') {
                impossible = true;
              }
              mat[oldI][oldJ] = '-';
              mat[i][j] = '-';
            }
            oldI = i;
            oldJ = j;
          }
        }
      }
    }
    impossible |= !back(mat, r, c);

    if (impossible)
      printf("Case #%d: IMPOSSIBLE\n", t);
    else {
      printf("Case #%d: POSSIBLE\n", t);
      for(int i = 1; i <= r; i++) {
        for(int j = 1; j <= c; j++) {
          printf("%c", mat[i][j]);
        }
        printf("\n");
      }
    }
  }
  return 0;
}
