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

int dp[5][105][105][105];

void solve(){
  int n,p,g[SIZE];
  int cc[4] = {};

  scanf("%d%d",&n,&p);

  for(int i=0;i<n;i++){
    scanf("%d",g+i);
    g[i]%=p;
    cc[g[i]]++;
  }
  
  printf("%d\n",dp[p][cc[1]][cc[2]][cc[3]] + cc[0]);

}

void init(int q){

  for(int i=0;i<=102;i++){
    for(int j=0;j<=102;j++){
      for(int k=0;k<=102;k++){
        dp[q][i][j][k] = -INF;
      }
    }
  }

  dp[q][0][0][0] = 0;
  
  for(int i=0;i<=300;i++){
    for(int j=0;j<=min(i,100);j++){
      for(int k=0;k<=min(i-j,100);k++){
        if(i-j-k > 100) continue;
        assert(j>=0 && k>=0 && i-j-k>=0);
        dp[q][j+1][k][i-j-k] = max(dp[q][j+1][k][i-j-k], dp[q][j][k][i-j-k] + ((j+k*2+(i-j-k)*3)%q==0));
        dp[q][j][k+1][i-j-k] = max(dp[q][j][k+1][i-j-k], dp[q][j][k][i-j-k] + ((j+k*2+(i-j-k)*3)%q==0));
        dp[q][j][k][i-j-k+1] = max(dp[q][j][k][i-j-k+1], dp[q][j][k][i-j-k] + ((j+k*2+(i-j-k)*3)%q==0));
      }
    }
  }

}

int main(){
  int t;

  init(2);
  init(3);
  init(4);
  
  scanf("%d",&t);
  
  for(int i=1;i<=t;i++){
    printf("Case #%d: ",i);
    solve();
  }
  
  return 0;
}

