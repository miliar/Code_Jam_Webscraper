#include "stdafx.h"
#include <iostream>

using namespace std;

unsigned long long TwoInPower(int thePower)
{
	if (thePower == 0) {
		return 1;
	}

	if (thePower == 1) {
		return 2;
	}

	return 2 * TwoInPower(thePower - 1);
}

void GetMinMaxLen(const unsigned long long n,
	const unsigned long long k,
	unsigned long long &theMax,
	unsigned long long &theMin)
{
	if (k == 0) {
		theMax = n;
		theMin = n;
		return;
	}
	else if (k == 1) {
		theMax = n / 2;
		theMin = (n - 1) / 2;
		return;
	}
	else {
		unsigned long long idealN = 1;
		unsigned long long idealK = 1;
		int powerN = 0;
		int powerK = 0;
		bool isFoundPowerK = false;

		while (idealN < n) {
			idealN <<= 1;
			powerN++;

			if (!isFoundPowerK && idealN >= k) {
				idealK = idealN;
				powerK = powerN;
				isFoundPowerK = true;
			}
		}

		if (idealN > n) {
			idealN >>= 1;
			powerN--;
		}

		if (idealK > k) {
			idealK >>= 1;
			powerK--;
		}

		idealN--;
		idealK--;

		unsigned long long aRestN = n - idealN;
		unsigned long long aRestK = k - idealK;
		unsigned long long aNewN = TwoInPower(powerN - powerK) - 1;
		unsigned long long aNbNewN = idealK + 1;
		const unsigned long long aRestNewN = aRestN % aNbNewN;
		unsigned long long aNewK = aRestK / aNbNewN;
		const unsigned long long aRestNewK = aRestK % aNbNewN;

		aNewN += aRestN / aNbNewN;

		if (aRestNewK) {
			aNewK++;

			if (aRestNewN >= aRestNewK) {
				aNewN++;
			}
		}

		GetMinMaxLen(aNewN, aNewK, theMax, theMin);
	}
}

void main() {
	int t;

	cin >> t;

	for (int i = 1; i <= t; ++i) {
		unsigned long long n, k;

		cin >> n >> k;
		//cout << n << " " << k << endl;

		unsigned long long aMax;
		unsigned long long aMin;

		GetMinMaxLen(n, k, aMax, aMin);

		cout << "Case #" << i << ": " << aMax << " " << aMin << endl;
	}
}
