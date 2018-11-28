#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;

long long solve(string s) {
	for (int i = 0, j = s.size() - 1; i < j; ++i) {
		if (s[i] <= s[i + 1])
			continue;

		for (int k = i + 1; k < s.size(); ++k)
			s[k] = '9';

		s[i]--;
		j = i;
		i = -1;
	}

	return stoll(s);
}

int main() {
	ifstream cin("B-large.in");
	ofstream cout("output.txt");

	int T, k;
	string s;
	cin >> T;

	for (k = 1; k <= T; ++k) {
		cin >> s;
		cout << "Case #" << k << ": " << solve(s) << endl;
	}

	cin.close();
	cout.close();
	return 0;
}