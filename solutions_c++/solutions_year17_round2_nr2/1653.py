#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

int main() {
  int t;
  cin >> t;
  for (int c = 1; c <= t; ++c) {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    
    vector<char> u(n);
    int first = max(r, max(y, b));
    if (first == r) {
      u[0] = 'R';
      --r;
    } else if (first == y) {
      u[0] = 'Y';
      --y;
    } else if (first == b) {
      u[0] = 'B';
      --b;
    }
    
    bool possible = true;
    
    for (int i = 1; i < n; ++i) {
      int color = max(r, max(y, b));
      
      if (color == 0) {
        possible = false;
        break;
      }
      
      if (color == r) {
      
        if (u[i - 1] == 'R') {
          if (y == 0 && b == 0) {
            possible = false;
            break;
          }
          
          if (y > b) {
            u[i] = 'Y';
            --y;
          } else {
            u[i] = 'B';
            --b;
          }
        } else {
          u[i] = 'R';
          --r;
        }
        
      } else if (color == y) {
        
        if (u[i - 1] == 'Y') {
          if (r == 0 && b == 0) {
            possible = false;
            break;
          }
          
          if (r > b) {
            u[i] = 'R';
            --r;
          } else {
            u[i] = 'B';
            --b;
          }
        } else {
          u[i] = 'Y';
          --y;
        }
        
      } else if (color == b) {
      
        if (u[i - 1] == 'B') {
          if (r == 0 && y == 0) {
            possible = false;
            break;
          }
          
          if (r > y) {
            u[i] = 'R';
            --r;
          } else {
            u[i] = 'Y';
            --y;
          }
        } else {
          u[i] = 'B';
          --b;
        }
        
      }
      
      if (i == n - 1 && u[0] == u[i]) {
        possible = false;
        break;
      }
    }
    
    // cheat
    if (!possible && r == 0 && y == 0 && b == 0) {
      if (u[n - 1] != u[n - 3]) {
        char temp = u[n - 1];
        u[n - 1] = u[n - 2];
        u[n - 2] = temp;
        possible = true;
      }
    }
    
    cout << "Case #" << c << ": ";
    if (possible) {
      for (int i = 0; i < u.size(); ++i) {
        cout << u[i];
      }
      cout << "\n";
    } else {
      cout << "IMPOSSIBLE\n";
    }  
  }
  
  return 0;
}

