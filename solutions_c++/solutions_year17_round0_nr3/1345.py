#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <set>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for (int test = 1; test <= tests; test++) {
		long long k, n;
		cin >> n >> k;

		long long power2 = 1;
		while (power2 * 2 <= k) power2 *= 2;

		n -= power2 - 1;
		k -= power2 - 1;

		long long numbers = n % power2;
		long long length;

		if (k <= numbers) length = n / power2 + 1;
		else length = n / power2;

		cout << "Case #" << test << ": ";
		cout << length / 2 << ' ' << (length - 1) / 2;
		cout << endl;
	}
}