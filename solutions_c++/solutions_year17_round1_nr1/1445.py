#include <bits/stdc++.h>

using namespace std;

bool empty(string s, int n) {
  bool sw = true;
  for(int i = 0 ; i < n ; i++) {
    sw &= (s[i] == '?');
  }
  return sw;
}

int main(){
  int casos;
  cin >> casos;
  for(int caso = 1 ; caso <= casos; caso++) {

    int r, c;
    cin >> r >> c;
    vector<string> grid(r);
    for(int i = 0 ; i < r ; i++) {
      cin >> grid[i];
    }

    for(int i = 0 ; i < r ; i++) {
      char x = '?';
      for(int j = 0 ; j < c ; j++) {
        if(grid[i][j] != '?') {
          x = grid[i][j];
          break;
        }
      }
      for(int j = 0 ; j < c; j++) {
        if(grid[i][j] == '?') {
          grid[i][j] = x;
        } else {
          x = grid[i][j];
        }
      }
    }

    for(int i = 1 ; i < r ; i++) {
      if(empty(grid[i], c)) {
        for(int j = 0 ; j < c ; j++) {
          grid[i][j] = grid[i - 1][j];
        }
      }
    }

    for(int i = r-2 ; i >= 0 ; i--) {
      if(empty(grid[i], c)) {
        for(int j = 0 ; j < c ; j++) {
          grid[i][j] = grid[i + 1][j];
        }
      }
    }

    cout << "Case #" << caso << ":" << endl;
    for(int i = 0 ; i < r ; i++) {
      cout << grid[i] << endl;
    }
  }
  return 0;
}