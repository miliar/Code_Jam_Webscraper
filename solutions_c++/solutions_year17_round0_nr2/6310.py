#include <iostream>
#include <cstdio>
using namespace std;

long long T, n;

void f(long long n) {
	int l = 0, digit[20] = {0};
	while (n) {
		digit[l++] = n % 10;
		n = n / 10;
	}

	while (true) {

		bool remain = false;
		for (int i = l - 1; i >= 0; --i) {
			if (remain) {
				digit[i] = 9;
			} else if (i) {
				if (digit[i] > digit[i - 1]) {
					digit[i]--;
					remain = true;
				}
			}
		}

		bool cont = false;
		for (int i = l - 1; i > 0; --i) {
			if (digit[i] > digit[i - 1]) { cont = true; break; }
		}
		if (!cont) break;
	}

	bool top = true;
	for (int i = l - 1; i >= 0; --i) {
		if (digit[i] || !top) { cout << digit[i]; top = false; }
	}
}

int main () {
	cin >> T;
	for (int _ = 0; ++_ <= T;) {
		cin >> n;
		cout << "Case #" << _ << ": ";
		f(n);
		cout << endl;
	}
	return 0;
}
