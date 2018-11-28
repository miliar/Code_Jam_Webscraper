#include <bits/stdc++.h>

using namespace std;

void solve() {
  int r; int c;
  cin >> r >> c;
  vector<string> grid(r);
  for(int i = 0; i < r; i++) {
    cin >> grid[i];
  }
  char k;
  for(int i = 0; i < r; i++) {
    k = '?';
    for(int j = 0; j < c; j++) {
      if(grid[i][j]!='?') k = grid[i][j];
      else grid[i][j] = k;
    }
  }
  for(int i = 0; i < r; i++) {
    k = '?';
    for(int j = c-1; j >= 0; j--) {
      if(grid[i][j]!='?') k = grid[i][j];
      else grid[i][j] = k;
    }
  }
  for(int i = 0; i < c; i++) {
    k = '?';
    for(int j = 0; j < r; j++) {
      if(grid[j][i]!='?') k = grid[j][i];
      else grid[j][i] = k;
    }
  }
  for(int i = 0; i < c; i++) {
    k = '?';
    for(int j = r-1; j >= 0; j--) {
      if(grid[j][i]!='?') k = grid[j][i];
      else grid[j][i] = k;
    }
  }
  for(int i = 0; i < r; i++) {
    cout << grid[i] << endl;
  }
}

int main() {
  int t; cin >> t;
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ":" << endl;
    solve();
  }
  return 0;
}
