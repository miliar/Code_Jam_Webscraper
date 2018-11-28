#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int main() {
	int t;
	cin >> t;
	for (int testCase = 1; testCase <= t; testCase++) {
		int n, p, r;
		int tab[4] {};
		cin >> n >> p;
		for (int i = 0; i < n; i++) {
			int g;
			cin >> g;
			tab[g % p]++;
		}
		switch (p) {
			case 2:
				r = tab[1] >> 1;
				break;
			case 3:
				r = min(tab[1], tab[2]);
				r += abs(tab[1] - tab[2]) * 2 / 3;
				break;
			case 4:
				r = min(tab[1], tab[3]);
				r += tab[2] >> 1;
				{
					int d = abs(tab[1] - tab[3]);
					if (d >= 2 && tab[2] & 1) {
						r += 2;
						d -= 2;
						tab[2] &= ~1;
					}
					if (d % 4)
						r += tab[2] & 1;
					r += d * 3 / 4;
				}
				break;
		}
		cout << "Case #" << testCase << ": " << (n - r) << endl;
	}
    return 0;
}
