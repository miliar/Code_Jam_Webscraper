#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <unordered_set>
#include <set>
#include <unordered_map>
#include <map>

using namespace std;

int main(int, char**) {

  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {
    int C, R;
    cin >> R >> C;

    vector<char> grid(C * R);
    vector<bool> to_fill(C * R);
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        cin >> grid[i * C + j];
        to_fill[i * C + j] = grid[i * C + j] == '?';
      }
    }

    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        if (!to_fill[i * C + j]) {
          int min = j;
          int max = j;
          for (int jj = j + 1; jj < C; jj++) {
            if (grid[i * C + jj] != '?') {
              break;
            }
            max = jj;
            grid[i * C + jj] = grid[i * C + j];
          }
          for (int jj = j - 1; jj >= 0; jj--) {
            if (grid[i * C + jj] != '?') {
              break;
            }
            min = jj;
            grid[i * C + jj] = grid[i * C + j];
          }

          for (int ii = i + 1; ii < R; ii++) {
            for (int jj = min; jj <= max; jj++) {
              if (grid[ii * C + jj] != grid[i * C + j] && grid[ii * C + jj] != '?') {
                goto b1;
              }
            }
            for (int jj = min; jj <= max; jj++) {
              grid[ii * C + jj] = grid[i * C + j];
            }
          }
          b1:;

          for (int ii = i - 1; ii >= 0; ii--) {
            for (int jj = min; jj <= max; jj++) {
              if (grid[ii * C + jj] != grid[i * C + j] && grid[ii * C + jj] != '?') {
                goto b2;
              }
            }
            for (int jj = min; jj <= max; jj++) {
              grid[ii * C + jj] = grid[i * C + j];
            }
          }
          b2:;
        }
      }
    }

    cout << "Case #" << t + 1 << ":\n";
    for (int i = 0; i < R; i++) {
      for (int j = 0; j < C; j++) {
        cout << grid[i * C + j];
      }
      cout << "\n";
    }

  }

  return 0;
}
