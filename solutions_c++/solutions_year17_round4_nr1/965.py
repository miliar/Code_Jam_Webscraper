#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int memo2[101][101][2];
int memo3[101][101][101][3];
int memo4[101][101][101][101][4];

int solve2(int r0, int r1, int rem){
  int &ret = memo2[r0][r1][rem];

  if(ret == -1){
    ret = 0;
    int aux = 0;
    if(rem == 0) aux = 1;

    if(r0 > 0) ret = max(ret, aux + solve2(r0 - 1, r1, rem));
    if(r1 > 0) ret = max(ret, aux + solve2(r0, r1 - 1, (rem + 1) % 2));
  }

  return ret;
}

int solve3(int r0, int r1, int r2, int rem){
  int &ret = memo3[r0][r1][r2][rem];

  if(ret == -1){
    ret = 0;
    int aux = 0;
    if(rem == 0) aux = 1;

    if(r0 > 0) ret = max(ret, aux + solve3(r0 - 1, r1, r2, rem));
    if(r1 > 0) ret = max(ret, aux + solve3(r0, r1 - 1, r2, (rem + 1) % 3));
    if(r2 > 0) ret = max(ret, aux + solve3(r0, r1, r2 - 1, (rem + 2) % 3));
  }

  return ret;
}

int solve4(int r0, int r1, int r2, int r3, int rem){
  int &ret = memo4[r0][r1][r2][r3][rem];

  if(ret == -1){
    ret = 0;
    int aux = 0;
    if(rem == 0) aux = 1;

    if(r0 > 0) ret = max(ret, aux + solve4(r0 - 1, r1, r2, r3, rem));
    if(r1 > 0) ret = max(ret, aux + solve4(r0, r1 - 1, r2, r3, (rem + 1) % 4));
    if(r2 > 0) ret = max(ret, aux + solve4(r0, r1, r2 - 1, r3, (rem + 2) % 4));
    if(r3 > 0) ret = max(ret, aux + solve4(r0, r1, r2, r3 - 1, (rem + 3) % 4));
  }

  return ret;
}

int main(){
  int T;
  int cont[4];

  scanf("%d",&T);

  memset(memo2, -1, sizeof memo2);
  memset(memo3, -1, sizeof memo3);
  memset(memo4, -1, sizeof memo4);

  for(int tc = 1;tc <= T;++tc){
    int N,P;
    scanf("%d %d",&N,&P);

    memset(cont,0,sizeof cont);

    for(int i = 0,a;i < N;++i){
      scanf("%d", &a);
      a %= P;
      ++cont[a];
    }

    int ans;

    if(P == 2){
      ans = solve2(cont[0],cont[1],0);
    }else if(P == 3){
      ans = solve3(cont[0],cont[1],cont[2],0);
    }else{
      ans = solve4(cont[0],cont[1],cont[2],cont[3],0);
    }

    printf("Case #%d: %d\n", tc, ans);
  }

  return 0;
}
