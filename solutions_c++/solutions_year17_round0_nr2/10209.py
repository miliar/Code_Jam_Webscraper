#include <iostream>
#include <string>
using namespace std;

int is_sorted(int n) {
	string s = to_string(n);
	for (int i = 0; i<s.length()-1; i++) {
		if ((s[i]-'0')>(s[i+1]-'0')) {
			return 0;
		}
	}
	return 1;
}

int main() {
  int t, n, m;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
  	cin >> n;
  	for (int j=n; j>0; j--) {
  		if (is_sorted(j)) {
  			cout << "Case #" << i << ": " << j << endl; 
  			break;
  		}
  	}
  }
  return 0;
}
