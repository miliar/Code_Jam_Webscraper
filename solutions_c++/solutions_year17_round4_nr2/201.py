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


    long long int n, c, m;
    cin >> n >> c >> m;

    long long int ti[1001] = {};
    long long int num[1001] = {};
    long long int st = 0;

    for ( long long int i = 0; i < m; i++ ) {
      long long int in0, in1;
      cin >> in0 >> in1;
      in1--;
      ti[in1]++;
      in0--;
      num[in0]++;
    }
    for ( long long int i = 0; i < c; i++ ) {
      st = max( st, ti[i] );
    }

    for ( long long int ans = st;; ans++ ) {

      long long int mo_s = 0;
      for ( long long int p = n - 1; p >= 0; p-- ) {
	if ( num[p] + mo_s <= ans ) {
	  mo_s = 0;
	  continue;
	}
	mo_s = num[p] + mo_s - ans;
      }
      if ( mo_s > 0 ) continue;

      long long int cnt = 0;
      mo_s = 0;
      for ( long long int p = n - 1; p >= 0; p-- ) {
	if ( num[p] + mo_s <= ans ) {
	  mo_s = 0;
	  continue;
	}
	long long int k = num[p] + mo_s - ans;
	cnt += max( 0LL, k - mo_s );
	mo_s = k;
      }

      cout << ans << " " << cnt << endl;
      break;

    }


  }

  return 0;

}
