#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

bool order_function (unsigned long long i,unsigned long long j) { return (i>j); }

int main()
{
  int n_inputs;
  std::cin >> n_inputs;

  unsigned long long input;
  unsigned long long output=0;
  for (int i = 1; i <= n_inputs; ++i)
  {
    std::cin>>input;
    output=input;

    for(unsigned long long counter=input; counter>=1; --counter)
    {
      std::vector<unsigned long long> v_digits;
      auto n=counter;

      // std::cout<<'\n'<<counter<<std::endl;
      while(n>10)
      {
        v_digits.push_back(n%10);
        n/=10;
      }
      v_digits.push_back(n);

      std::reverse(v_digits.begin(), v_digits.end());

      // for(auto& x:v_digits)
      //   std::cout<<x<<" ";
      // std::cout<<std::endl;

      int j;
      bool eq=false;
      // for(j=v_digits.size()-1; j>= 0; --j)

      for(j=0; j<v_digits.size(); ++j)
      {
        // std::cout<<std::endl<<v_digits[j] << "("<< j <<") "<<v_digits[j+1]<<"("<<j+1<<")"<<std::endl;
        if(v_digits[j] > v_digits[j+1])
        {
          unsigned mult=1;
          for(int aux=v_digits.size()-1; aux>j; --aux)
          {
            // std::cout<<"- "<<v_digits[aux]*mult<<std::endl;
            counter-= (v_digits[aux]*mult);
            mult*=10;
          }
          break;
        }
        else if(j==v_digits.size()-2)
        {
          eq=true;
        }
      }
      if(eq==true)
      {
        output=counter;
        break;
      }

    }


    std::cout << "Case #" << i << ": " << output << std::endl;

  }
  return 0;
}
