#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <assert.h>
#include <cmath>

bool order_function (unsigned long long i,unsigned long long j) { return (i>j); }

int main()
{
  int n_inputs;
  std::cin >> n_inputs;

  unsigned long long n_stalls, n_people;

  for (int i = 1; i <= n_inputs; ++i)
  {
    std::vector<bool> v_stall;
    std::cin>>n_stalls>>n_people;

    v_stall.push_back(true);
    for(int i=0; i<n_stalls; ++i)
    {
      v_stall.push_back(false);
    }
    v_stall.push_back(true);

    assert(v_stall.size()==n_stalls+2);

    for(unsigned long long person=0; person<n_people; ++person)
    {
      unsigned long long lefter, righter;
      unsigned long long distance_left=n_stalls, distance_right=n_stalls;
      unsigned long long further_closer_global_stall=0, further_closer_global_pos;
      unsigned long long max=0;
      if(person==0)
      {
        lefter=0;
        righter=v_stall.size()-1;
      }

      // std::cout<<"v: ";
      // for(const auto& x:v_stall)
      //   std::cout<<x<<" ";
      // std::cout<<std::endl;

      for(unsigned long long pos=0; pos<v_stall.size(); pos++)
      {
        if(v_stall[pos]==false)
        {

          for(int iter=pos-1; iter>=0; --iter)
          {
            if(v_stall[iter]==1)
            {
              lefter=iter;
              break;
            }
          }
          for(int iter=pos+1; iter<=v_stall.size(); ++iter)
          {
            if(v_stall[iter]==1)
            {
              righter=iter;
              break;
            }
          }

          // std::cout<<pos<<" "<<lefter<<" "<<righter<<std::endl;
          distance_left= pos - lefter -1;
          distance_right= righter - pos -1;

          unsigned long long closer_stall = std::min(distance_left, distance_right);
          // std::cout<<"*"<<closer_stall<<" "<<further_closer_global_stall<<std::endl;
          unsigned long long  local_max= std::max(distance_left, distance_right);
          if(closer_stall > further_closer_global_stall)
          {
            further_closer_global_stall= closer_stall;
            further_closer_global_pos= pos;

            max=local_max;
          }
          else if(closer_stall==further_closer_global_stall)
          {
            if(local_max > max)
            {

              further_closer_global_stall= closer_stall;
              further_closer_global_pos= pos;

              max=local_max;
            }
          }
        }

      }
      v_stall[further_closer_global_pos]= true;
      // if(further_closer_global_pos > lefter)
      //   lefter= further_closer_global_pos;
      // if(further_closer_global_pos < righter)
      //   righter= further_closer_global_pos;

      // for(const auto& x:v_stall)
      //   std::cout<<x<<" ";
      //   std::cout<<std::endl;

      if(person==n_people-1)
        std::cout << "Case #" << i << ": " << max <<" "<< further_closer_global_stall << std::endl;
    }

  }
  return 0;
}
