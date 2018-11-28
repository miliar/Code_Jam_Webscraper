#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    int testCase;
    cin>>testCase;
    for(int k = 0 ; k < testCase ; k++)
    {
      string pancake;
      int no_of_Flips = 0;
      cin>>pancake>>no_of_Flips;
      int len = pancake.length();
      int flag = 0,count_flip = 0;
      for(int i = 0 ; pancake[i] != '\0' ; i++)
       {
         if(pancake[i] == '-' && (i + no_of_Flips - 1) > len)
          {
             flag = 1;
             break;
          }
         else if(pancake[i] == '-' && (i + no_of_Flips - 1) <= len)
          {
             for(int j = i ; j < no_of_Flips + i; j++)
               {
                 if(pancake[j] == '-')
                    pancake[j] = '+';
                 else
                    pancake[j] = '-';
               }
             count_flip++;
         }
       }
      if(flag == 1)
        cout<<"Case #"<<k+1<<": IMPOSSIBLE\n";
      else
        cout<<"Case #"<<k+1<<": "<<count_flip<<"\n";
    }
    return 0;
}
