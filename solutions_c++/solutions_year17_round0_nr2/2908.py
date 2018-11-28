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

void solve(string & s, ostream& out = std::cout) {
	
	size_t length = s.length();
	size_t start = 0;
	for (size_t index = 1; index < length; ++index) {
		if (s[index] < s[index - 1]) {
			for (size_t j = index; j < length; ++j) {
				s[j] = '9';
			}
			start = index;
		}
	}
	if (start == 0) {
		out << s << endl;
		return;
	}
	--start;
	for (size_t index = start; index > 0; --index) {
		if (s[index] > s[index - 1]) {
			s[index] = s[index] - 1;
			out << s << endl;
			return;
		} else {
			s[index] = '9';
		}
	}
	s[0] = s[0] - 1;
	if (s[0] != '0') {
		out << s << endl;
		return;
	}
	for (size_t index = 1; index < length; ++index) {
		out << s[index];
	}
	out << endl;
	return;
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
		fin >> s;
		fout << "Case #" << ccase + 1 << ": ";
		solve(s, fout);
	}
	return 0;
}