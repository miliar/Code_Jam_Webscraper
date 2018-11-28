#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <algorithm>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
	int t, n;
	string ans;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> n;  // read n.
		for (int j = n; j >= 0; j--) {
			ans = to_string(j);
			int k = 0;
			char pre = ans[k];
			for (k = 1; k < ans.length(); k++) {
				if (ans[k] < pre) break;
				pre = ans[k];
			}
			if (k == ans.length()) break;
		}
		cout << "Case #" << i << ": " << ans << endl;
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
    return 0;
}
