#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <deque>
#include <map>
#include <iterator>

using namespace std;

pair<long long,long long> BathroomStalls ( long long n, long long k )
{
   map<long long, long long> m;
   m.insert ( make_pair ( n, 1 ) );

   while ( k > 0 )
   {
      auto it = m.end ();
      --it;
      auto a = it->first;
      auto c = it->second;
      //cout << a << "," << c << " ";

      auto b1 = ( a - 1 ) / 2;
      auto b2 = a - b1 - 1;
      //cout << b1 << "," << b2 << " ";

      if ( c >= k )
         return make_pair ( b2, b1 );

      m[b1] += c;
      m[b2] += c;

      m.erase ( it );
      //cout << m.size () << " ";
      //cout << endl;

      k -= c;
   }

   return make_pair ( 0, 0 );
}

int main ()
{
   int n;
   cin >> n;

   for ( int i = 0; i < n; ++i )
   {
      long long m, k;
      cin >> m >> k;

      auto result = BathroomStalls ( m, k );

      cout << "Case #" << i+1 << ": ";
      cout << result.first << " " << result.second;
      cout << endl;
   }
}
