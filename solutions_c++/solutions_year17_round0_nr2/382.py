#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
#include <string>

string solve(const string & s) {
	// find top.
	int pos = 0;
	// first flat  123_5_5
	int first = -1;
	// last flat 12355_5_4
	int last = -1;
	while(true) {
		if ( s.size() == pos+1 ) {
			break;
		}
		if (s[pos] < s[pos+1]) {
			++pos;
			continue;
		}

		if (s[pos] == s[pos+1]) {
			if (first == -1)
				first = pos;

			++pos;
			continue;
		}

		if (s[pos] > s[pos+1]) {
			if (first == -1)
				first = pos;

			last = pos;
			break;
		}
	}

	if ((last == -1) || (first == -1))
		return s;

	string r = s;

	if (s[first] == '1') {
		r = "";
		for(int i = first + 1; i < s.size(); ++i) {
			r += '9';
		}
		return r;
	}
	else {
		--r[first];
		for(int i = first + 1; i < s.size(); ++i)
			r[i] = '9';
		return r;
	}
}

int main() {
	int n;
	cin >> n;
	string x;
	getline(cin, x);
	for (int i = 1; i <= n; ++i) {
		getline(cin, x);
		cout << "Case #" << i << ": " << solve(x) << endl;
	}
	return 0;
}