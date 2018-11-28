#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <sstream>
using namespace std;

template<class P0, class P1> ostream &operator<<(ostream &os, const pair<P0, P1> &p) { return os << "(" << p.first << "," << p.second << ")"; }
template<class T> void dump(const T &t) { cerr << "["; for (auto it = t.begin(); it != t.end(); ++it) cerr << " " << *it; cerr << " ]" << "\n"; } 

#if 0
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/cpp_dec_float.hpp>
using namespace boost::multiprecision;
#define Integer cpp_int
#define Rational cpp_rational
#define Float cpp_dec_float_50
#endif

void flip(string &s, int i) { s[i] = ('+' + '-' - s[i]); }

int main(void) {
  int T; cin >> T;
  
  for (int iCase = 1; iCase <= T; ++iCase) {
    cout << "Case #" << iCase << ":";
    string s0; cin >> s0;
    int k; cin >> k;
    int i, j, n = s0.length();
    string target(n, '+');

    int nFlips = 0;
    for (i = 0; i < n - k + 1; ++i)
      if (s0[i]!='+') {
	++nFlips;
	for (j = 0; j < k; ++j)
	  flip(s0, i+j);
      }

    if (s0!=target)
      cout << " IMPOSSIBLE";
    else
      cout << " " << nFlips;

    cout << "\n";
  }

  return 0;
}
