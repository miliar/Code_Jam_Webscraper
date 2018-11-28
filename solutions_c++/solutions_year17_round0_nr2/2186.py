#include <iostream>
#include <string>
using namespace std;
void fetch_fun(string sl,int &t_i)
{
   t_i--;
  while(t_i>0)
  {
      if(sl[t_i]!=sl[t_i-1])
      {
          return;
      }
      else
      {
          t_i--;
      }
   }
}
int main()
{
  long long number;
  int test_case;
  int t_i;
  cin>>test_case;
  for(int xa=1;xa<=test_case;xa++)
  {
         cin>>number;
         string sl = to_string(number);
         for(t_i=1;sl[t_i]!='\0';t_i++)
         {
              if(sl[t_i]<sl[t_i-1])
              {
                  fetch_fun(sl, t_i);
                  sl[t_i] = sl[t_i]-1;
                  break;
              }
          }
          t_i++;
          for(;sl[t_i]!='\0';t_i++)
          {
              sl[t_i] = '9';
          }
          number=stol(sl);
          cout<<"Case #"<<xa<<": "<<number<<"\n";
  }
  return 0;
}