#include<stdio.h>

void solve(int t) {
  int D, N;
  double mxs=1e18, ms;
  scanf("%d %d",&D,&N);
  for(int i=0;i<N;i++) {
    double x, s;
    scanf("%lf %lf",&x,&s);
    ms = D*s/(D-x);
    if(ms < mxs) mxs = ms;
  }
  printf("Case #%d: %.6lf\n",t,mxs);
}

int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}