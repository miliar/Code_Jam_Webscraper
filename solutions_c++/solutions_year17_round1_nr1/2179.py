#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <stack>
using namespace std;
int R, C;
void fill(int r, int c, vector<string>& grid) {
  int left=c;
  int right=c;
  for(int i=c-1; i>=0 && grid[r][i] == '?'; i--){
      left= i;
  }
  for(int i=c+1; i<C && grid[r][i] == '?'; i++){
      right = i;
  }
  int U = r;
  int D = r;
  for(int i=r-1; i>=0; i--){
    bool flag = false;
    for(int j=left; j<=right; j++){
      if(grid[i][j] != '?'){
        flag = true;
        break;
      }
    }
    if(flag) break;
    U = i;
  }
  for(int i=r+1; i<R; i++){
    bool flag = false;
    for(int j=left; j<=right; j++){
      if(grid[i][j] != '?'){
        flag = true;
        break;
      }
    }
    if(flag) break;
    D = i;
  }
  char ch = grid[r][c];
  for(int i=left; i<=right; i++){
    for(int j=U; j<=D; j++){
      grid[j][i] = ch;
    }
  }
}

int main () {
  int T;
  cin >> T;
  for(int tc=1; tc<=T; tc++) {
     cin >> R >> C;
     vector<string> origgrid(R);
     for(int i=0; i<R; i++){
        cin >> origgrid[i];
     }
     vector<string> grid(origgrid);
     for(int i=0; i<R; i++){
      for(int j=0; j<C; j++) {
        if(grid[i][j] != '?' && grid[i][j] == origgrid[i][j]){
          fill(i, j, grid);
        }
      }
     }
   cout << "Case #" << tc << ":" << endl;
   for(int i=0; i<R; i++){
    cout << grid[i] << endl;
   }
  }
}
