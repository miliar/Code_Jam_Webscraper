#include <iostream>
#include <cstdlib>
#include <sstream>
#include <algorithm>
#include <string>

using namespace std;

typedef unsigned long long ull;

bool check( string num )
{
   string temp = num;
   sort( temp.begin(), temp.end() );
   
   //cout << temp << '\t' << num << endl;
   if( num == temp )
      return true;
   else
      return false;
}

string greedy( string number )
{
   long i = number.length() - 1;
   
   if( check(number) )
      return number;
   else
   {
      while( !check(number) )
      {
         number[i] = '9';
         number[i-1] = number[i-1] - 1; //ASCII TRICK
         i--;
      }
      if( number[0] == '0' )
         number.erase(number.begin());
   }
   return number;
}
int main()
{
   int T, i;
   ull N;

   cin >> T;
   for (i = 1; i <= T; ++i)
   {
      cin >> N; // last counted num 
         //CHECK THE EASY ONES (1-DIGIT NUMS)
         string num = to_string(N); 
         if( num.length() == 1 )
         {
            cout << "Case #" << i << ": " << num << endl;
         }
         else
         {
            //DO THE GREEDY ONE
            cout << "Case #" << i << ": " << greedy(num) << endl;
         }
   } 

   return 0;
}
