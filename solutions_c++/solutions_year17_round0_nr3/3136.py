#include <vector>
#include <utility>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <algorithm>
#include <string>
#include <fstream>

using namespace std;

void C(const string &file) {
	ifstream fin(file + ".in");
	ofstream fout(file + ".out");
	int nCases;
	fin >> nCases;
	for (int iCase = 1; iCase <= nCases; ++iCase) {
		fout << "Case #" << iCase << ": ";
		///////////////////CODE//HERE///////////////////
		long long n, k;
		fin >> n >> k;
		for (;;) {
			long long more, less;
			more = n / 2;
			less = (n - 1) / 2;
			if (k == 1) {
				fout << more << " " << less << endl;
				break;
			}
			n = (k % 2 == 0) ? more : less;
			k /= 2;
		}
		///////////////////CODE//ENDS///////////////////
	}
	fin.close();
	fout.close();
	cout << "Done" << endl;
	getchar();
}
