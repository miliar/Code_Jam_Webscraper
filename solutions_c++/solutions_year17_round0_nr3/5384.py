#include <stdio.h>

#include <vector>

using namespace std;


int main() {

  int T;

  scanf("%d",&T);
  
  for (int t = 1; t <= T; t++) {
    unsigned long long min;
    unsigned long long max;
    unsigned long long N;
    unsigned long long K;
    
    scanf("%llu %llu",&N,&K);
    
    while (K > 1) {
      
      if (K % 2 == 0) {
	N = (N)/2;
      }
      else {
	N = (N-1)/2;
      }
      K = K/2;

    }
    
    min = (N-1)/2;
    max = (N)/2;

    printf("Case #%d: %llu %llu\n",t,max,min);
  }
    
  


}
