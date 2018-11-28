#include <iostream>
#include <string.h>
#include <vector>
#include <string>
#include <limits.h>
#include <stdint.h>
#include <algorithm>
using namespace std;

string solve(string s)
{
	for (size_t i = 0; i < s.length() - 1; i++) {
		if (s[i] > s[i + 1]) {
			int64_t v = stoll(s.substr(0, i + 1)) - 1;
			string r = string(s.length() - (i + 1), '9');
			return (v > 0) ? solve(to_string(v)) + r : r;
		}
	}
	return s;
}

int main(int argc, char* argv[])
{
	if (argc >= 2) {
		FILE* fp = freopen(argv[1], "r", stdin);
	}

	int T;
	cin >> T;

	for (int i = 1; i <= T; i++) {
		int64_t N;
		cin >> N;
		cout << "Case #" << i << ": " << solve(to_string(N)) << endl;
	}

	return 0;
}
