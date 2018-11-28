#include <bits/stdc++.h>

char oldgrid[105][105];
char plus[105][105];
char times[105][105];
char lookup[2][2];

/*
bool count_bad_in_row(int r, int c) {
  int count = 0;
  for(int i=0; i<105; i++) {
    if(i != c and (grid[r][i] == 'x' or grid[r][i] == 'o')) count++;
  }
  return count;
}

bool count_bad_in_col(int r, int c) {
  int count = 0;
  for(int i=0; i<105; i++) {
    if(i != r and (grid[i][c] == 'x' or grid[i][c] == 'o')) count++;
  }
  return count;
}

bool count_bad_in_diag_1(int r, int c) {
  int count = 0;
  for(int i=-105; i<105; i++) {
    if(i != 0 and r+i >= 0 and r+i < 105 and c+i >= 0 and c+i < 105 and
       (grid[r+i][c+i] == '+' or grid[r+i][c+i] == 'o')) count++;
  }
  return count;
}

bool count_bad_in_diag_2(int r, int c) {
  int count = 0;
  for(int i=-105; i<105; i++) {
    if(i != 0 and r-i >= 0 and r-i < 105 and c+i >= 0 and c+i < 105 and
       (grid[r-i][c+i] == '+' or grid[r-i][c+i] == 'o')) count++;
  }
  return count;
}
*/

int main() {
  int t; scanf("%d", &t);
  for(int _i=1; _i<=t; _i++) {
    printf("Case #%d: ", _i);
    int n, m; scanf("%d %d", &n, &m);
    for(int i=0; i<n; i++) for(int j=0; j<n; j++) {
      plus[i][j] = times[i][j] = false;
      oldgrid[i][j] = '.';
    }
    for(int i=0; i<m; i++) {
      char x; int r, c; scanf(" %c %d %d", &x, &r, &c); r--; c--;
      oldgrid[r][c] = x;
      if(x == '+' or x == 'o') plus[r][c] = true;
      if(x == 'x' or x == 'o') times[r][c] = true;
    }
    for(int i=0; i<n; i++) {
      for(int j=0; j<n; j++) {
        bool clear = true;
        for(int k=0; k<n; k++) {
          if(times[i][k]) clear = false;
          if(times[k][j]) clear = false;
        }
        if(clear) times[i][j] = true;
      }
    }
    for(int i=0; i<1; i++) {
      for(int j=0; j<n; j++) {
        bool clear = true;
        for(int k=-n; k<n; k++) {
          if(i+k >= 0 and i+k < n and j+k >= 0 and j+k < n) {
            if(plus[i+k][j+k]) clear = false;
          }
          if(i-k >= 0 and i-k < n and j+k >= 0 and j+k < n) {
            if(plus[i-k][j+k]) clear = false;
          }
        }
        if(clear) plus[i][j] = true;
      }
    }
    for(int i=n-1; i<n; i++) {
      for(int j=0; j<n; j++) {
        bool clear = true;
        for(int k=-n; k<n; k++) {
          if(i+k >= 0 and i+k < n and j+k >= 0 and j+k < n) {
            if(plus[i+k][j+k]) clear = false;
          }
          if(i-k >= 0 and i-k < n and j+k >= 0 and j+k < n) {
            if(plus[i-k][j+k]) clear = false;
          }
        }
        if(clear) plus[i][j] = true;
      }
    }

    lookup[0][0] = '.';
    lookup[0][1] = 'x';
    lookup[1][0] = '+';
    lookup[1][1] = 'o';

    int score=0, changes=0;
    for(int i=0; i<n; i++) {
      for(int j=0; j<n; j++) {
        if(plus[i][j]) score++;
        if(times[i][j]) score++;
        if(lookup[plus[i][j]][times[i][j]] != oldgrid[i][j]) changes++;
      }
    }
    printf("%d %d\n", score, changes);
    for(int i=0; i<n; i++) {
      for(int j=0; j<n; j++) {
        if(lookup[plus[i][j]][times[i][j]] != oldgrid[i][j]) {
          printf("%c %d %d\n", lookup[plus[i][j]][times[i][j]], i+1, j+1);
        }
      }
    }
  }
}
