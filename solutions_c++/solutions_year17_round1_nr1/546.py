#include <iostream>
#include <algorithm>
using namespace std;

string a[27];

void solve() {
  int R, C; cin >> R >> C;
  for(int i = 0 ; i < R ; i++) {
    cin >> a[i];
  }
  for(int i = 0 ; i < R ; i++) {
    for(int j = 0 ; j < C ; j++) {
      if(a[i][j] != '?') {
        // fill up
        char ch = a[i][j];
        for(int k = i - 1 ; k >= 0 ; k--) {
          if(a[k][j] != '?') {
            break;
          } else {
            a[k][j] = ch;
          }
        }
        // fill down
        for(int k = i + 1 ; k < R ; k++) {
          if(a[k][j] != '?') {
            break;
          } else {
            a[k][j] = ch;
          }
        }
      }
    }
  }
  for(int i = 0 ; i < R ; i++) {
    for(int j = 0 ; j < C ; j++) {
      if(a[i][j] != '?') {
        // fill left
        char ch = a[i][j];
        for(int k = j - 1 ; k >= 0 ; k--) {
          if(a[i][k] != '?') {
            break;
          } else {
            a[i][k] = ch;
          }
        }
        for(int k = j + 1 ; k < C ; k++) {
          if(a[i][k] != '?') {
            break;
          } else {
            a[i][k] = ch;
          }
        }
      }
    }
  }
  for(int i = 0 ; i < R ; i++) {
    cout << a[i] << "\n";
  }
}

int main() {
  int t; cin >> t;
  for(int qq = 1 ; qq <= t ; qq++) {
    cout << "Case #" << qq << ":\n";
    solve();
  }
}
