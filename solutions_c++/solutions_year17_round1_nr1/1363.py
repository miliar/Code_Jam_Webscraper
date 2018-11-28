#include <bits/stdc++.h>

using namespace std;

char grid[30][30];
int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int r, c; cin >> r >> c;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) cin >> grid[i][j];
    }
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (grid[i][j] == '?' && j > 0) {
          while (j < c && grid[i][j] == '?') {
            grid[i][j] = grid[i][j-1];
            j++;
          }
          j--;
        }
      }
    }
    for (int i = 0; i < r; i++) {
      for (int j = c-1; j >= 0; j--) {
        if (grid[i][j] == '?' && j < c - 1) {
          while (j >= 0 && grid[i][j] == '?') {
            grid[i][j] = grid[i][j+1];
            j--;
          }
          j++;
        }
      }
    }
    for (int i = 1; i < r; i++) {
      for (int j = 0; j < c; j++) {
        int cj = j;
        if (grid[i][j] != '?') {
          while (cj < c && grid[i][cj] == grid[i][j]) cj++;
          cj--;
          int ci = i-1;
          bool good = true;
          while (ci >= 0 && good) {
            for (int jj = j; jj <= cj; jj++) good &= grid[ci][jj] == '?';
            if (good) {
              for (int jj = j; jj <= cj; jj++) grid[ci][jj] = grid[i][j];
            }
            ci--;
          }
        }
      }
    }
    for (int i = r-2; i >= 0; i--) {
      for (int j = 0; j < c; j++) {
        int cj = j;
        if (grid[i][j] != '?') {
          while (cj < c && grid[i][cj] == grid[i][j]) cj++;
          cj--;
          int ci = i+1;
          bool good = true;
          while (ci < r && good) {
            for (int jj = j; jj <= cj; jj++) good &= grid[ci][jj] == '?';
            if (good) {
              for (int jj = j; jj <= cj; jj++) grid[ci][jj] = grid[i][j];
            }
            ci++;
          }
        }
      }
    }
    cout << "Case #" << t << ": " << endl;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        cout << grid[i][j];
      }
      cout << endl;
    }
  }
  return 0;
}
