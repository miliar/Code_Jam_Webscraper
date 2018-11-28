#include <iostream>
#include <algorithm>
#include <fstream>
#include <array>
#include <cassert>


std::ifstream  inf("in.txt",std::ios_base::in);
std::ofstream outf("out.txt",std::ios_base::out|std::ios_base::trunc);


std::pair<long long int,long long int> slover(long long int n,long long int k)
{
    if(n == k)
        return  {0,0};
   std::pair<long long int,long long int> nw_even,nw_odd;
   std::pair<long long int,long long int> old_even,old_odd;

    old_even.first = old_odd.first = n;
    old_even.second = 0; old_odd.second = 1;
    if((n%2) == 0) std::swap(old_even,old_odd);

   long long int iter = 1;
   while(iter < k) {

       bool odd_to_odd = false; // even odd

       if(((old_odd.first - 1) >> 1) & 1){
           odd_to_odd =  true;
       }


       long long int mmax = std::max(old_even.first,old_odd.first),
                mmin = std::min(old_even.first,old_odd.first);

       if(mmax&1){
           nw_even.first = (mmin-1)/2;
           nw_odd.first = mmin - 1 - nw_even.first;
           if(nw_even.first&1) std::swap(nw_even.first,nw_odd.first);
           if(nw_even.first < 0) nw_even.first = 0;
           if(nw_odd.first < 0) nw_odd.first = 0;

       }
       else{
           nw_even.first = (mmax-1)/2;
           nw_odd.first =  mmax-1 - nw_even.first;
           if(nw_even.first&1) std::swap(nw_even.first,nw_odd.first);
           if(nw_even.first < 0) nw_even.first = 0;
           if(nw_odd.first < 0) nw_odd.first = 0;

       }

       nw_even.second = !odd_to_odd  * old_odd.second * 2  + old_even.second;
       nw_odd.second =  odd_to_odd * old_odd.second * 2  + old_even.second;

       k-= iter;
       iter *= 2;

       assert((nw_even.second + nw_odd.second) == iter);
       std::swap(old_even,nw_even);
       std::swap(old_odd,nw_odd);
       nw_even.second = nw_odd.second = 0;
   }

    if(old_even.first > old_odd.first) {
        if (k > old_even.second)
            return {(old_odd.first - 1) / 2, (old_odd.first - 1) / 2};
        return {(old_even.first - 1) / 2,old_even.first - 1 - (old_even.first - 1) / 2 };
    }
    else{
        if(k > old_odd.second)
            return  {(old_even.first - 1) / 2,old_even.first - 1 - (old_even.first - 1) / 2 };
        else
            return {(old_odd.first - 1) / 2, (old_odd.first - 1) / 2};
    }

    return {0,0};
}

int main(void){

    assert(std::numeric_limits<long long int>::max() > pow(10,18));

std::ifstream  inf("in.txt",std::ios_base::in);
std::ofstream outf("out.txt",std::ios_base::out|std::ios_base::trunc);

  std::size_t num_of_tst;
  inf >> num_of_tst; //
  for(std::size_t i = 0; i < num_of_tst;++i){
      long long int n,k;
      inf >> n >> k;
      outf << "Case #" << i+1 << ": ";
      auto ans = slover(n,k);
      outf << std::max(ans.first,ans.second) << ' ' << std::min(ans.first,ans.second) << "\n";

  }

  return 0;
}
