#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

bool check(char s1, char s2) {
	if (s1 == s2) {
		return false;
	}
	if (s1 == 'R') {
		return !(s2 == 'O' || s2 == 'V');
	}
	if (s1 == 'Y') {
		return !(s2 == 'O' || s2 == 'G');
	}
	if (s1 == 'B') {
		return !(s2 == 'G' || s2 == 'V');
	}
	if (s1 == 'O') {
		return s2 == 'G';
	}
	if (s1 == 'V') {
		return s2 == 'Y';
	}
	if (s1 == 'G') {
		return s2 == 'R';
	}
}

vector<char> allv = vector<char>{ 'R', 'Y', 'B', 'O', 'G', 'V' };
vector<char> rv = vector<char>{ 'Y', 'B', 'G' };
vector<char> yv = vector<char>{ 'R', 'B', 'V' };
vector<char> bv = vector<char>{ 'R', 'Y', 'O' };

int n;
bool found;
vector<char> res;
void find(unordered_map<char, int>& colors, vector<char>& stalls, int pos) {
	if (found) {
		return;
	}

	if (pos == n) {
		res = stalls;
		found = true;
		return;
	}

	if (pos == 0) {
		for (char c : allv) {
			if (colors[c] != 0) {
				colors[c]--;
				stalls[0] = c;
				find(colors, stalls, 1);
				colors[c]++;
			}
		}
	}
	else {
		char pre = stalls[pos - 1];
		if (pre == 'O' || pre == 'G' || pre == 'V') {
			char c = ' ';
			if (pre == 'O') {
				c = 'B';
			}
			if (pre == 'G') {
				c = 'R';
			}
			if (pre == 'V') {
				c = 'Y';
			}
			if (colors[c] != 0) {
				colors[c]--;
				stalls[pos] = c;
				find(colors, stalls, pos + 1);
				colors[c]++;
			}
		}

		//
		vector<char> cv;
		if (pre == 'R') {
			cv = rv;
		}
		if (pre == 'Y') {
			cv = yv;
		}
		if (pre == 'B') {
			cv = bv;
		}

		for (char c : cv) {
			if (colors[c] != 0) {
				if (pos != n - 1 || (pos == n - 1 && check(c, stalls[0]))) {
					colors[c]--;
					stalls[pos] = c;
					find(colors, stalls, pos + 1);
					colors[c]++;
				}
			}
		}
	}
}

void func(int m1, int m2, int m3, char c1, char c2, char c3) {
	int part2 = m1 - m2;
	int part1 = m3 - part2;
	for (; m2 != 0; m1--, m2--, part1--) {
		printf("%c%c", c1, c2);
		if (part1 > 0) {
			printf("%c", c3);
		}
	}
	for (; m1 != 0; m1--) {
		printf("%c%c", c1, c3);
	}
}

int main() {
	//freopen("input.txt", "r", stdin);
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tt;
	cin >> tt;

	for (int t = 1; t <= tt; t++) {
		int r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;

		printf("Case #%d: ", t);
		if (r > y + b || y > b + r || b > r + y) {
			printf("IMPOSSIBLE");
		}
		// all three are equal
		else if (r == y && r == b) {
			while (r--) {
				printf("RYB");
			}
		}
		else if (r >= y && r >= b) {
			func(r, y, b, 'R', 'Y', 'B');
		}
		else if (y >= b && y >= r) {
			func(y, b, r, 'Y', 'B', 'R');
		}
		else if (b >= r && b >= y) {
			func(b, r, y, 'B', 'R', 'Y');
		}

		printf("\n");
	}

	fclose(stdout);
	return 0;
}
