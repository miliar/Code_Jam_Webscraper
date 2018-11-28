#include <cstdio>
#include <algorithm>
using namespace std;

int R[60], Q[60][60];
int MS[60][60], ME[60][60];
int pt[60];

int getMS(int x, int r){
  int ks = 0, ke = 10000000;
  while(ks <= ke){
    int m = (ks + ke) / 2;
    long long rs = (1LL * r * m * 9 + 9) / 10;
    long long re = (1LL * r * m * 11) / 10;

    if(x < rs) ke = m - 1;
    else if(x > re) ks = m + 1;
    else{ ke = m; if(ks == ke) return m; }
  }
  return -1;
}

int getME(int x, int r){
  int ks = 0, ke = 10000000;
  while(ks <= ke){
    int m = (ks + ke + 1) / 2;
    long long rs = (1LL * r * m * 9 + 9) / 10;
    long long re = (1LL * r * m * 11) / 10;

    if(x < rs) ke = m - 1;
    else if(x > re) ks = m + 1;
    else{ ks = m; if(ks == ke) return m; }
  }
  return -1;
}

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    int N, P; scanf("%d%d", &N, &P);
    for(int i = 1; i <= N; i++) scanf("%d", &R[i]);
    for(int i = 1; i <= N; i++){
      for(int j = 1; j <= P; j++) scanf("%d", &Q[i][j]);
      sort(Q[i] + 1, Q[i] + P + 1);

      for(int j = 1; j <= P; j++){
        MS[i][j] = getMS(Q[i][j], R[i]);
        ME[i][j] = getME(Q[i][j], R[i]);
      }
    }

    for(int i = 1; i <= N; i++) pt[i] = 1;

    int ans = 0;

    for(;;){
      int inval = -1;
      for(int i = 1; i <= N; i++){
        if(MS[i][pt[i]] == -1){ inval = i; break; }
      }

      if(inval != -1){
        pt[inval]++; if(pt[inval] == P + 1) break;
      }

      int maxs = 0, mine = 10000000, mins = 10000000;
      for(int i = 1; i <= N; i++){
        maxs = max(maxs, MS[i][pt[i]]);
        mins = min(mins, MS[i][pt[i]]);
        mine = min(mine, ME[i][pt[i]]);
      }

      bool fin = false;

      if(maxs <= mine){ // valid!
        ans++;
        for(int i = 1; i <= N; i++){
          pt[i]++; if(pt[i] == P + 1) fin = true;
        }
      }
      else{
        for(int i = 1; i <= N; i++){
          if(MS[i][pt[i]] == mins){
            pt[i]++; if(pt[i] == P + 1) fin = true;
          }
        }
      }

      if(fin) break;
    }

    printf("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
