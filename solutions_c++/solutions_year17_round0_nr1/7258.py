#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

void flip(char s[], int p, int w) {
	for (int i = p; i < p + w; i++) {
		if (s[i] == '-') {
			s[i] = '+';
		} else if (s[i] == '+') {
			s[i] = '-';
		}
	}
}

int solve(char s[], int w) {
	int len = strlen(s);
	int p = 0, res = 0;
	while (p < len) {
		if (s[p] == '-') {
			if (p + w <= len) {
				flip(s, p, w);
				res ++;
			} else {
				return -1;
			}
		}
		p++;
	}
	return res;
}

int main() {
	char s[1100];
	int w, T, I;
	cin >> T;
	for (I = 1; I <= T; I++) {
		cin >> s >> w;
		int res = solve(s, w);
		if (res != -1) {
			cout << "Case #" << I << ": " << res << endl;
		} else {
			cout << "Case #" << I << ": IMPOSSIBLE" << endl;
		}
	}
	return 0;
}
