#include <iostream>
#include <string>
#include <fstream>

using namespace std;

class Solution {
public:
	string solve(string s, int k) {

		int n = s.size();
		int res = 0;

		for (int i = 0; i <= n - k; ++i) {
			if (s[i] == '+') {
				continue;
			}

			res += 1;
			for (int j = 0; j < k; ++j) {
				s[i + j] = s[i + j] == '+' ? '-' : '+';
			}
		}

		for (int i = n - k + 1; i < n; ++i) {
			if (s[i] == '-') {
				return "IMPOSSIBLE";
			}
		}

		return to_string(res);
	}
};

int main() {

	Solution solution;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int m, n;
	string s;

	fin >> m;

	for (int i = 0; i < m; ++i) {
		fin >> s >> n;
		fout << "Case #" << i + 1 << ": " << solution.solve(s, n) << endl;
	}

	return 0;
}
