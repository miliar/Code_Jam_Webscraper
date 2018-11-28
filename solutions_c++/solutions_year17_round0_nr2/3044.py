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

void B(const string &file) {
	ifstream fin(file + ".in");
	ofstream fout(file + ".out");
	int nCases;
	fin >> nCases;
	for (int iCase = 1; iCase <= nCases; ++iCase) {
		fout << "Case #" << iCase << ": ";
		///////////////////CODE//HERE///////////////////
		char d[20];
		fin >> d;
		int n = strlen(d);
		int nines = n;
		for (int i = n - 1; i > 0; --i) {
			if (d[i - 1] > d[i]) {
				d[i - 1] -= 1;
				nines = i;
			}
		}
		for (int i = nines; i < n; ++i) {
			d[i] = '9';
		}
		//fout << atoll(d) << endl; // yeah I guess this works but..
		fout << (d[0] == '0' ? d + 1 : d) << endl; // hacks is better
		///////////////////CODE//ENDS///////////////////
	}
	fin.close();
	fout.close();
	cout << "Done" << endl;
	getchar();
}
