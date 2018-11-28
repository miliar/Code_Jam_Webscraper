#include <iostream>
#include <fstream>
#include <string>

using std::ifstream; using std::ofstream;
using std::endl;

bool checkTidy(const unsigned long long&);

int main() {

	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");

	int T;
	fin >> T;

	for (int c = 0; c < T; ++c) {
		unsigned long long N;
		fin >> N;

		while (!checkTidy(N)) {
			--N;
		}

		fout << "Case #" << c + 1 << ": " << N << endl;
	} 

	fin.close();
	fout.close();

	return 0;
}

bool checkTidy(const unsigned long long &x) {
	std::string s = std::to_string(x);

	const int l = s.size();
	for (int i = 0; i < l; ++i) {
		if (s[i] > s[i + 1] && i + 1 != l)
			return false;
	}

	return true;
}