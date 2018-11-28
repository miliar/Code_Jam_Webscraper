#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
#include <algorithm>
using namespace std;

using ll = long long int;
ifstream fin("1.in");
ofstream fout("1.out");

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int N, D;
		fin >> D >> N;
		double time = 0;
		for (int i = 0; i < N; i++) {
			int k, s;
			fin >> k >> s;
			time = max(time, (D - k) / (double)s);
		}
		fout << std::setprecision(9) << "Case #" << t << ": " << D/time << endl;
	}
}
