#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for (int test = 1; test <= tests; test++) {
		long long length;
		int n;
		cin >> length >> n;

		long double answer = 0;

		for (int i = 0; i < n; i++) {
			long double pos, speed;
			cin >> pos >> speed;
			answer = max(answer, (length - pos) / speed);
		}

		cout << "Case #" << test << ": ";
		cout << fixed << setprecision(7) << length / answer;
		cout << endl;
	}
}