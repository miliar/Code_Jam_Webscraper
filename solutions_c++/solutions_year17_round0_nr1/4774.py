#include <iostream>
#include <string>

using namespace std;

typedef pair<string, int> si;

void flip(string &txt, int idx, int k) {
	for (int i = 0; i < k; i++) {
		txt[idx + i] = txt[idx + i] == '-' ? '+' : '-';
	}
}

int solver(string txt, int k) {
	if (txt == string(txt.length(), '+')) return 0;

	int n = txt.length();
	int l, r;

	for (int i = 0; i < n; i++) {
		if (txt[i] == '-') { l = i; break; }
	}

	for (int i = n - 1; i >= 0; i--) {
		if (txt[i] == '-') { r = i; break; }
	}

	int count = 0;

	for (int i = l; i + k <= r;) {
		flip(txt, i, k);
		count++;
		while (i + k <= r and txt[i] == '+') i++;
	}

	for (int i = 0; i < n; i++) {
		if (txt[i] == '-') { l = i; break; }
	}

	if ((r - l + 1) % k != 0) return -1;

	for (int i = l; i <= r; i++) {
		if (txt[i] != '-') return -1;
	}

	return count + (r - l + 1) / k;
}

int main(void) {
	int t;
	cin >> t;

	// For each test case.
	for (int tc = 1; tc <= t; tc++) {
		int k;
		string txt;

		cin >> txt >> k;
		int output = solver(txt, k);

		if (output == -1) cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
		else cout << "Case #" << tc << ": " << output << endl;
	}

	return 0;
}