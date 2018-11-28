#include <cstdio>
#include <iostream>
using namespace std;

int main(){
  int T; scanf("%d\n",&T);
  for(int i = 1; i <= T; i++){
    int D,N; scanf("%d %d\n",&D,&N);
    int K,S;double t = 0.0;
    while(N--){
      double temp;
      scanf("%d %d\n",&K,&S);
      temp = (double)(D-K)/(double)S;
      //cout << temp << endl;
      if(temp - t >= 1e-10){
        t = temp;
      }
    }
    printf("Case #%d: %.10lf\n",i,D/t );
  }
  return 0;
}
