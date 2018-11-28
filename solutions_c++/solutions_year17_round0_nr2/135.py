#include <iostream>
#include <vector>

using namespace std;

typedef long long int64;

int64 place(int64 x, int pos, int dig) {
	for (int i = 1; i <= pos; ++i) {
		x = x * 10 + dig;
	}
	return x;
}

void solve(int test) {
	cout << "Case #" << test << ": ";

	int64 n;
	cin >> n;

	int64 current = 0;

	for (int i = 18; i >= 1; --i) {
		for (int j = 0; j < 10; ++j) {
			if (j == 9 || place(current, i, j+1) > n) {
				current = current * 10 + j;
				break;
			}
		}
	}

	cout << current << "\n";
}

int main() {
	int tests;
	cin >> tests;

	for (int k = 1; k <= tests; ++k) {
		solve(k);
	}
}