#include <bits/stdc++.h>
using namespace std;

string curr , res , ans;

bool rec ( int ind , bool f , int maxi ) {

  if ( ind >= curr.size() )
    return true;

  if ( f ) {
    rec ( ind+1 , f , 0 );
    res += '9';
    return true;
  }

  if ( curr[ind]-'0' >= maxi ) {
    if ( rec ( ind+1 , f , curr[ind]-'0' ) ) {
      res += curr[ind];
      return true;
    }
    if ( curr[ind]-'0'-1 < maxi )
      return false;
    rec ( ind+1 , true , 0 );
    res += curr[ind]-1;
    return true;
  }

  return false;
}

int main() {

  freopen ( "B-large.in" , "r" , stdin );
  freopen ( "out.txt" , "w" , stdout );

  int test;
  cin >> test;

  for ( int i = 0 ; i < test ; i++ ) {

    ans = res = "";
    cin >> curr;

    rec ( 0 , 0 , 0 );

    int it = res.size()-1;
    while ( res[it] == '0' )
      it--;
    it++;
    while ( it-- )
      ans += res[it];

    cout << "Case #"<< i+1 << ": " << ans << "\n";

  }

  return 0;

}
