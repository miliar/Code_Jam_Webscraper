#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

void work() {
	long long N, K;
	cin >> N >> K;
	long long a = 1, b = 0;
	long long x = N;
	for (; K > a + b; ) {
		K -= a + b;
		if (x & 1) {
			a = a * 2 + b;
		} else {
			b = b * 2 + a;
		}
		x /= 2;
	}
	if (K <= a) {
		cout << x / 2 << ' ' << (x - 1) / 2;
	} else {
		cout << (x - 1) / 2 << ' ' << (x - 2) / 2;
	}
}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		cout << "Case #" << i + 1 << ": ";
		work();
		cout << endl;
	}
	return 0;
}
