#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

void flip(std::string &s, int pos, int k) {
	for (int i = pos; i < pos+k; i++) {
		if (s[i] == '-')
			s[i] = '+';
		else
			s[i] = '-';
	}
}

int main() {
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
  	std::string s;
  	int k;
    cin >> s >> k;  // read n and then m.
    int count = 0;
    for (int i=0; i<s.size()-k+1; i++) {
    	if (s[i] == '-') {
    		count ++;
    		flip(s, i, k);
    		//cout << s << endl;
    	}
    }
    bool failed = false;
    for (int i=0; i<s.size(); ++i) {
    	if (s[i] == '-')
    		failed = true;
    }
    if (failed)
	    cout << "Case #" << i << ": IMPOSSIBLE" << endl;
	else 
		cout << "Case #" << i << ": " << count << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 0;
}