#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<pair<int, int>, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define I18F 1000000000000000000 // 10^18
#define INF 2139062143
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B

int N, _T;
int R, C;

bool valid(int i, int j){
  return i >= 0 && i < R && j >= 0 && j < C;
}

int main(){
  scanf("%d", &_T);
  for(int _t = 0; _t < _T; ++_t){
    printf("Case #%d:\n", _t + 1);

    scanf("%d%d", &R, &C);
    char G[100][100];
    for(int i = 0; i < R; ++i){
      //for(int j = 0; j < C; ++j){
        cin >> G[i];
        //scanf("%c", &G[i][j]);
      //}
    }

    for(int k = 0; k < max(R, C); ++k){
      for(int i = 0; i < R; ++i){
        for(int j = 0; j < C; ++j){
          if(G[i][j] == '?'){
            if(valid(i-1, j) && G[i-1][j] != '?') G[i][j] = G[i-1][j];
            if(valid(i+1, j) && G[i+1][j] != '?') G[i][j] = G[i+1][j];
          }
        }
      }
    }

    for(int k = 0; k < max(R, C); ++k){
      for(int i = 0; i < R; ++i){
        for(int j = 0; j < C; ++j){
          if(G[i][j] == '?'){
            if(valid(i, j-1) && G[i][j-1] != '?') G[i][j] = G[i][j-1];
            if(valid(i, j+1) && G[i][j+1] != '?') G[i][j] = G[i][j+1];
          }
        }
      }
    }

    for(int i = 0; i < R; ++i){
      for(int j = 0; j < C; ++j){
        printf("%c", G[i][j]);
      }
      printf("\n");
    }
  }
}
