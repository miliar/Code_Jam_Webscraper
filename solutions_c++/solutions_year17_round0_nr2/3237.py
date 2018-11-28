#include <iostream>
#include <algorithm>
#include <fstream>
#include <array>
#include <cassert>


std::ifstream  inf("in.txt",std::ios_base::in);
std::ofstream outf("out.txt",std::ios_base::out|std::ios_base::trunc);


long long int slover(long long int n)
{
    std::string s(std::to_string(n));
    s.push_back('9');

    for(std::size_t k,i = s.size()-1;i != 0;--i){
        if(s[i] < s[i-1]){
            for(k = i; s[k] != '9';++k)
                s[k] = '9';
            if(s[i-1] != 0)
                --s[i-1];
        }
    }
    s.pop_back();
    return std::atoll(s.data());
}

int main(void){

    assert(std::numeric_limits<long long int>::max() > pow(10,18));

std::ifstream  inf("in.txt",std::ios_base::in);
std::ofstream outf("out.txt",std::ios_base::out|std::ios_base::trunc);

  std::size_t num_of_tst;
  inf >> num_of_tst; //
  for(std::size_t i = 0; i < num_of_tst;++i){
      long long int bf;
      inf >> bf;
      outf << "Case #" << i+1 << ": ";
      outf << slover(bf) << "\n";
  }

  return 0;
}
