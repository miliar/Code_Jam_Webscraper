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

double AmpleSyrup ( int k, vector<int> r, vector<int> h )
{
   const size_t n = r.size ();
   //cout << n << "/" << k << endl;
   //for ( auto x : r ) cout << x << " "; cout << endl;
   //for ( auto x : h ) cout << x << " "; cout << endl;

   vector<size_t> p (n);
   for ( size_t i=0; i<n; ++i )
      p[i] = i;

   for ( size_t i=0; i<n-1; ++i )
      for ( size_t j=i+1; j<n; ++j )
         if ( r[p[i]] < r[p[j]] )
            swap ( p[i], p[j] );

   //for ( auto x : p ) cout << r[x] << " "; cout << endl;
   //for ( auto x : p ) cout << h[x] << " "; cout << endl;

   double y = 0;

   for ( size_t i=0; i<n-k+1; ++i )
   {
      double rr = r[p[i]];
      double hh = h[p[i]];
      double yy = rr*rr + 2*rr*hh;

      vector<int> b (n);
      for ( int j=1; j<k; ++j )
      {
         double yyy = 0;
         size_t jj=0;
         for ( size_t ii=i+1; ii<n; ++ii )
         {
            if ( b[ii] ) continue;
            double rrr = r[p[ii]];
            double hhh = h[p[ii]];
            if ( yyy < rrr*hhh )
               yyy = rrr*hhh, jj = ii;
         }
         b[jj] = 1;
         yy += 2*yyy;
      }

      //cout << "*" << yy << " ";
      y = max ( y, yy );
   }

   double z = atan (1)*4;
   //cout << z << endl;
   return y*z;
}

int main ()
{
   int t;
   cin >> t;

   for ( int i = 0; i < t; ++i )
   {
      int n, k;
      cin >> n >> k;

      vector<int> r (n);
      vector<int> h (n);
      for ( int j=0; j<n; ++j )
         cin >> r[j] >> h[j];

      auto y = AmpleSyrup ( k, r, h );

      cout << "Case #" << i+1 << ": ";
      //cout << fixed << setprecision (9);
      cout << scientific << setprecision (7);
      cout << y;
      cout << endl;
   }
}
