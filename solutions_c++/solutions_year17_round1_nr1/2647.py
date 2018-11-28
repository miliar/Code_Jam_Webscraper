#include <cstdio>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

const int R = 26;
const int C = 26;

char grid[R][C];
int dc[] = {1, -1};
int dr[] = {0, 0};
int n, m;

bool valid(int i, int j){
  return (i >= 0 && i < n) && (j >= 0 && j < m) && grid[i][j] == '?';
}

int main(){
  int T; cin >> T;
  for(int cs = 1; cs <= T; cs++){
    printf("Case #%d:\n", cs);
    cin >> n >> m;
    bool hasInter = false;
    cin.ignore();
    for(int i = 0; i < n; i++){
      string line; getline(cin, line);
      for(int j = 0; j < m; j++){
        grid[i][j] = line[j];
      }
    }
    for(int i = 0; i < n; i++){
      for(int j = 0; j < m; j++){
        if(grid[i][j] != '?' && j != m - 1){
          bool coloquei = false;
          for(int k = 0; k < 2 && !coloquei; k++){
            if(valid(i + dr[k], j + dc[k])){
              coloquei = true;
              grid[i + dr[k]][j + dc[k]] = grid[i][j];
              //printf("coloquei %c em %d %d\n", line[j], i + dr[k], j + dc[k]);
            }
          }
          //grid[i][j] = line[j];
        }else{
          //grid[i][j] = line[j];
        }
      }
    }

    for(int i = 0; i < n; i++){
      for(int j = 0; j < m; j++){
        if(grid[i][j] == '?'){
          if(j > 0 && grid[i][j - 1] != '?'){
            grid[i][j] = grid[i][j - 1];
          }
        }
      }
    }

    for(int i = 0; i < n; i++){
      for(int j = m - 1; j >= 0; j--){
        if(grid[i][j] == '?'){
          if(j < m - 1 && grid[i][j + 1] != '?'){
            grid[i][j] = grid[i][j + 1];
          }
        }
      }
    }

    bool go = true;
    do{
      for(int i = 0; i < n; i++){
        for(int j = 0; j < m; j++){
          if(grid[i][j] == '?' && i > 0 && grid[i - 1][j] != '?'){
            grid[i][j] = grid[i-1][j];
          }
          
          if(grid[i][j] == '?' && i < n - 1 && grid[i + 1][j] != '?'){
            grid[i][j] = grid[i+1][j];
          }
        }
      }
      if(grid[0][0] != '?') go = false;
    }while(go);

    if(m == 1){
      for(int i = 0; i < n; i++){
        if(grid[i][0] == '?'){
          if(i > 0 && grid[i - 1][0] != '?'){
            grid[i][0] = grid[i - 1][0];
          }
        }
      }

      for(int i = n - 1; i >= 0; i--){
        if(grid[i][0] == '?'){
          if(i < n - 1 && grid[i + 1][0] != '?'){
            grid[i][0] = grid[i + 1][0];
          }
        }
      }
    }
    
    
    for(int i = 0; i < n; i++){
      for(int j = 0; j < m;j++){
        printf("%c", grid[i][j]);
      }
      puts("");
    }
  }
}
