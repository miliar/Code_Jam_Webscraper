#include <iostream>
#include <stdint.h>
#include <iomanip>
#include <cmath>

int main(){
  int64_t T;
  std::cin>>T;
  for(int64_t i=1;i<=T;i++){
    int64_t D,N;
    std::cin>>D>>N;
    double max=INFINITY;
    for(int64_t j=0;j<N;j++){
      int64_t K,S;
      std::cin>>K>>S;
      max=std::min(max,double(S*D)/(D-K));
    }
    std::cout<<"Case #"<<i<<": "<<std::fixed<<std::setprecision(10)<<max<<std::endl;
  }
  
  return 0;
}
