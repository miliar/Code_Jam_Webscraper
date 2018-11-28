#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main() {
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int T;
	cin >> T;
	for (int test = 1; test <= T; ++test) {
		string s;
		int k, c = 0;
		cin >> s >> k;
		int q = s.size();
		for (int i = 0, ilen = q - k; i <= ilen; ++i) {
			if (s[i] == '+') continue;
			for (int j = 0; j < k; ++j) {
				s[i + j] = s[i + j] == '+' ? '-' : '+';
			}
			++c;
		}
		bool f = false;
		for (int i = 1; i < k; ++i) {
			if (s[q - k + i] == '-') {
				f = true;
			}
		}
		cout << "Case #" << test << ": ";
		if (f) {
			cout << "IMPOSSIBLE";
		} else {
			cout << c;
		}
		cout << endl;
	}
}