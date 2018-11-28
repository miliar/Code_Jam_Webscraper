#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int is_tidy(int n) {
	if (n <= 9) {
		return 1;
	}
	while (n > 9) {
		int last = n % 10;
		int second = (n / 10) % 10;
		if (second > last) {
			return 0;
		}
		n /= 10;
	}
	return 1;
}

int tidy (int n) {
	while(!is_tidy(n)) {
		--n;
	}
	return n;
}

int main() {
  int t, n;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> n;  // read n and then m.
    cout << "Case #" << i << ": " << tidy(n) << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
}
