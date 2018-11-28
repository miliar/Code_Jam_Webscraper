#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cmath>

using namespace std;

int main(){
  char pan[1001];
  bool flip[1000];
  int T,S,K;
  scanf("%d", &T);
  int t = T;
  while(T--){
    scanf("%s %d", pan, &S);
    K = strlen(pan);
    int cnt = 0;
    int pl = 0;
    for(int i=0; i<K; i++){
      if(pan[i] == '-') flip[i] = false;
      else {
        flip[i] = true;
        pl++;
      }
    }
    if(pl == K){
      printf("Case #%d: 0\n", t - T);
      continue;
    }
    for(int i=0; i<=K-S; i++){
      if(pl == K) break;
      else if(flip[i]) continue;
      for(int j=i; j<i+S; j++){
        if(flip[j]) pl--;
        else pl++;
        flip[j] ^= true;
      }
      cnt++;
    }
    if(pl < K){
      printf("Case #%d: IMPOSSIBLE\n", t - T);
    }
    else{
      printf("Case #%d: %d\n", t - T, cnt);
    }
  }
  return 0;
}
