#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		long long n;
		cin >> n;
		stringstream ss;
		ss << n;
		string s = ss.str();

		string res = s;
		for (size_t i = 0; i < s.size(); ++i) {
			bool keep = true;
			for (int j = i + 1; j < s.size(); ++j) {
				if (s[j] < s[i]) {
					keep = false;
					break;
				} else if (s[j] > s[i]) {
					break;
				}
			}
			if (!keep) {
				res[i]--;
				for (int j = i + 1; j < res.size(); ++j) {
					res[j] = '9';
				}
				break;
			}
		}
		if (res[0] == '0') {
			res = res.substr(1, res.size() - 1);
		}

		cout << "Case #" << test << ": " << res << endl;
	}
}
