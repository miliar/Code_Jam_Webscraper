#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

typedef unsigned long long ull;  // 18^18

void Place(ull N, ull K, ull* gmins, ull* gmaxs) {
	if (0ULL == K) return;
	//cout << K << endl;
	//
	ull Rs = N / 2ULL;
	ull Ls = N - Rs - 1ULL;
	ull mins = min(Ls, Rs);
	//
	ull N1 = Ls;
	ull N2 = Rs;
	ull K2 = K / 2ULL;
	ull K1 = K - K2 - 1ULL;
	Place(N2, K2, gmins, gmaxs);
	Place(N1, K1, gmins, gmaxs);
	//
	if (mins <= *gmins) {
		ull maxs = max(Ls, Rs);
		if (mins < *gmins) {
			*gmaxs = maxs;
		}
		else {
			*gmaxs = min(maxs, *gmaxs);
		}
		*gmins = mins;
	}
}

void main() {
	string file = "C-small-2-attempt0";
	ifstream ifile(file + ".in");
	ofstream ofile(file + ".out");
	//
	int T;
	ifile >> T;
	for (int t = 1; t <= T; t++) {
		cout << "t: " << t << endl;
		ull N, K;
		ifile >> N;
		ifile >> K;
		if (11 == t) {
			cout << "A" << endl;
		}
		ull gmins = 1000000000000000000ULL, gmaxs = 0ULL;
		if (N == K) {
			gmins = 0ULL;
			gmaxs = 0ULL;
		}
		else {
			Place(N, K, &gmins, &gmaxs);
		}
		ofile << "Case #" << t << ": " << gmaxs << " " << gmins << endl;
	}
	//
	ifile.close();
	ofile.close();
}