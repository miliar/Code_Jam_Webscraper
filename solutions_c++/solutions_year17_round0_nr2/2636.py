#include "stdafx.h"
#include <iostream>
#include <string> 

using namespace std;

void main() {
	int t;

	cin >> t;

	for (int i = 1; i <= t; ++i) {
		unsigned long long n;

		cin >> n;
		//cout << n << endl;
		string aStrN = to_string(n);
		const int aLen = aStrN.length();
		int j;
		string aTidyNumber;
		int aHigherDigit = '9';

		aTidyNumber = aStrN;

		for (j = aLen - 1; j >= 0; --j) {
			if (aTidyNumber[j] < aHigherDigit) {
				// Decrease the higher number.
				aHigherDigit = aTidyNumber[j];
			}
			else if (aTidyNumber[j] > aHigherDigit) {
				// Decrease the corresponding digit in tidy number.
				aTidyNumber[j] = aTidyNumber[j] - 1;

				int k;

				for (k = j + 1; k < aLen; ++k) {
					aTidyNumber[k] = '9';
				}
				aHigherDigit = aTidyNumber[j];
			}
		}

		if (aTidyNumber[0] == '0') {
			aTidyNumber.clear();
			aTidyNumber.resize(aLen - 1, '9');
		}

		cout << "Case #" << i << ": " << aTidyNumber << endl;
	}
}
