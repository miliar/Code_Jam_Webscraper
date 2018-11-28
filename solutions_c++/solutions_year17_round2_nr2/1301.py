#include <stdio.h>
#include <algorithm>



int n, r, o, y, g, b, v;
char last, highPrio;

int totRed() { return v + r + o; }
int totYellow() { return o + y + g; }
int totBlue() { return g + b + v; }
int totColor(char c) {
	if (c == 'R') return r;
	if (c == 'Y') return y;
	if (c == 'B') return b;
	if (c == 'O') return r + o + y;
	if (c == 'G') return y + g + b;
	if (c == 'V') return b + v + r;
	return -1;
}

bool isRed(char c) { return c == 'V' || c == 'R' || c == 'O'; }
bool isBlue(char c) { return c == 'G' || c == 'B' || c == 'V'; }
bool isYellow(char c) { return c == 'O' || c == 'Y' || c == 'G'; }
bool isSame(char c, char last) {
	if ((isRed(c) && isRed(last)) ||
		(isYellow(c) && isYellow(last)) ||
		(isBlue(c) && isBlue(last)))
	{
		return true;
	}
	return false;
}

struct color {
	int *amt;
	char c;

	const bool isH() const {
		if (isRed(c) && isRed(highPrio)) return true;
		if (isBlue(c) && isBlue(highPrio)) return true;
		if (isYellow(c) && isYellow(highPrio)) return true;
		return false;
	}

	bool operator<(const color &co) const {
		if (totColor(c) < totColor(co.c)) {
			return false;
		}
		if (totColor(c) == totColor(co.c) && !isH()) {
			return false;
		}
		if (totColor(c) == totColor(co.c) && isH() == co.isH()) {
			return c < co.c;
		}
		return true;
	}
};

color col[6];

void solve() {
	scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y, &g, &b, &v);
	col[0].c = 'R';
	col[0].amt = &r;
	col[1].c = 'O';
	col[1].amt = &o;
	col[2].c = 'Y';
	col[2].amt = &y;
	col[3].c = 'G';
	col[3].amt = &g;
	col[4].c = 'B';
	col[4].amt = &b;
	col[5].c = 'V';
	col[5].amt = &v;

	int pos = 0;
	char res[9001];

	last = 0;
	highPrio = 0;
	while (pos < n) {
		std::sort(col, col + 6);
		color *next;
		for (int i = 0; i < 7; i++) {
			if (i == 6) {
				printf("IMPOSSIBLE\n");
				return;
			}
			next = &col[i];
			if (isSame(next->c, last)) continue;
			if (*next->amt == 0) continue;
			break;
		}
		last = next->c;
		res[pos++] = last;
		(*next->amt)--;
		if (!highPrio) {
			highPrio = last;
		}
	}
	res[pos] = 0;

	if ((isRed(res[0]) && isRed(res[n - 1])) ||
		(isBlue(res[0]) && isBlue(res[n - 1])) ||
		(isYellow(res[0]) && isYellow(res[n - 1])))
	{
		printf("IMPOSSIBLE\n");
		return;
	}

	printf("%s\n", res);
}

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
