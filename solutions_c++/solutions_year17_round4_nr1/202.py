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

    long long int a[4] = {};
    for ( long long int i = 0; i < n; i++ ){
      long long int in;
      cin >> in;
      a[(in%p)]++;
    }

    long long int ans = 0;

    if ( p == 2 ) {
      ans = a[0] + a[1] / 2 + a[1] % 2;
    }else if ( p == 3 ) {
      long long int k = min( a[1], a[2] );
      long long int m = max( a[1] - k, a[2] - k );
      ans = a[0] + k + m / 3;
      if ( ( m % 3 ) != 0 ) ans++;
    }else if ( p == 4 ) {
      cout << "44444444444" << endl;
      continue;
      ans = a[0];
      long long int k = min( a[1],a[3] );
      ans += k;
      long long int m = max( a[1]-k, a[3]-k );
      ans += a[2] / 2;
      a[2] = a[2] % 2;
      if ( a[2] == 1 && m >= 2 ) {
	ans++;
	m -= 2;
	a[2] = 0;
      }
      ans += m / 4;
      m %= 4;
      if ( m + a[2] != 0 ) ans++;
    }

    cout << ans << endl;


  }

  return 0;

}
