
#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#define toDigit(c) (c-'0')

using namespace std;

int main()
{
	ifstream fin("B-small-attempt0.in");
	ofstream fout("B-small-attempt0.out");

	int T;
	string tStr;
	getline(fin, tStr);
	istringstream is(tStr);
	is >> T;

	unsigned long long int N;
	string nStr;
	for (int i = 1; i <= T; i++){
		getline(fin, nStr);
		istringstream is(nStr);
		is >> N;

		unsigned long long int maxN;
		while (N>0) {
			ostringstream os;
			os << N;
			string tempN = os.str();

			bool isTidy = true;
			for (int j = 0, leng = tempN.length(); j < leng - 1; j++) {
				int tempA = toDigit(tempN.at(j));
				int tempB = toDigit(tempN.at(j + 1));

				if (tempA > tempB) {
					isTidy = false;
					break;
				}
			}

			if (isTidy) {
				maxN = N;
				break;
			}
			--N;
		}
		fout << "Case #" << i << ": " << maxN << endl;
	}

	fin.close();
	fout.close();
    return 0;
}
