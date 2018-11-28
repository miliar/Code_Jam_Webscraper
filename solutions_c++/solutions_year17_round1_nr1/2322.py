#include <bits/stdc++.h>
#define ll long long

using namespace std;

void io() {
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
}

const int N = 123;

char grid[N][N];
pair <int, int> save[N][N], mn[N][N];
map <char, int> mm;
int orig[N][N];

int main() {
  io();
  int t, _case = 0;
  cin >> t;
  while (t--) {
    _case++;
    mm.clear();
    int r, c;
    cin >> r >> c;
    for (int i = 0; i < r; i++) {
      scanf("%s", grid[i]);
    }
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        mn[i][j] = {i, j};
        save[i][j] = {i, j};
        orig[i][j] = 0;
      }
    }
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (grid[i][j] != '?' && (! mm[grid[i][j]])) {
          int found = 0, cx = i, cy = j, mx = i, my = j;
          for (int k = 0; k < r; k++) {
            for (int l = 0; l < c; l++) {
              if (grid[i][j] == grid[k][l]) {
                cx = max(cx, k);
                cy = max(cy, l);
                mx = min(mx, k);
                my = min(my, l);
              }
            }
          }
          for (int k = mx; k <= cx; k++) {
            for (int l = my; l <= cy; l++) {
              grid[k][l] = grid[i][j];
              orig[k][l] = 1;
            }
          }
          save[mx][my] = {cx, cy};
          mn[mx][my] = {i, j};
          mm[grid[i][j]] = 1;
        }
      }
    }
    mm.clear();
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (orig[i][j] && (! mm[grid[i][j]])) {
          for (int k = j - 1; k >= 0; k--) {
            int found = 1;
            for (int l = mn[i][j].first; l <= save[i][j].first; l++) {
              if (orig[l][k]) {
                found = 2;
              }
              if (grid[l][k] == '?' && found != 2) {
                found = 0;
              }
            }
            if (! found) {
              mn[i][j].second--;
            } else {
              break;
            }
            for (int l = mn[i][j].first; l <= save[i][j].first; l++) {
              grid[l][k] = grid[i][j];
            }
          }
          for (int k = save[i][j].second + 1; k < c; k++) {
            int found = 1;
            for (int l = mn[i][j].first; l <= save[i][j].first; l++) {
              if (orig[l][k]) {
                found = 2;
              }
              if (grid[l][k] == '?' && found != 2) {
                found = 0;
              }
            }
            if (! found) {
              save[i][j].second++;
            } else {
              break;
            }
            for (int l = mn[i][j].first; l <= save[i][j].first; l++) {
              grid[l][k] = grid[i][j];
            }
          }
          for (int k = i - 1; k >= 0; k--) {
            int found = 1;
            for (int l = mn[i][j].second; l <= save[i][j].second; l++) {
              if (orig[k][l]) {
                found = 2;
              }
              if (grid[k][l] == '?' && found != 2) {
                found = 0;
              }
            }
            if (! found) {
              mn[i][j].first--;
            } else {
              break;
            }
            for (int l = mn[i][j].second; l <= save[i][j].second; l++) {
              grid[k][l] = grid[i][j];
            }
          }
          for (int k = save[i][j].first + 1; k < r; k++) {
            int found = 1;
            for (int l = mn[i][j].second; l <= save[i][j].second; l++) {
              if (orig[k][l]) {
                found = 2;
              }
              if (grid[k][l] == '?' && found != 2) {
                found = 0;
              }
            }
            if (! found) {
              save[i][j].first++;
            } else {
              break;
            }
            for (int l = mn[i][j].second; l <= save[i][j].second; l++) {
              grid[k][l] = grid[i][j];
            }
          }
          mm[grid[i][j]] = 1;
        }
      }
    }
    cout << "Case #" << _case << ":\n";
    for (int i = 0; i < r; i++) {
      puts(grid[i]);
    }
  }
  return 0;
}
