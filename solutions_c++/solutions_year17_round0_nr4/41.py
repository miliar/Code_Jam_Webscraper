#include <cstdio>
using namespace std;

const int maxN = 300 + 7;
int T, n, m, p, q, ans[maxN][3], enable[maxN][maxN];
bool st, matrix[2][maxN][maxN]; // matrix[0]:row/column, matrix[1]:diagonal
char ch, pic[maxN][maxN];

int x[maxN][maxN][2], y[maxN][maxN][2];
void insert(int t, int n, int s) {
  for (int i = 1; i <= n; i ++) {
    st = true;
    for (int j = 1; j <= x[i][0][0]; j ++) {
      p = x[i][j][0], q = x[i][j][1];
      if (matrix[t][p][q]) st = false;
    }
    for (int j = 1; j <= x[i][0][0]; j ++) {
      p = x[i][j][0], q = x[i][j][1];
      enable[p][q] = st ? i : 0;
    }
  }
  /*
  for (int i = 1; i <= s; i ++) {
    for (int j = 1; j <= s; j ++) printf("%d", enable[i][j]);
    printf("\n");
  }
  printf("\n");
  for (int i = 1; i <= n; i ++) {
    st = true;
    for (int j = 1; j <= y[i][0][0]; j ++) {
      p = y[i][j][0], q = y[i][j][1];
      if (matrix[t][p][q]) st = false;
    }
    for (int j = 1; j <= y[i][0][0]; j ++) {
      p = y[i][j][0], q = y[i][j][1];
      enable[p][q] = st ? i : 0;
    }
  }
  for (int i = 1; i <= s; i ++) {
    for (int j = 1; j <= s; j ++) printf("%d", enable[i][j]);
    printf("\n");
  }
  printf("\n");
  */
  int pos[2];
  for (int i = 1; i <= n; i ++) {
    st = true, pos[0] = 0;
    for (int j = 1; j <= y[i][0][0]; j ++) {
      p = y[i][j][0], q = y[i][j][1];
      if (matrix[t][p][q]) {
        st = false;
        break;
      } else {
        if (enable[p][q] > 0) pos[0] = p, pos[1] = q; 
      }
    }
    if (st && pos[0] > 0) { 
      matrix[t][pos[0]][pos[1]] = true;
      int k = enable[pos[0]][pos[1]];
      for (int j = 1; j <= x[k][0][0]; j ++) {
        p = x[k][j][0], q = x[k][j][1];
        enable[p][q] = 0;
      }
    }
  }
}
void solve() {
  for (int i = 1; i <= n; i ++) {
    x[i][0][0] = y[i][0][0] = n;
    for (int j = 1; j <= x[i][0][0]; j ++) x[i][j][0] = i, x[i][j][1] = j; //raw
    for (int j = 1; j <= y[i][0][0]; j ++) y[i][j][0] = j, y[i][j][1] = i; //column
  }
  insert(0, n, n);
  // x should be sorted from sortest to longest
  int id;
  // slash / /
  for (int i = 1; i < n; i ++) {
    id = (i << 1) - 1;
    x[id][0][0] = x[id + 1][0][0] = i;
    for (int j = 1; j <= i; j ++) {
      x[id][j][0] = i - j + 1, x[id][j][1] = j;
      x[id + 1][j][0] = n - x[id][j][1] + 1;
      x[id + 1][j][1] = n - x[id][j][0] + 1;
    }
  }
  for (int j = 1; j <= n; j ++) {
    id = (n << 1) - 1, x[id][0][0] = n;
    for (int j = 1; j <= n; j ++)
      x[id][j][0] = n - j + 1, x[id][j][1] = j;
  }
  // backslash \ /
  for (int i = 1; i < n; i ++) {
    id = (i << 1) - 1;
    y[id][0][0] = y[id + 1][0][0] = i;
    for (int j = 1; j <= i; j ++) {
      y[id][j][0] = j, y[id][j][1] = n - i + j;
      y[id + 1][j][0] = y[id][j][1];
      y[id + 1][j][1] = y[id][j][0];
    }
  }
  for (int j = 1; j <= n; j ++) {
    id = (n << 1) - 1, y[id][0][0] = n;
    for (int j = 1; j <= n; j ++)
      y[id][j][0] = y[id][j][1] = j;
  }
  insert(1, (n << 1) - 1, n);
}

int main()
{
  scanf("%d", &T);
  for (int cou = 1; cou <= T; cou ++) {
    scanf("%d%d", &n, &m);
    for (int i = 1; i <= n; i ++)
      for (int j = 1; j <= n; j ++) {
        pic[i][j] = '.';
        matrix[0][i][j] = matrix[1][i][j] = false;
      }
    char str[7];
    for (int i = 0; i < m; i ++) {
      scanf("%s %d %d", str, &p, &q), ch = str[0]; // numbered from 1 to N
      if (ch == '+' || ch == 'o') matrix[1][p][q] = true;
      if (ch == 'x' || ch == 'o') matrix[0][p][q] = true;
      pic[p][q] = ch;
    }

    solve();

    int points, models;
    points = models = 0;
    for (int i = 1; i <= n; i ++)
      for (int j = 1; j <= n; j ++) {
        points += (matrix[0][i][j] ? 1 : 0) + (matrix[1][i][j] ? 1 : 0);

        if (matrix[0][i][j] && matrix[1][i][j]) ch = 'o';
        if (!matrix[0][i][j] && matrix[1][i][j]) ch = '+';
        if (matrix[0][i][j] && !matrix[1][i][j]) ch = 'x';
        if (!matrix[0][i][j] && !matrix[1][i][j]) ch = '.';
       
        if (ch != pic[i][j]) {
          ans[models][0] = (int)ch;
          ans[models][1] = i;
          ans[models][2] = j;
          models ++;
        }
      }
    printf("Case #%d: %d %d\n", cou, points, models);
    for (int i = 0; i < models; i ++) printf("%c %d %d\n", (char)ans[i][0], ans[i][1], ans[i][2]);
  }
}
