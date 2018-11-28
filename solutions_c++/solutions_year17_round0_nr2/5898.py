#include <stdio.h>
#include <string>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;


int main() {
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		long long input;
		scanf("%lld", &input);

		string s = to_string(input);
		//cout << s << endl;

		int idx;
		for (idx = 1; idx < (int)s.size(); ++idx) {
			// find first descending one
			if (s[idx] < s[idx-1]) break;
		}
		// Increasing original string
		if (idx == (int)s.size()) {
			cout << "Case #" << (i+1) << ": " << s << endl;
			continue;
		}

		// if number in the front is same
		while (idx > 1 && s[idx-1] == s[idx-2]) --idx;

		// if descending one has 1 infront.
		while (idx > 0 && s[idx-1] == '1') --idx;

		if (idx == 0) {
			cout << "Case #" << (i+1) << ": " << string(s.size()-1, '9') << endl;
		}
		else {
			s[idx-1] -= 1;
			cout << "Case #" << (i+1) << ": " << s.substr(0, idx) << string(s.size() - idx, '9') << endl;
		}
		//cout << "-----" << endl;
	} 
}
