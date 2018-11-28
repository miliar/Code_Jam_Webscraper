#include<bits/stdc++.h>
using namespace std;

int main(){
  int T;
  cin>>T;
  for(int q=1;q<=T;q++){
    double K,D,ans=0,m,h;
    int P;
    cin>>D>>P;
    for(int i=0;i<P;i++){
      cin>>m>>h;
      ans=max(ans,(D-m)/h);
    }
    printf("Case #%d: %.6lf\n",q,D/ans);
  }

  return 0;
}
