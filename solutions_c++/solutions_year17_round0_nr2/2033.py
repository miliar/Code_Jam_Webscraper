#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <deque>

using namespace std;

long long TidyNumbers ( long long n )
{
   deque<int> v;
   for ( auto k = n; k > 0; k /= 10 )
      v.push_front ( k % 10 );

   //for ( auto x : v ) cout << x;
   //cout << endl;

   const size_t m = v.size ();
   size_t p = 0;
   for ( size_t i=1; i<m; ++i )
   {
      if ( v[m-i-1] <= v[m-i] ) continue;

      --v[m-i-1];
      p = i;
   }

   //cout << p << " ";

   for ( size_t i=0; i<p; ++i )
      v[m-i-1] = 9;

   //for ( auto x : v ) cout << x;
   //cout << endl;

   long long y = 0;

   for ( auto x : v )
   {
      y *= 10;
      y += x;
   }

   return y;
}

int main ( int argc, char* argv[] )
{
   if ( argc < 2 )
   {
      cerr << "usage: " << argv[0] << " <dataset>" << endl;
      return 1;
   }

   ifstream is ( argv[1] );
   int n;
   is >> n;

   for ( int i = 0; i < n; ++i )
   {
      long long k;
      is >> k;

      auto result = TidyNumbers ( k );

      cout << "Case #" << i+1 << ": ";
      cout << result;
      cout << endl;
   }
}
