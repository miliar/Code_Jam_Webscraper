#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

long long int hd, ad, hk, ak, b, d, ans;

void kansu( long long int bb, long long int dd, long long int k ) {

  long long int hhd = hd;
  long long int hhk = hk;
  long long int bbb = 0;
  long long int ddd = 0;
  bool f = false;

  while( true ) {

    long long int aad = ad + b * bbb;
    long long int aak = max( ak - d * ddd, 0LL );

    if ( hhk <= aad ) {
      ans = min( ans, k + 1 );
      return;
    }
    if ( d > 0 && ddd < dd && hhd > max( aak - d, 0LL ) ) {
      ddd++;
      aak = max( ak - d * ddd, 0LL );
      f = false;
    }else if ( hhd <= aak ) {
      if ( f == true ) return;
      hhd = hd;
      f = true;
    }else if ( b > 0 && bbb < bb ) {
      bbb++;
      f = false;
    }else {
      hhk -= aad;
      f = false;
    }
    hhd -= aak;
    if ( hhd <= 0 ) return;
    k++;

  }

  return;

}

int main() {

  long long int t;
  cin >> t;

  for ( long long int tt = 0; tt < t; tt++ ) {

    cout << "Case #" << tt+1 << ": ";

    cin >> hd >> ad >> hk >> ak >> b >> d;
    ans = 100000000;

    for ( long long int bb = 0; bb <= 20; bb++ ) {

      for ( long long int dd = 0;; dd++ ) {
	kansu( bb, dd, 0 );
	if ( d * dd >= ak || d == 0 ) break;
      }
      if ( b == 0 ) break;

    }

    if ( ans == 100000000 ) {
      cout << "IMPOSSIBLE" << endl;
    }else {
      cout << ans << endl;
    }


  }

  return 0;

}
