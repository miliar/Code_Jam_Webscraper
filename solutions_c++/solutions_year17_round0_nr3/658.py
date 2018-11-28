#include <iostream>
#include <map>
#include <stdint.h>

void test(int64_t N,int64_t K){
  std::map<int64_t,int64_t> open;
  open[N]=1;
  while(true){
    int64_t size=open.rbegin()->first;
    int64_t count=open.rbegin()->second;
    if(K<=count){
      std::cout<<size/2<<" "<<(size-1)/2<<std::endl;
      return;
    }else{
      open[size/2]+=count;
      open[(size-1)/2]+=count;
      open.erase(size);
      K-=count;
    }
  }
}

int main(){
  int64_t T;
  std::cin>>T;
  for(int64_t i=1;i<=T;i++){
    int64_t N,K;
    std::cin>>N>>K;
    std::cout<<"Case #"<<i<<": ";
    test(N,K);
  }
  return 0;
}
