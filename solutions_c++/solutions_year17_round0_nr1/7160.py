#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_set>

using namespace std;

#define DEBUG 0

fstream fin("largeA.in");
fstream fout("largeA.out");

string alg(string s, int& k) {

	int res = 0, sum = 0;
	std::vector<int> vs;
	int M = s.length();

	for (int i=0; i<M; ++i) {
		vs.push_back(0);
	}



	for (int i=0; i<M; ++i) {
		vs[i] = (s[i]=='+'? 0 : 1) + sum;
		vs[i] %= 2;
		sum += vs[i] - (i >= k - 1 ? vs[i - k + 1]: 0 );
		res += vs[i];
		if (i > M - k && vs[i] != 0) {
			return "IMPOSSIBLE";
		}
	}

	return std::to_string(res);
}


void f_main(const int& testCase) {
	string s;
	int k;
	fin >> s >> k;

	string res = alg(s, k);

	if (DEBUG) {
		cout << "Case #" << testCase << ": " << res << endl;
	}
	fout << "Case #" << testCase << ": " << res << endl;
}

int main() {
	int T;
	fin >> T;
	for (int t=0; t < T; ++t) {
		f_main(t+1);
	}
	return 0;
}
