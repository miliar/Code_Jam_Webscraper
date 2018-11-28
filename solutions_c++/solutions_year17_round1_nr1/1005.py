#include <bits/stdc++.h>

using namespace std;

const int N = 55;

char grid[N][N];
int r, c;

bool valid(int x, int y) {
  return x >= 0 && y >= 0 && x < r && y < c;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int r, c;
    cin >> r >> c;
    for (int j = 0; j < r; j++) {
      for (int k = 0; k < c; k++) {        
        cin >> grid[j][k];        
      }
    }
    for (int j = 0; j < r; j++) {
      for (int k = 1; k < c; k++) {
        if (grid[j][k] == '?' && grid[j][k - 1] != '?') {
          grid[j][k] = grid[j][k - 1];
        }
      }
      for (int k = c - 2; k >= 0; k--) {
        if (grid[j][k] == '?' && grid[j][k + 1] != '?') {
          grid[j][k] = grid[j][k + 1];
        }
      }
    }
    for (int j = 0; j < r; j++) {
      if (grid[j][0] == '?') {
        int other;
        if (j != 0) {
          other = j - 1;                  
        } else {
          for (int k = 0; ; k++) {
            if (grid[k][0] != '?') {
              other = k;
              break;
            }
          }
        }
        for (int k = 0; k < c; k++) {
          grid[j][k] = grid[other][k];
        }
      }
    }
    cout << "Case #" << i + 1 << ":" << endl;
    for (int j = 0; j < r; j++, cout << endl) {
      for (int k = 0; k < c; k++) {
        cout << grid[j][k];
      }
    }  
  }
}