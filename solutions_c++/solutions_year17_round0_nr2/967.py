#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

bool loop(string num, string& ans, int lvl) {
	if (num.compare(ans) >= 0) {
		return true;
	}
	if (lvl > 0 && num[lvl] < ans[lvl-1]) {
		return false;
	}
	if (lvl >= num.size()) {
		return false;
	}
	ans[lvl] = num[lvl];
	if (!loop(num, ans, lvl+1)) {
		if (num[lvl] > '0') {
			ans[lvl] = num[lvl] - 1;
		};
		if (lvl > 0 && ans[lvl] < ans[lvl-1]) {
			ans[lvl] = '9';
			return false;
		} else {
			return true;
		}
	}
};

int main() {
	int numCases;
	ifstream fin("B-large.in");
	ofstream fout("B-sol.txt");
	fin >> numCases;
	for (int cases = 1; cases <= numCases; cases++) {
		string num;
		fin >> num;
		string ans = num;
		for (int i = 0; i < num.size(); i++) {
			ans[i] = '9';
		}
		bool sol = loop(num, ans, 0);
		while (ans[0] == '0') {
			ans.erase(0, 1);
		}
		cout << "Case #" << cases << ": " << ans << '\n';
		fout << "Case #" << cases << ": " << ans << '\n';
	}
	fin.close();
	fout.close();
	return 0;
}
