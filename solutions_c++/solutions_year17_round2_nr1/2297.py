#include<stdio.h>

void solve(){
  int D, N; scanf("%d %d", &D, &N);
  double best = 0;
  for(int i=0; i<N; i++){
    int K, S;
    scanf("%d %d", &K, &S);
    double now = double(D-K)/S;
    if(now > best)
      best = now;
  }
  printf("%lf\n", D/best);
}

int main(int agrc, char*argv[]){
  int T; scanf("%d", &T);
  for(int tc=1; tc<=T; tc++){
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
