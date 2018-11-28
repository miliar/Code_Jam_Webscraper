#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {

  long long int in_t;
  cin >> in_t;
  for ( long long int for_t = 0; for_t < in_t; for_t++ ) {
    cout << "Case #" << for_t + 1 << ": ";


    string s;
    cin >> s;

    if ( s.size() == 1 ) {
      cout << s << endl;
      continue;
    }

    for ( long long int i = 0; i < s.size() + 3; i++ ) {

      for ( long long int k = 1; k < s.size(); k++ ) {

	if ( s[k-1] > s[k] ) {
	  s[k-1]--;
	  for ( long long int p = k; p < s.size(); p++ ) {
	    s[p] = '9';
	  }
	  break;
	}

      }

    }

    stringstream ss;
    ss.str( s );
    long long int ans;
    ss >> ans;
    cout << ans << endl;

  }

  return 0;

}
