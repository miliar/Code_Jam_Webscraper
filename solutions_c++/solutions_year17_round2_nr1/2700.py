#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <deque>
#include <map>
#include <iterator>

using namespace std;

double CruiseControl ( int d, vector<int> k, vector<int> s )
{
   const size_t n = k.size ();
#if 0
   cout << d << " " << n << endl;
   for ( auto x:k ) cout << x << " ";
   cout << endl;
   for ( auto x:s ) cout << x << " ";
   cout << endl;
#endif

   double t = 0;
   for ( size_t i=0; i<n; i++ )
   {
      double t2 = ( d - k[i] ) * 1.0 / s[i];
      t = max ( t, t2 );
   }

   return d / t;
}

int main ()
{
   int t;
   cin >> t;

   for ( int i = 0; i < t; ++i )
   {
      int d, n;
      cin >> d >> n;

      vector<int> k;
      vector<int> s;

      for ( int j=0; j<n; ++j )
      {
         int kk, ss;
         cin >> kk >> ss;
         k.push_back ( kk );
         s.push_back ( ss );
      }

      auto y = CruiseControl ( d, k, s );

      cout << fixed;
      cout << "Case #" << i+1 << ": ";
      cout << y;
      cout << endl;
   }
}
