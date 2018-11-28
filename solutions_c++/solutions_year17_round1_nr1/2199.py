#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

void print(char grid[25][25], int R, int C){
  cout << "----" << endl;
  for (int i = 0; i < R; i++){
    for (int j = 0; j < C; j++){
      cout << grid[i][j];
    }
    cout << endl;
  }
}

int main(){

  int T;
  char grid[25][25];
  bool check[25][25];

  cin >> T;

  for (int case_test = 0; case_test < T; case_test++){
    int R, C;
    cin >> R >> C;

    for (int i = 0; i < R; i++){
      for (int j = 0; j < C; j++){
        check[i][j] = false;
        cin >> grid[i][j];
        if (grid[i][j] != '?')
          check[i][j] = true;
      }
    }

    for (int i = 0; i < R; i++){
      for (int j = 0; j < C; j++){
        if (grid[i][j] != '?' && check[i][j]){
          int k = j-1;
          int left, right;
          while (k >= 0 && grid[i][k] == '?' ){
            grid[i][k] = grid[i][j];
            k--;
          }
          left = k+1;
          k = j+1;
          while (k < C && grid[i][k] == '?' ){
            grid[i][k] = grid[i][j];
            k++;
          }
          right = k-1;
          bool check_row_up = true;
          int row_up = i-1;
          while (check_row_up && row_up >= 0){
            for (k = left; k <= right; k++){
              if (grid[row_up][k] != '?'){
                check_row_up = false;
                break;
              }
            }
            if (check_row_up){
              for (k = left; k <= right; k++){
                grid[row_up][k] = grid[i][j];
              }
            }
            row_up--;
          }
          bool check_row_down = true;
          int row_down = i+1;
          // cout << "i = " << i << endl;
          // cout << "j = " << j << endl;
          // cout << "left = " << left << endl;
          // cout << "right = " << right << endl;



          while (check_row_down && row_down < R){
            for (k = left; k <= right; k++){
              if (grid[row_down][k] != '?'){
                check_row_down = false;
                break;
              }
            }
            if (check_row_down){
              for (k = left; k <= right; k++){
                grid[row_down][k] = grid[i][j];
              }
            }
            row_down++;
          }
        }
        // print(grid,R,C);
      }
    }
    cout << "Case #" << case_test+1 << ":" << endl;
    for (int i = 0; i < R; i++){
      for (int j = 0; j < C; j++){
        cout << grid[i][j];
      }
      cout << endl;
    }
  }


  return 0;
}
