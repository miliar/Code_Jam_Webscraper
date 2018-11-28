#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <deque>
#include <map>
#include <cmath>
#include <iterator>
#include <iomanip>

using namespace std;

int f ( vector<int> c, vector<int> d )
{
   const size_t n = c.size ();
   vector<int> x (1440);

   for ( size_t i=0; i<n; ++i )
      for ( int j=c[i]; j<d[i]; ++j )
         x[j] = 1;
   
   for ( size_t i=0; i<720; ++i )
      if ( x[i] == 1 && x[i+720] == 1 )
         return 4;

   return 2;
}

int ParentingPartnering ( vector<int> c, vector<int> d, vector<int> j, vector<int> k )
{
   //for ( auto x : c ) cout << x << " "; cout << endl;
   //for ( auto x : d ) cout << x << " "; cout << endl;
   //for ( auto x : j ) cout << x << " "; cout << endl;
   //for ( auto x : k ) cout << x << " "; cout << endl;

   if ( !c.empty () && j.empty () )
      return f ( c, d );

   if ( c.empty () &&  !j.empty () )
      return f ( j, k );

   return 2;
}

int main ()
{
   int t;
   cin >> t;

   for ( int i = 0; i < t; ++i )
   {
      int ac, aj;
      cin >> ac >> aj;

      vector<int> c (ac);
      vector<int> d (ac);
      vector<int> j (aj);
      vector<int> k (aj);
      for ( int ii=0; ii<ac; ++ii )
         cin >> c[ii] >> d[ii];
      for ( int ii=0; ii<aj; ++ii )
         cin >> j[ii] >> k[ii];

      auto y = ParentingPartnering ( c, d, j, k );

      cout << "Case #" << i+1 << ": ";
      cout << y;
      cout << endl;
   }
}
