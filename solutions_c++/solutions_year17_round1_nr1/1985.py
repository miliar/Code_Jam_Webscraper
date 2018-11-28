#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>

using namespace std;

int r, c;
vector<string> cake;

void solve() {
	cin >> r >> c;

	cake.assign(r, string(c, '?'));
	for (int i = 0; i < r; i++) {
		cin >> cake[i];
	}

	char name;
	for (int i = 0; i < r; i++) {
		name = '?';
		for (int j = 0; j < c; j++) {
			if (cake[i][j] != '?') {
				name = cake[i][j];
				break;
			}
		}

		if (name == '?' && i != 0) {
			cake[i] = cake[i - 1];
		} else {
			for (int k = 0; k < c; k++) {
				if (cake[i][k] == '?') {
					cake[i][k] = name;
				} else {
					name = cake[i][k];
				}
			}
		}
	}

	string empty_str(c, '?');
	int pos = 0;
	for (int i = 0; i < r; i++) {
		if (cake[i] != empty_str) {
			pos = i;
			break;
		}
	}
	for (int i = 0; i < pos; i++) {
		cake[i] = cake[pos];
	}
}

int main() {
	int t;
	long long n;

	cin >> t;

	for (int i = 0; i < t; i++) {
		solve();
		printf("Case #%d:\n", i + 1);
		for (auto s : cake) {
			printf("%s\n", s.c_str());
		}
	}
	return 0;
}
