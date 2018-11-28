#include <bits/stdc++.h>
using namespace std ;

int main() {
  ifstream cin("p11_large.in") ;
  ofstream cout("p11_large.out") ;
  int t ;
  cin >> t ;
  for(int tc = 1 ; tc <= t ; tc ++) {
    int r , c ;
    cin >> r >> c ;
    char grid[r][c] ;
    for(int i = 0 ; i < r ; i ++) {
      for(int j = 0 ; j < c ; j ++)
        cin >> grid[i][j] ;
    }
    cout << "Case #" << tc << ":\n" ;
    int up = -1 , down = -1 ;
    for(int i = 0 ; i < r ; i ++) {
      int pre1 = -1 , pre2 = -1 ;
      bool empty = true ;
      char ch = '_' ;
      for(int j = 0 ; j < c ; j ++) {
        if(grid[i][j] == '?') {
          if(pre1 == -1)
            pre1 = j ;
          else
            pre2 = j ;
        }
        else {
          if(pre1 != -1) {
            if(pre2 != -1) {
              for(int k = pre1 ; k <= pre2 ; k ++)
                grid[i][k] = grid[i][j] ;
            } else {
              grid[i][pre1] = grid[i][j] ;
            }
          }
          pre1 = -1 ;
          pre2 = -1 ;
          empty = false ;
          ch = grid[i][j] ;
        }
        if(j == c - 1 && pre1 != -1 && ch != '_') {
          if(pre2 != -1) {
            for(int k = pre1 ; k <= pre2 ; k ++)
              grid[i][k] = ch ;
          } else {
            grid[i][pre1] = ch ;
          }
          pre1 = -1 ;
          pre2 = -1 ;
        }
      }
      if(empty) {
        if(up == -1)
          up = i ;
        else
          down = i ;
      } else {
        if(up != -1) {
          if(down == -1) {
            for(int l = 0 ; l < c ; l ++)
              grid[up][l] = grid[i][l] ;
          } else {
            for(int m = up ; m <= down ; m ++) {
              for(int l = 0 ; l < c ; l ++)
                grid[m][l] = grid[i][l] ;
            }
          }
        }
        up = -1 ;
        down = -1 ;
      }
    }
    if(up != -1) {
      if(down == -1) {
        for(int l = 0 ; l < c ; l ++)
          grid[up][l] = grid[up - 1][l] ;
      } else {
        for(int m = up ; m <= down ; m ++) {
          for(int l = 0 ; l < c ; l ++)
            grid[m][l] = grid[m - 1][l] ;
        }
      }
    }
    for(int i = 0 ; i < r ; i ++) {
      for(int j = 0 ; j < c ; j ++)
        cout << grid[i][j] ;
      cout << "\n" ;
    }
  }
  return 0 ;
}
