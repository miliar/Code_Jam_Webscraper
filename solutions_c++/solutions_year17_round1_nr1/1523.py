#include <cinttypes>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <unordered_map>
#include <vector>
using namespace std;

int T, R, C;
char grid[25][25];
char current;
bool found1, found2;
bool missing_rows[25];

int main(int argc, char *argv[]) {

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> R;
    cin >> C;
    for (int j = 0; j < R; ++j) {
      for (int k = 0; k < C; ++k) {
        cin >> grid[j][k];
      }
    }

    for (int j = 0; j < R; ++j) {
      missing_rows[j] = false;
    }
    for (int j = 0; j < R; ++j) {
      found1 = false;
      for (int k = 0; k < C; ++k) {
        if (grid[j][k] == '?') {
          if (!found1) {
            continue;
          } else {
            grid[j][k] = current;
          }
        } else {
          current = grid[j][k];
          if (!found1) {
            for (int l = 0; l < k; ++l) {
              grid[j][l] = current;
            }
          }
          found1 = true;
        }
      }
      if (!found1) {
        missing_rows[j] = true;
      }
    }
    found2 = false;
    for (int j = 0; j < R; ++j) {
      if (missing_rows[j]) {
        if (!found2) {
          continue;
        } else {
          for (int k = 0; k < C; ++k) {
            grid[j][k] = grid[j-1][k];
          }
        }
      } else {
        if (!found2) {
          for (int l = 0; l < j; ++l) {
            for (int k = 0; k < C; ++k) {
              grid[l][k] = grid[j][k];
            }
          }
        }
        found2 = true;
      }
    }

    cout << "Case #" << i << ":" << endl;
    for (int j = 0; j < R; ++j) {
      for (int k = 0; k < C; ++k) {
        cout << grid[j][k];
      }
      cout << endl;
    }
  }

  return 0;
}
