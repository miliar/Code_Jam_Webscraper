#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

void divide(long long pieceF, long long sumF, long long &new_pieceF, long long &new_sumF, long long &new_pieceS, long long &new_sumS) {
	long long fst = pieceF / 2;
	if (pieceF % 2) {
		if (new_pieceF == fst) {
			new_sumF += sumF * 2;
			return;
		}
		new_pieceS = fst;
		new_sumS += sumF * 2;
		return;
	}
	else {
		if (new_pieceF == fst) {
			new_sumF += sumF;
			new_pieceS = fst - 1;
			new_sumS += sumF;
			return;
		}
		new_pieceS = fst;
		new_sumS += sumF;
		new_pieceF = fst - 1;
		new_sumF += sumF;
		return;
	}
}

long long get_max(long long number) {
	return number / 2;
}

long long get_min(long long number) {
	if (number % 2)
		return number / 2;
	else
		return number / 2 - 1;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int q = 0; q < t; q++) {
		long long n, k;
		cin >> n >> k;

		long long pieceF = n;
		long long sumF = 1;
		long long pieceS = -1;
		long long sumS = 0;

		bool flag = false;

		while (k && !flag) {
			long long new_pieceF = -1, new_sumF = 0, new_pieceS = -1, new_sumS = 0;
			if (pieceF > 1)
				divide(pieceF, sumF, new_pieceF, new_sumF, new_pieceS, new_sumS);
			k -= min(sumF, k);
			if (k == 0 && sumF > 0) {
				cout << "Case #" << q + 1 << ": ";
				cout << get_max(pieceF) << ' ' << get_min(pieceF) << '\n';
				flag = true;
				break;
			}
			if (pieceS != -1) {
				if (pieceS > 1)
					divide(pieceS, sumS, new_pieceF, new_sumF, new_pieceS, new_sumS);
				k -= min(sumS, k);
				if (k == 0 && sumS > 0) {
					cout << "Case #" << q + 1 << ": ";
					cout << get_max(pieceS) << ' ' << get_min(pieceS) << '\n';
					flag = true;
					break;
				}
			}
			if (new_pieceF > new_pieceS)
				pieceF = new_pieceF, sumF = new_sumF, pieceS = new_pieceS, sumS = new_sumS;
			else
				pieceS = new_pieceF, sumS = new_sumF, pieceF = new_pieceS, sumF = new_sumS;
		}

		if (flag)
			continue;
		cout << "Case #" << q + 1 << ": ";
		cout << 0 << ' ' << 0;
		cout << '\n';
	}

	return 0;
}