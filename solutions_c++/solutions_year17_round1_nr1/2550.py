#include <iostream>
#include <vector>
using namespace std;

#define ll long long

char grid[100][100];

void replace_char(int r, int c_left, int c_right, char c) {
  for(int i = c_left; i <= c_right; i++) {
    grid[r][i] = c;
  }
}

bool check(int r, int c_left, int c_right) {
  for(int i = c_left; i <= c_right; i++) {
    if(grid[r][i] != '?') return false;
  }
  return true;
}

void replace_bottom(int r, int r_max, int c_max) {
  for(int i = r+1; i <= r_max; i++) {
    for(int j = 0; j <= c_max; j++) {
      grid[i][j] = grid[r][j]; 
    }
  }
}

void replace_most_top(int r, int c, int c_max) {
  int left_most = c, right_most = c;
  char init = grid[r][c];
  for(int i = c-1; i >= 0; i--) {
    if(grid[r][i] == '?')
      left_most = i;
    else
      break;
  }
  for(int i = c+1; i <= c_max; i++) {
    if(grid[r][i] == '?')
      right_most = i;
    else
      break;
  }
  replace_char(r, left_most, right_most, init);
  for(int i = r-1; i >= 0; i--) {
    if(check(i, left_most, right_most)) {
      replace_char(i, left_most, right_most, init);
    }
  }
}


int main() {
  int t;
  int r, c;
  cin >> t;
  for(int i = 0; i < t; i++) {
    cin >> r >> c;
    for(int j = 0; j < r; j++) {
      for(int k = 0; k < c; k++) {
        cin >> grid[j][k];
      }
    }

    vector<int> r_c_pair;
    for(int j = 0; j < r; j++) {
      for(int k = 0; k < c; k++) {
        if(grid[j][k] != '?') {
          r_c_pair.push_back(j);
          r_c_pair.push_back(k);
        }
      }
    }

    for(size_t j = 0; j < r_c_pair.size(); j+=2) {
      replace_most_top(r_c_pair[j], r_c_pair[j+1], c-1);
    }

    for(int j = r-1; j >= 0; j--) {
      if(check(j, 0, c-1)) 
        continue;
      else {
        replace_bottom(j, r-1, c-1);
        break;
      }
    }

    cout << "Case #" << i+1 << ":" << endl;
    for(int j = 0; j < r; j++) {
      for(int k = 0; k < c; k++) {
        cout << grid[j][k];
      }
      cout << endl;
    }
  }

  return 0;
}
