#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

bool get_bit(char c) {
	return c == '+' ? 1 : 0;
}

int solve(istream &cin) {
	int k = 0;
	string s;
	cin >> s >> k;

	bool flop = 0;
	int steps = 0;
	vector<bool> v = vector<bool>(s.size() + 1);
	for (int i = 0; i < s.size(); i++) {
		bool bit = get_bit(s[i]);
		flop ^= v[i];
		if (bit ^ flop != 1) {
			if (i + k <= s.size()) {
				v[i + k] = v[i + k] ^ 1;
				flop ^= 1;
				steps++;
			}
			else {
				return -1;
			}
		}
	}
	return steps;
}

int main() {
	ifstream fin("A-large.in");
	ofstream fout("t2.out");
	int t;
	fin >> t;
	for (int i = 0; i < t; i++) {
		int result = solve(fin);
		fout << "Case #" << i + 1 << ": " << (result >= 0 ? std::to_string(result) : "IMPOSSIBLE") << '\n';
	}
	return 0;
}