#include <iostream>
#include <vector>

using namespace std;

void printArray(vector<vector<char> > grid) {
  for (int i = 0; i < grid.size(); i++) {
    for (int j = 0; j < grid[i].size(); j++) {
      cout << grid[i][j];
    }
    cout << endl;
  }
}

int main() {
  int t, r, c;
  cin >> t;

  for (int k = 0; k < t; k++) {
    cin >> r >> c;
    vector<vector<char> > grid(r, vector<char> (c));

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        cin >> grid[i][j];
      }
    }

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (grid[i][j] == '?' && j > 0 && grid[i][j - 1] != '?') {
          grid[i][j] = grid[i][j - 1];
        }
      }
    }

    for (int i = 0; i < r; i++) {
      for (int j = c - 1; j >= 0; j--) {
        if (grid[i][j] == '?' && j < c - 1 && grid[i][j + 1] != '?') {
          grid[i][j] = grid[i][j + 1];
        }
      }
    }

    for (int i = 0; i < c; i++) {
      for (int j = 0; j < r; j++) {
        if (grid[j][i] == '?' && j > 0 && grid[j - 1][i] != '?') {
          grid[j][i] = grid[j - 1][i];
        }
      }
    }

    for (int i = 0; i < c; i++) {
      for (int j = r - 1; j >= 0; j--) {
        if (grid[j][i] == '?' && j < r - 1 && grid[j + 1][i] != '?') {
          grid[j][i] = grid[j + 1][i];
        }
      }
    }

    cout << "Case #" << k + 1 << ":" << endl;
    printArray(grid);
  }
}
