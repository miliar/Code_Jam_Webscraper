#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <string>
#include <map>

using namespace std;

using ll = long long;

char buff[100500];
char colors[] = "BRY";
int cnt[3];

bool build(int B, int R, int Y) {
	char prv = 'x';
	cnt[0] = B;
	cnt[1] = R;
	cnt[2] = Y;
	buff[0] = 'x';
	for (int i = 0; i < B + R + Y; ++i) {
		int mx = -1;
		int pos = 0;
		for (int j = 0; j < 3; ++j) {
			if (colors[j] != prv) {
				if (cnt[j] > mx || cnt[j] == mx && colors[j] == buff[0]) {
					mx = cnt[j];
					pos = j;
				}
			}
		}
		if (cnt[pos] <= 0) {
			return false;
		}
		--cnt[pos];
		buff[i] = colors[pos];
		prv = buff[i];
	}
	return buff[0] != buff[B + R + Y - 1];
}

void print2(char a, char b, int cnt) {
	for (int i = 0; i < cnt; ++i) {
		printf("%c%c", a, b);
	}
	puts("");
}

bool solve() {
	int N;
	int R, O, Y, G, B, V;
	scanf("%d", &N);
	scanf("%d%d%d%d%d%d", &R, &O, &Y, &G, &B, &V);
	if (O == B && N == O + B) {
		print2('O', 'B', O);
		return true;
	}
	if (G == R && N == G + R) {
		print2('G', 'R', G);
		return true;
	}
	if (V == Y && N == V + Y) {
		print2('V', 'Y', V);
		return true;
	}
	if (O > 0 && O >= B) {
		return false;
	}
	B -= O;
	if (G > 0 && G >= R) {
		return false;
	}
	R -= G;
	if (V > 0 && V >= Y) {
		return false;
	}
	Y -= V;
	if (!build(B, R, Y)) {
		return false;
	}
	for (int i = 0; i < B + R + Y; ++i) {
		printf("%c", buff[i]);
		if (buff[i] == 'B') {
			while (O > 0) {
				printf("OB");
				--O;
			}
		}
		if (buff[i] == 'R') {
			while (G > 0) {
				printf("GR");
				--G;
			}
		}
		if (buff[i] == 'Y') {
			while (V > 0) {
				printf("VY");
				--V;
			}
		}
	}
	puts("");
	return true;
}

int main() {
	freopen("bin.txt", "r", stdin);
	freopen("bout.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		fprintf(stderr, "%d\n", i + 1);
		printf("Case #%d: ", i + 1);
		if (!solve()) {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}