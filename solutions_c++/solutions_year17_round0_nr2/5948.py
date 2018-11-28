#include <iostream>
using namespace std;

typedef signed long long longf;
typedef unsigned long long ulongf;

bool isTidy(ulongf num) {
	ulongf last = num % 10;
	ulongf newLast;
	while (num != 0) {
		num = num / 10;
		newLast = num % 10;
		if (newLast > last) return false;
		last = newLast;
	}
	return true;
}

ulongf n;

int t;

int main() {
	cin >> t;

	for (int tt = 1; tt <= t; ++tt) {
		cin >> n;

		for (ulongf i = n; i > 0; --i) {
			if (isTidy(i)) {
				cout << "Case #" << tt << ": " << i << endl;
				break;
			}
		}
	}

	return 1;
}