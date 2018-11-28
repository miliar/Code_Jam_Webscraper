#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <deque>
#include <map>
#include <iterator>

using namespace std;

string f ( string s )
{
   const size_t c = s.length ();

   char y = s[0];
   for ( size_t j=1; j<c; ++j )
   {
      if ( s[j] == '?' )
         s[j] = y;
      else
         y = s[j];
   }
   
   y = s[c-1];
   for ( size_t j=1; j<c; ++j )
   {
      if ( s[c-j-1] == '?' )
         s[c-j-1] = y;
      else
         y = s[c-j-1];
   }
   return s;
}

vector<string> AlphabetCake ( vector<string> x )
{
   const size_t r = x.size ();

   x[0] = f ( x[0] );
   for ( size_t i=1; i<r; ++i )
   {
      x[i] = f ( x[i] );

      if ( x[i][0] == '?' )
         x[i] = x[i-1];
   }

   for ( size_t i=1; i<r; ++i )
   {
      if ( x[r-i-1][0] == '?' )
         x[r-i-1] = x[r-i];
   }

   return x;
}

int main ()
{
   int t;
   cin >> t;

   for ( int i = 0; i < t; ++i )
   {
      int r, c;
      cin >> r >> c;

      vector<string> x;

      for ( int j=0; j<r; ++j )
      {
         string s;
         cin >> s;
         x.push_back ( s );
      }

      auto y = AlphabetCake ( x );

      cout << "Case #" << i+1 << ": ";
      cout << endl;
      for ( const auto& s : y )
         cout << s << endl;
   }
}
