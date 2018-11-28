#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <bitset>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <functional>
#include <unordered_map>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <list>
#include <deque>
#include <queue>
#include <math.h>
#include <map>
#include <numeric>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;
bool test = false;
const double pi = acos(-1.0);
const double eps = 1e-11;
int breakpoint = 0;

const char rootdir[] = "C:\\CodeJam\\FashionShow";
void reopen(char* a) {
  char input[256], output[256];
  sprintf(input, "%s\\%s", rootdir, a);
  sprintf(output, "%s\\%s", rootdir, a);
  char *p = strstr(output, ".in");
  if (p) sprintf(p, ".out");
  else sprintf(&p[strlen(output)], ".out");
  freopen(input, "r", stdin);
  if (!test) freopen(output, "w", stdout);
}

int N;
int M;
char G[128][128];
char G2[128][128];

void showGrid() {
  if (!test) return;
  printf("     ");
  for (int j = 1; j <= N; j++) {
    printf("%c ", '0' + j % 10);
  }
  printf("\n");
  for (int i = 1; i <= N; i++) {
    printf("%3d: ", i);
    for (int j = 1; j <= N; j++) {
      printf("%c ", G[i][j]);
    }
    printf("\n");
  }
}

void disqualifyRowCol(int r, int c) {
  for (int i = 1; i <= N; i++) {
    if (G[i][c] == '.') G[i][c] = '#';
  }
  for (int j = 1; j <= N; j++) {
    if (G[r][j] == '.') G[r][j] = '#';
  }
}

void disqualifyDiag(int r, int c) {
  // i + j = r + c or i - j = r - c.
  for (int i = 1; i <= N; i++) {
    int j1 = (r + c - i);
    int j2 = (i + c - r);
    if (j1 >= 1 && j1 <= N && G[i][j1] == '.') G[i][j1] = '#';
    if (j2 >= 1 && j2 <= N && G[i][j2] == '.') G[i][j2] = '#';
  }
}

void resetDisqualified() {
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G[i][j] == '#') G[i][j] = '.';
    }
  }
}

// identify cells disqualified to be o
void identifyCellsDisqualied_O() {
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G[i][j] == '.' || G[i][j] == '#') continue;
      if (G[i][j] == 'o') {
        // no o in row, col, diag
        disqualifyRowCol(i, j);
        disqualifyDiag(i, j);
      } else if (G[i][j] == '+') {
        // no o in diag
        disqualifyDiag(i, j);
      } else if (G[i][j] == 'x') {
        // no o in row col
        disqualifyRowCol(i, j);
      }
    }
  }
  // showGrid();
}

int greedyPlace_O() {
  int count = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G[i][j] == '.') {
        G[i][j] = 'o';
        count++;
        disqualifyRowCol(i, j);
        disqualifyDiag(i, j);
      }
    }
  }
  // showGrid();
  return count;
}

void identifyCellsDisqualied_P() {
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G[i][j] == '.' || G[i][j] == '#') continue;
      if (G[i][j] == 'o' || G[i][j] == '+') {
        // no + in diag
        disqualifyDiag(i, j);
      } else if (G[i][j] == 'x') {
        // no + in row col
        disqualifyRowCol(i, j);
      }
    }
  }
  // showGrid();
}

int greedyPlace_P() {
  int count = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G[i][j] == '.') {
        G[i][j] = '+';
        count++;
        disqualifyDiag(i, j);
      }
    }
  }
  // showGrid();
  return count;
}

void identifyCellsDisqualied_X() {
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G[i][j] == '.' || G[i][j] == '#') continue;
      if (G[i][j] == 'o' || G[i][j] == 'x') {
        // no x in row col
        disqualifyRowCol(i, j);
      }
    }
  }
  // showGrid();
}

int greedyPlace_X() {
  int count = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G[i][j] == '.') {
        G[i][j] = 'x';
        count++;
        disqualifyRowCol(i, j);
      }
    }
  }
  // showGrid();
  return count;
}

int calculatePoints() {
  int y = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G[i][j] == '.') continue;
      y += (G[i][j] == 'o') ? 2 : 1;
    }
  }
  return y;
}

void clearGrid() {
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      G[i][j] = '.';
    }
  }
}

void backupGrid() {
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      G2[i][j] = G[i][j];
    }
  }
}

void restoreGrid() {
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      G[i][j] = G2[i][j];
    }
  }
}

bool upgradable(int r, int c) {
  if (G[r][c] == '+') {
    // row and col contains neither 'x' nor 'o'
    for (int i = 1; i <= N; i++) {
      if (i != r && G[i][c] == 'x' || G[i][c] == 'o') return false;
    }
    for (int j = 1; j <= N; j++) {
      if (j != c && G[r][j] == 'x' || G[r][j] == 'o') return false;
    }
    return true;
  } else if (G[r][c] == 'x') {
    // diag contains neither '+' nor 'o'
    for (int i = 1; i <= N; i++) {
      int j1 = (r + c - i);
      int j2 = (i + c - r);
      if (j1 >= 1 && j1 <= N && (G[i][j1] == '+' || G[i][j1] == 'o')) return false;
      if (j2 >= 1 && j2 <= N && (G[i][j2] == '+' || G[i][j2] == 'o')) return false; 
    }
    return true;
  }
  return false;
}

