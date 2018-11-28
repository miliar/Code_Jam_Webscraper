#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int tidy(long long x) {
	int b[20];
	b[0] = 0;
	while (x) {
		b[++b[0]] = x % 10;
		x /= 10;
	}
	for (int i = 1; i < b[0]; ++i) {
		if (b[i] < b[i + 1])
			return 0;
	}
	return 1;
}

int main() {
	int tt;
	cin >> tt;

	for (int t = 0; t < tt; ++t) {
		long long n;
		cin >> n;
		while (!tidy(n)) --n;
		cout << "Case #" << (t + 1) << ": " << n << endl;
	}

	return 0;
}
