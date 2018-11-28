#include <bits/stdc++.h>
using namespace std;

string vals[27];
int x, y;

void metodo() {

    for(int i = 0; i < x; i++) {
        for(int j = 0; j < y; j++) {
            if(vals[i][j] != '?') {
                for(int k = j - 1; k >= 0; k--) {
                    if(vals[i][k] != '?') break;
                    else vals[i][k] = vals[i][j];
                }
                for(int k = j + 1; k < y; k++) {
                    if(vals[i][k] != '?') break;
                    else vals[i][k] = vals[i][j];
                } 
            }
        }
    }
    bool flag = false;
    for(int i = 0; i < x; i++) {
        if(vals[i][0] == '?' && flag) {
            for(int j = 0; j < y; j++) {
                vals[i][j] = vals[i - 1][j];
            }
        } else {
            flag = true;
        }
    }
    flag = false;
    for(int i = x -1; i >= 0; i--) {
        if(vals[i][0] == '?' && flag) {
            for(int j = 0; j < y; j++) {
                vals[i][j] = vals[i + 1][j];
            }
        } else {
            flag = true;
        }
    }
}


int main () {
  int t;
  cin >> t;
  for(int i = 1; i <= t; i++) {
    cin >> x >> y;
    for(int j = 0; j < x; j++) {
        cin >> vals[j];
    }
    metodo();
    cout << "Case #" << i << ":\n";
    for(int j = 0; j < x; j++) {
        cout << vals[j] << "\n";
    }
  }
  return 0;
}