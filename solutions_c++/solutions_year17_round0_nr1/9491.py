#include <iostream>
#include <string>

using namespace std;

string solve(string pattern, int length) {
	int result = 0;
	for (int i = 0; i < (int)pattern.size(); i++) {
		if (pattern[i] == '-') {
			if (i + length > (int)pattern.size()) {
				return "IMPOSSIBLE";
			}
			for (int j = 0; j < length; j++) {
				char &c = pattern[i + j];
				c = (c == '-' ? '+' : '-');
			}
			result++;
		}
	}
	return to_string(result);
}

int main() {

	int tests;
	
	cin >> tests;
	for (int i = 1; i <= tests; i++) {
		string pattern;
		int length;

		cin >> pattern >> length;
		cout << "Case #" << i << ": " << solve(pattern, length) << "\n";
	}

	return 0;
}