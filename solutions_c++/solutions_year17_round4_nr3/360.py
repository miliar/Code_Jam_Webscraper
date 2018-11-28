#include <iostream>
#include <string>
#include <cstring>
using namespace std;

char map[55][55];
bool shooter_fixed[55][55];
bool feasible;

void fix(int ri, int ci, char c) {
  if (shooter_fixed[ri][ci] && map[ri][ci] != c) {
    feasible = false;
  }
  shooter_fixed[ri][ci] = true;
  map[ri][ci] = c;
}

int main() {
  int t;
  cin >> t;
  for (int ti = 1; ti <= t; ti++) {
    int r, c;
    cin >> r >> c;
    for (int ri = 0; ri < r; ri++) {
      cin >> map[ri];
    }
    memset(shooter_fixed, 0, sizeof(shooter_fixed));
    feasible = true;
    for (int ri = 0; ri < r; ri++) {
      for (int ci = 0; ci < c; ci++) {
        if (map[ri][ci] == '-' || map[ri][ci] == '|') {
          for (int rj = ri - 1; rj >= 0; rj--) {
            if (map[rj][ci] == '#') {
              break;
            }
            if (map[rj][ci] == '-' || map[rj][ci] == '|') {
              fix(ri, ci, '-');
              fix(rj, ci, '-');
            }
          }
          for (int rj = ri + 1; rj < r; rj++) {
            if (map[rj][ci] == '#') {
              break;
            }
            if (map[rj][ci] == '-' || map[rj][ci] == '|') {
              fix(ri, ci, '-');
              fix(rj, ci, '-');
            }
          }
          for (int cj = ci - 1; cj >= 0; cj--) {
            if (map[ri][cj] == '#') {
              break;
            }
            if (map[ri][cj] == '-' || map[ri][cj] == '|') {
              fix(ri, ci, '|');
              fix(ri, cj, '|');
            }
          }
          for (int cj = ci + 1; cj < c; cj++) {
            if (map[ri][cj] == '#') {
              break;
            }
            if (map[ri][cj] == '-' || map[ri][cj] == '|') {
              fix(ri, ci, '|');
              fix(ri, cj, '|');
            }
          }
        }
      }
    }
    for (int i = 0; i < 1000; i++) {
      for (int ri = 0; ri < r; ri++) {
        for (int ci = 0; ci < c; ci++) {
          if (map[ri][ci] == '.') {
            int cnt = 0;
            bool satisfied = false;
            int cr = 0, cc = 0;
            for (int rj = ri - 1; rj >= 0; rj--) {
              if (map[rj][ci] == '#') {
                break;
              }
              if (map[rj][ci] == '|' && shooter_fixed[rj][ci]) {
                satisfied = true;
              }
              if (!shooter_fixed[rj][ci] && (map[rj][ci] == '-' || map[rj][ci] == '|')) {
                cnt++;
                cr = rj;
                cc = ci;
              }
            }
            for (int rj = ri + 1; rj < r; rj++) {
              if (map[rj][ci] == '#') {
                break;
              }
              if (map[rj][ci] == '|' && shooter_fixed[rj][ci]) {
                satisfied = true;
              }
              if (!shooter_fixed[rj][ci] && (map[rj][ci] == '-' || map[rj][ci] == '|')) {
                cnt++;
                cr = rj;
                cc = ci;
              }
            }
            for (int cj = ci - 1; cj >= 0; cj--) {
              if (map[ri][cj] == '#') {
                break;
              }
              if (map[ri][cj] == '-' && shooter_fixed[ri][cj]) {
                satisfied = true;
              }
              if (!shooter_fixed[ri][cj] && (map[ri][cj] == '-' || map[ri][cj] == '|')) {
                cnt++;
                cr = ri;
                cc = cj;
              }
            }
            for (int cj = ci + 1; cj < c; cj++) {
              if (map[ri][cj] == '#') {
                break;
              }
              if (map[ri][cj] == '-' && shooter_fixed[ri][cj]) {
                satisfied = true;
              }
              if (!shooter_fixed[ri][cj] && (map[ri][cj] == '-' || map[ri][cj] == '|')) {
                cnt++;
                cr = ri;
                cc = cj;
              }
            }
            if (!satisfied) {
              if (cnt == 0) {
                feasible = false;
              } else if (cnt == 1) {
                if (cr == ri) {
                  fix(cr, cc, '-');
                } else {
                  fix(cr, cc, '|');
                }
              }
            }
          }
        }
      }
    }
    for (int i = 0; i < 1000; i++) {
      bool arbitrary = false;
      for (int ri = 0; ri < r; ri++) {
        for (int ci = 0; ci < c; ci++) {
          if (map[ri][ci] == '.') {
            int cnt = 0;
            bool satisfied = false;
            int cr = 0, cc = 0;
            for (int rj = ri - 1; rj >= 0; rj--) {
              if (map[rj][ci] == '#') {
                break;
              }
              if (map[rj][ci] == '|' && shooter_fixed[rj][ci]) {
                satisfied = true;
              }
              if (!shooter_fixed[rj][ci] && (map[rj][ci] == '-' || map[rj][ci] == '|')) {
                cnt++;
                cr = rj;
                cc = ci;
              }
            }
            for (int rj = ri + 1; rj < r; rj++) {
              if (map[rj][ci] == '#') {
                break;
              }
              if (map[rj][ci] == '|' && shooter_fixed[rj][ci]) {
                satisfied = true;
              }
              if (!shooter_fixed[rj][ci] && (map[rj][ci] == '-' || map[rj][ci] == '|')) {
                cnt++;
                cr = rj;
                cc = ci;
              }
            }
            for (int cj = ci - 1; cj >= 0; cj--) {
              if (map[ri][cj] == '#') {
                break;
              }
              if (map[ri][cj] == '-' && shooter_fixed[ri][cj]) {
                satisfied = true;
              }
              if (!shooter_fixed[ri][cj] && (map[ri][cj] == '-' || map[ri][cj] == '|')) {
                cnt++;
                cr = ri;
                cc = cj;
              }
            }
            for (int cj = ci + 1; cj < c; cj++) {
              if (map[ri][cj] == '#') {
                break;
              }
              if (map[ri][cj] == '-' && shooter_fixed[ri][cj]) {
                satisfied = true;
              }
              if (!shooter_fixed[ri][cj] && (map[ri][cj] == '-' || map[ri][cj] == '|')) {
                cnt++;
                cr = ri;
                cc = cj;
              }
            }
            if (!satisfied) {
              if (cnt == 0) {
                feasible = false;
              } else if (!arbitrary) {
                arbitrary = true;
                if (cr == ri) {
                  fix(cr, cc, '-');
                } else {
                  fix(cr, cc, '|');
                }
              } else if (cnt == 1) {
                if (cr == ri) {
                  fix(cr, cc, '-');
                } else {
                  fix(cr, cc, '|');
                }
              }
            }
          }
        }
      }
    }
    cout << "Case #" << ti << ": ";
    if (feasible) {
      cout << "POSSIBLE" << endl;
      for (int ri = 0; ri < r; ri++) {
        cout << map[ri] << endl;
      }
    } else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
