#include <iostream>  // includes cin to read from stdin and
using namespace std;  // since cin and cout are both in namespace std


void main() {
  int t, n, m, count;
  string s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
	cin >> s;
    cin >> n;
    count = 0;
    int length = s.length();
    int j;
    for(j = 0; j < s.length() - n + 1; j++) {
	  if (s[j] == '+')
		continue;
      count++;
      for(int z = 0; z < n; z++) {
        if(s[j+z] == '+')
          s[j+z] = '-'; 
        else
          s[j+z] = '+'; 
      }
    }
    int f = 1;
    for(;j < s.length(); j++) {
      if (s[j] == '-') {
        f = 0;
        cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		break;
      }
    }
    if (f)
    cout << "Case #" << i << ": " << count  << endl;
  }
}
