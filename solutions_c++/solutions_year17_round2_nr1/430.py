#include<bits/stdc++.h>
using namespace std;

int T;
int N,D;
int K[1111],S[1111];

bool check( double h ){
  double t =  D/h;
  for(int i=0;i<N;i++){
    double tt = (D-K[i])/(double)S[i];
    if( tt > t ) return false;
  }
  return true;
}

int main(){
  scanf("%d",&T);
  for(int ttt=1;ttt<=T;ttt++){
    scanf("%d%d",&D,&N);
    for(int i=0;i<N;i++)
      scanf("%d%d",&K[i],&S[i]);

    double st = 1.0, ed = 1e15;
    for(int i=0;i<100;i++){
      double h = (st+ed)/2.0;
      if( check(h) ) st = h;
      else ed = h;
    }
    printf("Case #%d: ",ttt);
    printf("%.9lf\n",st);

  }
}
