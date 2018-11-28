#include <iostream>
#include <algorithm>
#include <fstream>
#include <array>
#include <cassert>


std::ifstream  inf("in.txt",std::ios_base::in);
std::ofstream outf("out.txt",std::ios_base::out|std::ios_base::trunc);

std::string slover(std::string implement,long long int k){

    std::size_t swaps = 0;

    std::reverse(implement.begin(),implement.end());
    while(implement.back() == '+') implement.pop_back();

    while(implement.size() > k ){
        for(std::size_t i = 0; i < k;++i)
            implement[implement.size()-1-i] = implement[implement.size()-1-i] == '+' ? '-' : '+';

        while(implement.back() == '+') implement.pop_back();
        swaps += 1;
    }
    if(implement.size() == 0)
        return std::to_string(swaps);

    bool tst = true;
    for(const auto& i:implement)
        tst &= (i == '-');

    if(tst && implement.size() == k) return std::to_string(swaps+1);

    return "IMPOSSIBLE";
}


int main(void){

    assert(std::numeric_limits<long long int>::max() > pow(10,18));

std::ifstream  inf("in.txt",std::ios_base::in);
std::ofstream outf("out.txt",std::ios_base::out|std::ios_base::trunc);

  std::size_t num_of_tst;
  inf >> num_of_tst; //
  for(std::size_t i = 0; i < num_of_tst;++i){
      long long int n,k;
      std::string s;
      inf >> s >> k;
      outf << "Case #" << i+1 << ": ";
      auto ans = slover(s,k);
      outf << ans << "\n";

  }

  return 0;
}
