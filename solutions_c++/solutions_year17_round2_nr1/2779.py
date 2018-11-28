#include <iostream>
using namespace std;
int main(){
  long long T;
  scanf("%lld",&T);
  for(int i=0; i<T; i++){
    long long S,n;
    double Tmax=0;
    scanf("%lld%lld",&S,&n);
    for(int j=0; j<n; j++){
      double s,v;
      scanf("%lf%lf",&s,&v);
      Tmax=max(Tmax,(double(S)-s)/v);
    }
    printf("Case #%d: %lf\n",i+1,double(S)/Tmax);
  }
}
