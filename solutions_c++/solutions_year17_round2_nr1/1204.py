#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
  int T; scanf("%d",&T);
  for(int Case=1; Case<=T; ++Case) {
    int D,N; scanf("%d%d",&D,&N);
    double ans=-1;
    while(N--) {
      int K,S; scanf("%d%d",&K,&S);
      double tmp = (double)(D-K)/S;
      ans=max(tmp,ans);
    }
    printf("Case #%d: %lf\n",Case,D/ans);
  }
  return 0;
}
