#include <bits/stdc++.h>
using namespace std;

// why am I so weak

int n;
int a[6];

// 0 -> 2 3 4
// 1 -> 4
// 2 -> 4 5 0
// 3 -> 0
// 4 -> 0 1 2
// 5 -> 2

char trans(int x) {
	if (x == 0) return 'R';
	if (x == 1) return 'O';
	if (x == 2) return 'Y';
	if (x == 3) return 'G';
	if (x == 4) return 'B';
	return 'V';
}
int inv(char x) {
	if (x == 'R') return 0;
	if (x == 'O') return 1;
	if (x == 'Y') return 2;
	if (x == 'G') return 3;
	if (x == 'B') return 4;
	return 5;
}
inline bool trial(int x, int y) {
	if (x == 0) return y == 2 || y == 3 || y == 4;
	if (x == 1) return y == 4;
	if (x == 2) return y == 4 || y == 5 || y == 0;
	if (x == 3) return y == 0;
	if (x == 4) return y == 0 || y == 1 || y == 2;
	return y == 2;
}
string gao(int f) {
	string res = "";
	res += trans(f);

	int b[6];
	memset(b, 0, sizeof (b));

	b[f]++;

	for (int j = 1; j < n; j++) { 
		int choose = -1;

		for (int i = (j % 2 ? 0 : 6); (j % 2 ? i < 6 : i >= 0); (j % 2 ? i++ : i--)) if (trial(inv(res.back()), i) && b[i] < a[i]) {
			if (choose == -1 || a[i] - b[i] > a[choose] - b[choose]) {
				choose = i;
			}
		}

		if (choose < 0) return "IMPOSSIBLE";

		b[choose]++;
		res += trans(choose);
	}

	if (!trial(inv(*res.begin()), inv(res.back()))) return "IMPOSSIBLE";
	return res;
}
int main() {
	int _t;

	scanf("%d", &_t);

	for (int _ = 0; _ < _t; _++) {
		printf("Case #%d: ", _ + 1);

		scanf("%d", &n);

		for (int i = 0; i < 6; i++) {
			scanf("%d", &a[i]);
		}

		string res = "IMPOSSIBLE";

		for (int i = 0; i < 6 && res == "IMPOSSIBLE"; i++) if (a[i]) {
			res = gao(i);
		}

		printf("%s\n", res.c_str());
	}

	return 0;
}

