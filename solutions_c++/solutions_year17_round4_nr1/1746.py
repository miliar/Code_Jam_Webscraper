#include<stdio.h>
#include<algorithm>
using namespace std;
void solve(int t) {
  int N, P, tot = 0;
  int cnts[4] = {0,0,0,0};
  scanf("%d %d",&N,&P);
  for(int i=0;i<N;i++) {
    int d;
    scanf("%d",&d);
    cnts[ d%P ]++;
  }
  tot += cnts[0];

  if(P==2) {
    tot += (cnts[1]+1)/2;
    printf("Case #%d: %d\n",t,tot);
    return;
  }
  if(P==3) {
    tot += min(cnts[1],cnts[2]);
    tot += (max(cnts[1],cnts[2]) - min(cnts[1],cnts[2]) + 2)/3;
    printf("Case #%d: %d\n",t,tot);
    return;
  }
  if(P==4) {
    int m = min(cnts[1],cnts[3]);
    tot += m;
    cnts[1] -= m;
    cnts[3] -= m;
    m = cnts[2]/2;
    tot += m;
    cnts[2] -= m;
    
    tot += (cnts[1] + cnts[0] + 2 * cnts[2] + 3)/4;
    
    printf("Case #%d: %d\n",t,tot);
    return;
  }
}

int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}