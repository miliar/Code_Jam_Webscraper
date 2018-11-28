#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

const int MAXN = 1000;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);

	int nCases;
	cin >> nCases;

	for (int cnt = 1; cnt <= nCases; cnt++) {
		int N, P;
		cin >> N >> P;

		int modArr[4] = { 0, 0, 0, 0 };

		for (int i = 0; i < N; i++) {
			int x;
			cin >> x;

			modArr[x % P]++;
		}

		int result = 0;

		if (P == 2) {
			result = modArr[0] + (modArr[1] + 1) / 2;
		}
		else if (P == 3) {
			int larger = max(modArr[1], modArr[2]);
			int smaller = min(modArr[1], modArr[2]);

			result = modArr[0] + smaller + (larger - smaller + 2) / 3;
		}
		else {
			int larger = max(modArr[1], modArr[3]);
			int smaller = min(modArr[1], modArr[3]);

			result = modArr[0] + smaller + modArr[2] / 2;

			if (modArr[2] % 2 == 0) {
				result += (larger - smaller + 3) / 4;
			}
			else {
				result += (larger - smaller + 5) / 4;
			}
		}

		cout << "Case #" << cnt << ": " << result << endl;
	}

	return 0;
}
