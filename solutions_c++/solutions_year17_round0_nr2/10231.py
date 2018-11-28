#include <iostream>


unsigned long findTidy (unsigned long N){
  unsigned long i, tmp;
  unsigned int lastDig;

  for (i=N; i>9; i--){
    lastDig = i%10;
    for (tmp = i; ((lastDig >= (tmp%10)) && (tmp>0)); tmp/=10){
      lastDig = tmp%10;
    }
    if (tmp==0)
      return i;
  }

  return N;
}


int main (){
  unsigned int T;
  unsigned long N;

  std::cin >> T;

  for (unsigned int i=0; i<T; i++){
    std::cin >> N;
    std::cout <<"Case #"<<i+1<<": "<< findTidy (N) << std::endl;
  }
}
