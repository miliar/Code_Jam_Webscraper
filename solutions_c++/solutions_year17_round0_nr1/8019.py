#include <bits/stdc++.h>
using namespace std;

int main ()  {

  freopen ( "A-large.in" , "r" , stdin );
  freopen ( "out.txt" , "w" , stdout );

  int t , k , res;
  string curr;

  cin >> t;

  for ( int it = 1 ; it <= t ; it++ ) {

    cin >> curr >> k;
    res = 0;

    for ( int i = 0 ; i < curr.size() ; i++ ) {
      if ( curr[i] == '+' ) continue;
      if ( i + k > curr.size() ) {
        res = -1;
        break;
      }
      res++;
      for ( int h = 0 ; h < k ; h++ )
        curr[i+h] = curr[i+h] == '+' ? '-' : '+';
    }

    cout << "Case #" << it << ": ";
    if ( res == -1 )
      cout << "IMPOSSIBLE";
    else
      cout << res;
    cout << "\n";

  }

  return 0;

}
