#include <iostream>
#include <cstring>
#include<iostream>
#include<fstream>
using namespace std;
 int  main()
{
    ifstream f1;
	ofstream f2;
    f1.open("sample.in");
	f2.open("A-large.out");
    long int  testCase;
    f1>>testCase;
    for(long int  k = 0 ; k < testCase ; k++)
    {
      string pancake;
      long int  no_of_Flips = 0;
      f1>>pancake>>no_of_Flips;
      long int  len = pancake.length();
      long int  flag = 0,count_flip = 0;
      for(long int  i = 0 ; pancake[i] != '\0' ; i++)
       {
         if(pancake[i] == '-' && (i + no_of_Flips - 1) > len)
          {
             flag = 1;
             break;
          }
         else if(pancake[i] == '-' && (i + no_of_Flips - 1) <= len)
          {
             for(long int  j = i ; j < no_of_Flips + i; j++)
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
        f2<<"Case #"<<k+1<<": IMPOSSIBLE\n";
      else
        f2<<"Case #"<<k+1<<": "<<count_flip<<"\n";
    }
    f1.close();
	f2.close();
    return 0;
}
