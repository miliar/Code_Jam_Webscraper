#include <iostream>
#include <vector>
#include <utility>
#include <iomanip>
#include <deque>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdio>
#include <sstream>

using namespace std;

void answer(long long c, long long x, long long y) {
	cout << "Case #" << c + 1 << ": " << x << ' ' << y << endl;

}

int main_clever_algo()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		long long n, k;
		cin >> n >> k;
		long long a = (n - 1) / 2 + (n - 1) % 2, b = n - 1 - a, am_a = 1, am_b = 1; //a > b
		if (k != 1) {
			k--; //1st phase done manually
			while (k > 0) {
				long long _a, _b, _am_a, _am_b;
				_a = ((a - 1) / 2 + (a - 1) % 2);
				_b = (b - 1) / 2;
				if (a == b)
					_am_a = am_a + am_b,
					_am_b = _am_a;
				else if (a & 1)
					_am_a = 2 * am_a + am_b,
					_am_b = am_b;
				else
					_am_a = am_a,
					_am_b = am_a + 2 * am_b;
				k -= am_a;
				if (k <= 0) {
					answer(c, _a, a - _a - 1);
					break;
				}
				k -= am_b;
				if (k <= 0) {
					answer(c, b - _b - 1, _b);
					break;
				}
				a = _a;
				b = _b;
				am_a = _am_a;
				am_b = _am_b;
			}
		}
		else
			answer(c, a, b);
	}
	return 0;
}

int main_stupid_algo()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int c = 0; c < t; c++) {
		long long n, k;
		cin >> n >> k;
		multiset<int> a;
		a.insert(n);
		for (int i = 0; i < k; i++) {
			int p = *a.rbegin();
			a.erase(--a.end());
			int x = (p - 1) / 2 + (p - 1) % 2, y = p - x - 1;
			if (i == k - 1)
				answer(c, x, y);
			a.insert(x);
			a.insert(y);
		}
	}
	return 0;
}


int main() {
	/*
	freopen("output.txt", "w", stdout);
	cout << 1000 << endl;
	for (int i = 0; i < 1000; i++) {
		int n = rand() % 1000, k = rand() % n + 1;
		cout << n << ' ' << k << endl;
	}*/
	main_clever_algo();
	return 0;
}