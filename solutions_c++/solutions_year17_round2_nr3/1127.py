#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int ar[110][110];
struct HORSE { 
  int E, S; 
  double ans; 
  bool operator<(const struct HORSE &t)const {
    return ans<t.ans;
  }
}h[110];

int main() {
  int T; scanf("%d",&T);
  for(int Case=1; Case<=T; ++Case) {
    int N, Q; scanf("%d%d",&N,&Q);
    for(int i=0; i<N; ++i) scanf("%d%d",&h[i].E,&h[i].S);
    for(int i=0; i<N; ++i) for(int j=0; j<N; ++j) scanf("%d",&ar[i][j]);
    printf("Case #%d:",Case);
    while(Q--) {
      int U,V; scanf("%d%d",&U,&V);
      for(int i=0; i<N-1; ++i) { // city
        double dis = ar[i][i+1];
        sort(h,h+i);
        if(i==0) h[i].ans=0; 
        else h[i].ans = h[0].ans;
        for(int j=0; j<=i; ++j) {
          if(h[j].ans==-1) continue;
          if(h[j].E>=dis) {
            h[j].ans += dis/h[j].S;
            h[j].E-=dis;
          }
          else {
            if(h[i].E>=dis) {
              h[j].E=h[i].E-dis;
              h[j].S=h[i].S;
              h[j].ans += dis/h[j].S; 
            }
            else {
              h[j].ans = -1;
            }
          }
        }
      }
      sort(h,h+N-1);
      for(int i=0; i<N-1; ++i) {
        if(h[i].ans!=-1) {
          printf(" %lf",h[i].ans);
          break;
        }
      }
    }
    puts("");
  }
  return 0;
}
