#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using big_uint = unsigned long long;
using uint = unsigned;

big_uint last_tidy(big_uint u){
  for(big_uint i=u;i>0;--i){
    auto s = std::to_string(i);
    auto it = std::find(s.begin(),s.end(),'0');
    if(it != s.end()){
      auto d = std::distance(it,s.end())-1;
      big_uint base = 1;
      for(int i=0;i<d;++i) base *= 10;
      i -= i%base;
      continue;
    }
    if(std::is_sorted(s.begin(),s.end())) return i;
  }
  return -1;
}

int main(){
  big_uint n;
  std::cin >> n;
  for(big_uint i=0;i<n;++i){
    big_uint j;
    std::cin >> j;
    std::cout << "Case #" << i+1 << ": " << last_tidy(j) << std::endl;
  }
}
