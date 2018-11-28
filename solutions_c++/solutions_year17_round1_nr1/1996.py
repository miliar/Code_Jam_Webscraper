#include <iostream>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    int r, c;
    cin >> r >> c;
    char **cake = new char*[r];
    
    for (int j = 0; j < r; ++j) {
      cake[j] = new char[c];
      for (int k = 0; k < c; ++k) {
        cin >> cake[j][k];
      }
    }
    
    for (int j = 0; j < r; ++j) {
      for (int k = 0; k < c; ++k) {
        if (cake[j][k] != '?') {
          for (int l = 0; l < k; ++l) {
            if (cake[j][l] == '?') {
              cake[j][l] = cake[j][k];
            }
          }
          for (int l = k + 1; l < c; ++l) {
            if (cake[j][l] == '?') {
              cake[j][l] = cake[j][k];
            } else {
              break;
            }
          }
        }
      }
    }
    
    for (int j = 0; j < r; ++j) {
      // if all row values are ?
      bool all_q = true;
      for (int k = 0; k < c; ++k) {
        if (cake[j][k] != '?') {
          all_q = false;
        }
      }
      
      if (all_q) {
        if (j != 0) {
          for (int k = 0; k < c; ++k) {
            cake[j][k] = cake[j - 1][k];
          }
        } else {
          for (int k = j + 1; k < r; ++k) {
            if (cake[k][0] != '?') {
              for (int l = 0; l < c; ++l) {
                cake[j][l] = cake[k][l];
              }
              break;
            } else {
              continue;
            }
          }
        }
      }
    }
    
    cout << "Case #" << i << ":" << "\n";
    for (int j = 0; j < r; ++j) {
      for (int k = 0; k < c; ++k) {
        cout << cake[j][k];
      }
      cout << "\n";
    }
    
    // delete here
  }
  
  return 0;
}

