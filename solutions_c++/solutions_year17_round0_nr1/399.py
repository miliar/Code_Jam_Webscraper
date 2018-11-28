#include <iostream>
#include <string>
using namespace std;

int main() {

  long long int in_t;
  cin >> in_t;
  for ( long long int for_t = 0; for_t < in_t; for_t++ ) {
    cout << "Case #" << for_t + 1 << ": ";


    string s;
    long long int k;
    cin >> s >> k;

    long long int ans = 0;
    for ( long long int i = 0; i <= s.size() - k; i++ ) {

      if ( s[i] == '-' ) {
	ans++;
	for ( long long int j = 0; j < k; j++ ) {
	  if ( s[i+j] == '-' ) {
	    s[i+j] = '+';
	  }else {
	    s[i+j] = '-';
	  }
	}
      }

    }

    bool f = true;
    for ( long long int i = 0; i < s.size(); i++ ) {
      if ( s[i] == '-' ) {
	f = false;
	break;
      }
    }
    if ( f == false ) {
      cout << "IMPOSSIBLE" << endl;
    }else {
      cout << ans << endl;
    }


  }

  return 0;

}
