#include "stdafx.h"
#include <iostream>
#include <string>
#include <vector>

using namespace std;

void main() {
	int t;

	cin >> t;

	for (int i = 1; i <= t; ++i) {
		string aString;
		int K;

		cin >> aString >> K;
	    //cout << aString << " " << K << endl;

		const int aNbPancake = aString.length();
		vector<bool> aPancakes(aNbPancake);
		int j;
		int aNbSad = 0;
		int jMinSad = -1;
		int jMaxSad = -1;

		for (j = 0; j < aNbPancake; ++j) {
			switch (aString[j]) {
			case '+':
				aPancakes[j] = true;
				break;
			case '-':
				aPancakes[j] = false;
				if (aNbSad == 0) {
					jMinSad = j;
				}
				jMaxSad = j;
				aNbSad++;
				break;
			default:
				cout << "Error: Case #" << i << " incorrect string." << endl;
				return;
				break;
			}
		}

		if (K < 2 || K > aNbPancake) {
			cout << "Error: Case #" << i << " K is out of limits." << endl;
			return;
		}

		if (aNbSad == 0) {
			// Nothing to do.
			cout << "Case #" << i << ": " << 0 << endl;
			continue;
		}

		int aResult = 0;
		int m;

		while (jMaxSad - jMinSad > K - 1) {
			aResult++;

			// Flap from happy side
			bool isFlappedTwice = false;

			for (j = jMinSad + 1; j < jMinSad + K; ++j) {
				if (aPancakes[j]) {
					isFlappedTwice = true;

					if (jMaxSad - j > K - 1) {
						//for (m = jMinSad; m < j; ++m) {
						//	aPancakes[m] = !aPancakes[m];
						//}
						for (m = jMinSad + K; m < j + K; ++m) {
							aPancakes[m] = !aPancakes[m];
						}
						aResult++;

						// Find the next sad index.
						for (m = j + 1; m <= jMaxSad; ++m) {
							if (!aPancakes[m]) {
								jMinSad = m;
								break;
							}
						}
					}
					else {
						// Finish flap the first time as there is no need to flap second time.
						//for (m = jMinSad; m < j; ++m) {
						//	aPancakes[m] = !aPancakes[m];
						//}
						for (m = j; m < jMinSad + K; ++m) {
							aPancakes[m] = !aPancakes[m];
						}
						jMinSad = j;
					}
					break;
				}
			}

			if (!isFlappedTwice) {
				// The whole K is flapped. Find for the next sed index.
				for (m = jMinSad; m < jMinSad + K; ++m) {
					aPancakes[m] = !aPancakes[m];
				}

				// Find the next sad index.
				for (m = jMinSad + K; m <= jMaxSad; ++m) {
					if (!aPancakes[m]) {
						jMinSad = m;
						break;
					}
				}
			}
		}

		int aNbSadLeft = 0;

		for (m = jMinSad; m <= jMaxSad; ++m) {
			if (!aPancakes[m]) {
				aNbSadLeft++;
			}
		}

		if (aNbSadLeft) {
			aResult++;
		}

		if (aNbSadLeft && aNbSadLeft != K) {
			cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
		}
		else {
			cout << "Case #" << i << ": " << aResult << endl;
		}
	}
}
