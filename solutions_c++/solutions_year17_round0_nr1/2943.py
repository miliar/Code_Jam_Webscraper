#include <iostream>
#include <fstream>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <iomanip>


using namespace std;

void solve(string & s, size_t k, ostream& out = std::cout) {
	size_t length = s.length();
	size_t answer = 0;
	for (size_t index = 0; index + k <= length; ++index) {
		if (s[index] == '-') {
			++answer;
			for (size_t j = 0; j < k; ++j) {
				if (s[index + j] == '+') {
					s[index + j] = '-';
				} else {
					s[index + j] = '+';
				}
			}
		}
	}
	for (size_t i = 0; i < length; ++i) {
		if (s[i] == '-') {
			out << "IMPOSSIBLE" << endl;
			return;
		}
	}
	out << answer << endl;
}

int main() {
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	//cout << fixed << setprecision(10);
	ofstream fout("ouput.txt");
	ifstream fin("input.txt");
	size_t cases;
	string s;
	size_t k;
	fin >> cases;
	for (size_t ccase = 0; ccase < cases; ++ccase) {
		fin >> s >> k;
		fout << "Case #" << ccase + 1 << ": ";
		solve(s, k, fout);
	}
	return 0;
}