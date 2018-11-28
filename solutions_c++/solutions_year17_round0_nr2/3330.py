#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

typedef unsigned long long uli;  // 18^18

uli ipow(uli base, int exp)
{
	uli result = 1ULL;
	for (int i = 1; i <= exp; i++) {
		result *= base;
	}
	return result;
}

vector<int> Digitize(uli N) {
	vector<int> R;
	while (true) {
		uli r = N % 10ULL;
		R.push_back(int(r));
		if (N == r) break;
		N = (N - r) / 10ULL;
	}
	reverse(R.begin(), R.end());
	return R;
}

uli Summon(vector<int> D) {
	uli to_return = 0;
	for (int i = 0; i < D.size(); i++) {
		int p = D.size() - i - 1;
		uli to_add = uli(D[i]) * ipow(10ULL, p);
		to_return += to_add;
	}
	return to_return;
}

uli IsTidy(vector<int>* D) {
	for (int i = 1; i < D->size(); i++) {
		if ((*D)[i] < (*D)[i - 1]) return uli(i);
	}
	return 0ULL;
}

uli LastTidy(uli N) {
	uli n = N;
	while (true) {
		vector<int> D = Digitize(n);
		uli untidy_digit = IsTidy(&D);
		if (0ULL == untidy_digit) {
			return n;
		}
		else {
			for (int i = int(untidy_digit); i < D.size(); i++) {
				D[i] = 0;
			}
			n = Summon(D);
			n -= 1ULL;
		}
	}
}

void main() {
	string file = "B-large";
	ifstream ifile(file + ".in");
	ofstream ofile(file + ".out");
	//
	int T;
	ifile >> T;
	//
	for (int t = 1; t <= T; t++) {
		cout << "t: " << t << endl;
		uli N;
		ifile >> N;
		uli y = LastTidy(N);
		ofile << "Case #" << t << ": " << y << endl;
	}
	//
	ifile.close();
	ofile.close();
}