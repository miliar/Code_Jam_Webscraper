#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {

  long long int t;
  cin >> t;

  for ( long long int tt = 0; tt < t; tt++ ) {

    cout << "Case #" << tt+1 << ": ";

    long long int n, p;
    cin >> n >> p;
    vector< long long int > r, k;
    for ( long long int i = 0; i < n; i++ ) {
      long long int in;
      cin >> in;
      r.push_back( in );
      k.push_back( 0 );
    }
    vector< vector< long long int > > q;
    for ( long long int i = 0; i < n; i++ ) {
      vector< long long int > v;
      for ( long long int j = 0; j < p; j++ ) {
	long long int in;
	cin >> in;
	v.push_back( in );
      }
      sort( v.begin(), v.end() );
      q.push_back( v );
    }

    long long int ans = 0;

    while( true ) {

      bool flag = true;
      for ( long long int i = 0; i < n; i++ ) {
	if ( k[i] >= p ) {
	  flag = false;
	  break;
	}
      }
      if ( flag == false ) break;
      long long int mi = 0;
      long long int ma = 10000000;
      long long int ne = 0;
      for ( long long int i = 0; i < n; i++ ) {
	long double d = 1.00 * q[i][k[i]];
	d /= ( 1.1 * r[i] );
	long long int dd = 1LL * d;
	if ( ( q[i][k[i]] % 11 ) == 0 && ( q[i][k[i]] / 11 * 10 ) % r[i] == 0 ) dd = q[i][k[i]] / 11 * 10 / r[i] - 1;
	mi = max( mi, dd + 1 );
	d = 1.00 * q[i][k[i]];
	d /= ( 0.9 * r[i] );
	dd = 1LL * d;
	if ( ( q[i][k[i]] % 9 ) == 0 && ( q[i][k[i]] / 9 * 10 ) % r[i] == 0 ) dd = q[i][k[i]] / 9 * 10 / r[i];
	if ( dd < ma ) {
	  ma = dd;
	  ne = i;
	}
      }
      if ( mi <= ma ) {
	ans++;
	for ( long long int i = 0; i < n; i++ ) {
	  k[i]++;
	}
	continue;
      }
      k[ne]++;

    }

    cout << ans << endl;

  }

  return 0;

}
