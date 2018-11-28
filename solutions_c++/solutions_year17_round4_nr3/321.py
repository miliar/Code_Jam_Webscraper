#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>

#include <functional>
#include <cassert>

typedef long long ll;
using namespace std;

#define debug(x) cerr << #x << " = " << x << endl;


#define mod 1000000007 //1e9+7(prime number)
#define INF 1000000000 //1e9
#define LLINF 2000000000000000000LL //2e18
#define SIZE 100010

int h,w;
char cc[10][70];
int cf[10][70],cg[10][70];
char ans[10][70];

bool memo[70][3*3*3*3*3] = {};

int dfs(int d, int *t){
  int r[5] = {};
  
  int sum = 0;
  for(int i=0;i<h;i++){
    sum *= 3;
    sum += t[i];
  }
  
  if(memo[d][sum]) return 0;
  memo[d][sum] = true;  
  
  if(d == w){
    for(int i=0;i<h;i++){
      if(t[i] == 2) return 0;
      ans[i][w] = '\0';
    }

    puts("POSSIBLE");
    for(int i=0;i<h;i++){
      printf("%s\n",ans[i]);
    }

    return 1;
  }
  
  for(int i=0;i<(1<<h);i++){
    int new_t[5] = {};

    for(int j=0;j<h;j++){
      r[j] = (i & (1<<j)) > 0;
      new_t[j] = t[j];
    }
    
    for(int j=0;j<h;j++){
      
      if(cc[j][d] == '.'){
        bool f = false;
        ans[j][d] = '.';
        
        for(int k=j-1;k>=0;k--){
          if(cc[k][d] == '-' && r[k] == 0){
            f = true;
          }
          if(cc[k][d] == '#') break;
        }

        for(int k=j+1;k<h;k++){
          if(cc[k][d] == '-' && r[k] == 0){
            f = true;
          }
          if(cc[k][d] == '#') break;
        }

        f |= t[j] == 1;
        
        if(f == false){
          new_t[j] = 2;
        }
      }
      if(cc[j][d] == '-'){
        if(r[j] == 0 && cg[j][d] >= 2){
          return 0;
        }
        if(r[j] == 1 && cf[j][d] >= 2){
          return 0;
        }

        if(r[j] == 0) ans[j][d] = '|';
        if(r[j] == 1) ans[j][d] = '-';
        
        bool f = false;
        
        for(int k=j-1;k>=0;k--){
          if(cc[k][d] == '-' && r[k] == 0){
            f = true;
          }
          if(cc[k][d] == '#') break;
        }
        
        for(int k=j+1;k<h;k++){
          if(cc[k][d] == '-' && r[k] == 0){
            f = true;
          }
          if(cc[k][d] == '#') break;
        }
        
        if(f){
          return 0;
        }

        if(r[j] == 1){
          // -
          new_t[j] = 1;
        }
      }
      if(cc[j][d] == '#'){
        ans[j][d] = '#';
        if(t[j] == 2){
          return 0;
        }
        new_t[j] = 0;
      }
    }
    
    if(dfs(d+1, new_t)) return 1;
  }
  
  return  0;
}

void solve(){
  
  scanf("%d%d",&h,&w);
  
  for(int i=0;i<h;i++){
    scanf("%s",cc[i]);
    for(int j=0;j<w;j++){
      if(cc[i][j] == '#') cg[i][j] = cf[i][j] = -INF;
      else if(cc[i][j] == '|' || cc[i][j] == '-') cg[i][j] = cf[i][j] = 1;
      else cg[i][j] = cf[i][j] = 0;

      if(cc[i][j] == '|') cc[i][j] = '-';

      if(cc[i][j] == '/' || cc[i][j] == '\\'){
        puts("Error");
        return;
      }
    }
  }
  
  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      if(cf[i][j] >= 0) cf[i][j+1] += cf[i][j];
    }
  }

  for(int i=h-1;i>=0;i--){
    for(int j=w-1;j>0;j--){
      if(cf[i][j-1] >= 0) cf[i][j-1] = max(cf[i][j-1],cf[i][j]);
    }
  }

  for(int i=0;i<h;i++){
    for(int j=0;j<w;j++){
      if(cg[i][j] >= 0) cg[i+1][j] += cg[i][j];
    }
  }

  for(int i=h-1;i>0;i--){
    for(int j=w-1;j>=0;j--){
      if(cg[i-1][j] >= 0) cg[i-1][j] = max(cg[i-1][j],cg[i][j]);
    }
  }
  
  if(h > 5){
    puts("Error!");
    return;
  }

  int t[5] = {};

  for(int i=0;i<70;i++){
    for(int j=0;j<3*3*3*3*3;j++){
      memo[i][j] = false;
    }
  }
  
  if(!dfs(0,t)){
    puts("IMPOSSIBLE");
  }
  
}

int main(){
  int t;
  
  scanf("%d",&t);
  
  for(int i=1;i<=t;i++){
    printf("Case #%d: ",i);
    solve();
  }
  
  return 0;
}

