#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int find_num (string s, int m) {
  char *cstr = new char[s.length() + 1];
  strcpy(cstr, s.c_str());
  int n = 0;
  int iter = 0;
  while (true) {
      //cout << "Iteration is " << iter << endl;
      //cout << "String is " << cstr[iter] << endl;
      if (iter == s.length()) {
	return n;
      }
      if (cstr[iter] == '-') {
        if(iter + m > s.length()) {
          //cout << "Impossible " << endl;
	  return -1;
	}
	for (int i=iter; i < iter+m ; i++ ) {
	  if (cstr[i] == '-') {
	     cstr[i] = '+';
          }
	  else if (cstr[i] == '+') {
	     cstr[i] = '-';
          }
	}
	n++;
      } 
      iter++;
  }
}

int main() {
  int t, m,n;
  string s;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> s;
    cin >> m;
    n = find_num(s,m);
    if (n == -1) {
    	cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
    } 
    else {
    	cout << "Case #" << i << ": " << n << endl;
    }
  }
  return 0;
}