void finalOutput(int tt) {
  int y = calculatePoints();
  int z = 0;
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G2[i][j] != G[i][j]) {
        z++;
      }
    }
  }
  printf("Case #%d: %d %d\n", tt, y, z);
  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      if (G2[i][j] != G[i][j]) {
        printf("%c %d %d\n", G[i][j], i, j);
      }
    }
  }
  showGrid();
}

int placeAndGetPoints() {
  identifyCellsDisqualied_O();
  greedyPlace_O();
  resetDisqualified();

  identifyCellsDisqualied_P();
  greedyPlace_P();
  resetDisqualified();

  identifyCellsDisqualied_X();
  greedyPlace_X();
  resetDisqualified();

  // showGrid();
  return calculatePoints();
}

void solveOld(int tt) {
  backupGrid();
  vector<int> rows;
  vector<int> cols;
  vector<int> points;
  rows.push_back(0);
  cols.push_back(0);
  points.push_back(placeAndGetPoints());

  for (int i = 1; i <= N; i++) {
    for (int j = 1; j <= N; j++) {
      restoreGrid();
      // showGrid();
      if (upgradable(i, j)) {
        G[i][j] = 'o';
        rows.push_back(i);
        cols.push_back(j);
        points.push_back(placeAndGetPoints());
      }
    }
  }
  printf("points[%d]: ", points.size());
  for (int i = 0; i < points.size(); i++) {
    printf("%d ", points.size());
  }
  printf("\n");
}

int countBackwardDiagNonX(int r, int c) {
  int count = 0;
  for (int i = 1; i <= N; i++) {
    int j1 = (r + c - i);
    if (j1 >= 1 && j1 <= N && (G[i][j1] == '+' || G[i][j1] == 'o')) count++;
  }
  return count;
}

int countForwardDiagNonX(int r, int c) {
  int count = 0;
  for (int i = 1; i <= N; i++) {
    int j2 = (i + c - r);
    if (j2 >= 1 && j2 <= N && (G[i][j2] == '+' || G[i][j2] == 'o')) count++;
  }
  return count;
}

void checkGrid() {
  // each row has at most one 'x' or 'o'
  for (int i = 1; i <= N; i++) {
    int nonP = 0;
    for (int j = 1; j <= N; j++) {
      if (G[i][j] == 'x' || G[i][j] == 'o') nonP++;
    }
    assert(nonP <= 1);
  }
  // each col has at most one 'x' or 'o'
  for (int j = 1; j <= N; j++) {
    int nonP = 0;
    for (int i = 1; i <= N; i++) {
      if (G[i][j] == 'x' || G[i][j] == 'o') nonP++;
    }
    assert(nonP <= 1);
  }
  // each diag has at most one '+' or 'o'
  for (int j = 1; j <= N; j++) {
    assert(countForwardDiagNonX(1, j) <= 1);
    assert(countBackwardDiagNonX(1, j) <= 1);
  }
  for (int i = 2; i <= N; i++) {
    assert(countForwardDiagNonX(i, 1) <= 1);
  }
  for (int i = 2; i <= N; i++) {
    assert(countBackwardDiagNonX(i, N) <= 1);
  }
}

void solve(int tt) {
  backupGrid();
  showGrid();
  int x = 0;
  int o = 0;
  for (int j = 1; j <= N; j++) {
    if (G[1][j] == 'x') x = j;
    if (G[1][j] == 'o') o = j;
  }
  if (x == 0 && o == 0) {
    // upgrade + to o
    o = 1;
    G[1][1] = 'o';
  } else if (x > 0) {
    // upgrade x to o
    G[1][x] = 'o';
    o = x;
  }
  assert(o >= 1);
  // + + + o + + + + +
  // . . . . x . . . .
  // . . . . . x . . .
  // . . . . . . x . .
  // . . . . . . . x .
  // . . . . . . . . x
  // x . . . . . . . .
  // . x . . . . . . .
  // . . x . . . . . .
  // . + + + + + + + .
  for (int j = 1; j <= N; j++) {
    if (G[1][j] == '.') G[1][j] = '+';
  }
  for (int i = 2; i <= N; i++) {
    int j = (o + (i - 2)) % N + 1;
    G[i][j] = 'x';
    if (i == N && (j != N && j != 1)) G[i][j] = 'o';
  }
  for (int j = 2; j <= N - 1; j++) {
    if (G[N][j] == '.') G[N][j] = '+';
  }
  showGrid();
  checkGrid();
  finalOutput(tt);
}

void incub() {
  N = 10;
  clearGrid();
  G[1][1] = 'o';
  solve(0);

  clearGrid();
  G[1][2] = 'o';
  solve(0);

  clearGrid();
  G[1][3] = 'o';
  solve(0);
}

int main() {
  // test = true;
  // reopen("sample.in");
  reopen("D-small-attempt2.in");
  // reopen("C-small-2-attempt1.in");
  // reopen("C-large.in");
  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    scanf("%d %d", &N, &M);
    clearGrid();
    for (int i = 0; i < M; i++) {
      char buf[64];
      int r;
      int c;
      scanf("%s %d %d", buf, &r, &c);
      G[r][c] = buf[0];
    }
    solve(qq);
  }
  return 0;
}
