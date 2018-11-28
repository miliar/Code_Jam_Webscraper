#include <iostream>
#include <string>

using namespace std;

void flip_char(char& c) {
	if (c == '+') c = '-';
	else c = '+';
}

long long solve(string s, int k) {
	long long flips = 0;
	for (int i=0; i<=s.size()-k; ++i) {
		if (s[i] == '-') {
			++flips;
			for (int j=0; j<k; ++j) flip_char(s[i+j]);
		}
	}
	//cout << s << endl;
	for (int i=s.size()-k; i<s.size(); ++i) {
		if (s[i] == '-') return -1;
	}

	return flips;
}


int main() {
	int t;
	cin >> t;

	for (int i=1; i<=t; ++i) {
		string s; cin >> s;
		int k; cin >> k;
		long long result = solve(s, k);
		cout << "Case #" << i << ": ";
		if (result >= 0) cout << result << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
}
