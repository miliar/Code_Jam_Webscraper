#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	const char letters[6] = {'R', 'O', 'Y', 'G', 'B', 'V'};
	int t;
	cin >> t;
	for (int testCase = 1; testCase <= t; testCase++) {
		bool ok = true;
		int n, unicorns[6];
		string result, consecutives[3] = {"R", "Y", "B"};
		cin >> n;
		result.reserve(n);
		for (int i = 0; i < 6; i++) {
			cin >> unicorns[i];
		}
		for (int i = 1; i < 6; i += 2) {
			if (unicorns[i]) {
				int other = (i + 3) % 6;
				int cons = other >> 1;
				if (unicorns[other] <= unicorns[i]) {
					ok = false;
					if (unicorns[other] == unicorns[i] && unicorns[other] + unicorns[i] == n) {
						while (unicorns[i]) {
							unicorns[i]--;
							unicorns[other]--;
							result += letters[i];
							result += letters[other];
						}
					} else {
						result = "IMPOSSIBLE";
					}
					break;
				} else {
					consecutives[cons].reserve(unicorns[i] << 1 | 1);
					while (unicorns[i]) {
						unicorns[i]--;
						unicorns[other]--;
						consecutives[cons] += letters[i];
						consecutives[cons] += letters[other];
					}
				}
			}
		}
		if (ok) {
			unicorns[1] = unicorns[2];
			unicorns[2] = unicorns[4];
			if (unicorns[0] > unicorns[1] + unicorns[2] || unicorns[1] > unicorns[0] + unicorns[2] || unicorns[2] > unicorns[1] + unicorns[0]) {
				result = "IMPOSSIBLE";
			} else {
				int uMax = 0;
				for (int i = 1; i < 3; i++) {
					if (unicorns[i] > unicorns[uMax])
						uMax = i;
				}
				while ((int)result.size() < n) {
					if (unicorns[uMax]) {
						unicorns[uMax]--;
						result += consecutives[uMax];
						consecutives[uMax] = letters[uMax << 1];
						int uMax2 = !uMax;
						for (int j = 0; j < 3; j++) {
							if (j != uMax && unicorns[j] > unicorns[uMax2])
								uMax2 = j;
						}
						result += consecutives[uMax2];
						consecutives[uMax2] = letters[uMax2 << 1];
						unicorns[uMax2]--;
					} else {
						for (int j = 0; j < 3; j++) {
							if (unicorns[j] && result.back() != letters[j << 1]) {
								unicorns[j]--;
								result += consecutives[j];
								consecutives[j] = letters[j << 1];
							}
						}
					}
				}
			}
		}
		cout << "Case #" << testCase << ": ";
		cout << result << '\n';
	}
	return 0;
}
