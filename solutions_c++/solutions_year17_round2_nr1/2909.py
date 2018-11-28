#include "includes.h"

////////////////////////HELPER///HERE///////////////////////////////
//``````````````````````````````````````````````````````````````````

//..................................................................
////////////////////////HELPER///ENDS///////////////////////////////

void A(const string &file) {
	ifstream fin(file + ".in");
	ofstream fout(file + ".out");
	int nCases;
	fin >> nCases;
	fout << setprecision(6) << std::fixed;
	for (int iCase = 1; iCase <= nCases; ++iCase) {
		fout << "Case #" << iCase << ": ";
		/////////////////////////HERE/////////////////////////////////////////
		/////////////////////MAIN///CODE////////////////////////
		int d, n;
		fin >> d >> n;
		veci k(n), s(n);
		for (int i = 0; i < n; ++i) {
			fin >> k[i] >> s[i];
		}
		vecd t(n);
		for (int i = 0; i < n; ++i) {
			t[i] = double(d - k[i]) / s[i];
		}
		double t0 = *max_element(t.begin(), t.end());
		fout << d / t0 << ENDL;
		//////////////////////MAIN///CODE///////////////////////////
		/////////////////////////ENDS//////////////////////////////////////
	}
	fin.close();
	fout.close();
	cout << "Done" << endl;
	getchar();
}
