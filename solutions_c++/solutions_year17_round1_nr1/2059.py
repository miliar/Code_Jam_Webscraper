#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <utility>

#define MAXX 30
#define pb push_back
#define all(v) v.begin(), v.end()
#define CLR(x) memset((x), 0, sizeof((x)))
#define ll long long int
#define Fr first
#define Sc second

using namespace std;

char grid[MAXX][MAXX];
int R, C;
bool done_min[1000];
bool done[1000];

void fill_min(char symbol){


  int l = 1000;
  int r = -10;
  int top = 1000;
  int btm = -1000;
  for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++){
      if(grid[i][j] == symbol){
        l = min(l, j);
        r = max(r, j);
        top = min(top, i);
        btm = max(btm, i);
      }
    }
  }
  for(int i = top; i <= btm; i++){
    for(int j = l; j <= r; j++){
      if(grid[i][j] == '?') grid[i][j] = symbol;
    }
  }
}

bool check(int top, int btm, int l, int r){
  bool ok = true;
  for(int i = top; i < btm; i++){
    for(int j = l; j < r; j++){
      if(grid[i][j] != '?') return false;
    }
  }

  return true;
}

bool verify(char symbol){
  int l = 1000;
  int r = -10;
  int top = 1000;
  int btm = -1000;
  for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++){
      if(grid[i][j] == symbol){
        l = min(l, j);
        r = max(r, j);
        top = min(top, i);
        btm = max(btm, i);
      }
    }
  }

  for(int i = top; i <= btm; i++){
    for(int j = l; j <= r; j++){
      if(grid[i][j] != symbol) return false;
    }
  }

  return true;

}

void fill_rest(char symbol){
  int l = 1000;
  int r = -10;
  int top = 1000;
  int btm = -1000;
  for(int i = 0; i < R; i++){
    for(int j = 0; j < C; j++){
      if(grid[i][j] == symbol){
        l = min(l, j);
        r = max(r, j);
        top = min(top, i);
        btm = max(btm, i);
      }
    }
  }

  while(top > 0 && check(top-1, top, l, r+1)){
    //printf("Expanding %c up\n", symbol);
    for(int j = l; j <= r; j++){
      if(grid[top-1][j] == '?') grid[top-1][j] = symbol;
    }
    top--;
  }
  while(l > 0 && check(top, btm+1, l-1, l)){
    //printf("Expanding %c left\n", symbol);
    for(int j = top; j <= btm; j++){
      if(grid[j][l-1] == '?') grid[j][l-1] = symbol;
    }
    l--;
  }
  while(r < C-1 && check(top, btm+1, r+1, r+2)){
    //printf("Expanding %c right\n", symbol);
    for(int j = top; j <= btm; j++){
      if(grid[j][r+1] == '?') grid[j][r+1] = symbol;
    }
    r++;
  }

  while(btm <R-1 && check(btm+1, btm+2, l, r+1)){
    //printf("Expanding %c down\n", symbol);
    for(int j = l; j <= r; j++){
      if(grid[btm+1][j] == '?') grid[btm+1][j] = symbol;
    }
    btm++;
  }

  return;
}

int main(){

  int i, j, k, kases;

  freopen("io/gcj17_1a_A.in", "r", stdin);
  freopen("io/gcj17_1a_A.out", "w", stdout);

  scanf("%d", &kases);

  for(k = 1; k <= kases; k++){
    scanf("%d %d", &R, &C);
    CLR(done_min);
    CLR(done);

    for( i = 0; i < R; i++){
      scanf("%s", grid[i]);
    }

    for(i = 0; i < R; i++){
      for(j = 0; j < C; j++){
        if(grid[i][j] != '?' && !done_min[grid[i][j]]){
          done_min[grid[i][j]] = true;
          fill_min(grid[i][j]);
        }
      }
    }


    for(i = 0; i < R; i++){
      for(j = 0; j < C; j++){
        if(grid[i][j] != '?' && !done[grid[i][j]]){
          done[grid[i][j]] = true;
          fill_rest(grid[i][j]);
        }
      }
    }

    for(i = 0; i < R; i++){
      for(j = 0; j < C; j++){
          if(!verify(grid[i][j]) || grid[i][j] == '?'){
            printf("ERROR: symbol %c\n", grid[i][j]);
          }
      }
    }

    printf("Case #%d:\n", k);
    for(i = 0; i < R; i++){
      printf("%s\n", grid[i]);
    }



  }

  return 0;
}
