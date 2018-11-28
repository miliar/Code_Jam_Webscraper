#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

typedef struct node {
	long long k, s;
};

long long n, r, o, y, g, b, v;
long long t1, t2, t3;
char OUT = 'X';
int t;

long long min(long long a, long long b) {
	if (a < b) return a;
	else return b;
}

long long max(long long a, long long b) {
	if (a > b) return a;
	else return b;
}

bool check(long long n, long long r, long long o, long long y, long long g, long long b, long long v) {
	b -= o;
	r -= g;
	y -= v;

	if ((b < 0) || (r < 0) || (y < 0)) return false;

	t1 = min(b, min(r, y));

	b -= t1;
	r -= t1;
	y -= t1;

	if (b == 0) t2 = min(r, y);
	if (r == 0) t2 = min(b, y);
	if (y == 0) t2 = min(r, b);

	t3 = max(b, max(r, y)) - t2;

	if (t3 == b - t2) OUT = 'B';
	if (t3 == r - t2) OUT = 'R';
	if (t3 == y - t2) OUT = 'Y';

	if ((t1 == 0) && (t2 == 0) && (t3 == 1)) return true;
	if (t3 > t1) return false;

	return true;
}

void output_g() {
	while (g > 0) {
		printf("G");
		g--;
		printf("R");
		r--;
	}
}
void output_v() {
	while (v > 0) {
		printf("V");
		v--;
		printf("Y");
		y--;
	}
}
void output_o() {
	while (o > 0) {
		printf("O");
		o--;
		printf("B");
		b--;
	}
}

void output_r() {
	if (r == 0) return;
	printf("R");
	r--;
	if (g > 0) output_g();
}
void output_y() {
	if (y == 0) return;
	printf("Y");
	y--;
	if (v > 0) output_v();
}
void output_b() {
	if (b == 0) return;
	printf("B");
	b--;
	if (o > 0) output_o();
}

void proc(int id) {
	scanf("%lld %lld %lld %lld %lld %lld %lld", &n, &r, &o, &y, &g, &b, &v);

// R + Y = O -- B
// Y + B = G -- R
// R + B = V -- Y

	printf("Case #%d: ", id);

	if (check(n, r, o, y, g, b, v) == true) {
		// RYB round
		char last = ' ';
		for (long long i = 0; i < t1; i++) {
			output_r();
			if ((OUT == 'B') && (t3 > 0)) {
				output_b();
				t3--;
			}
			output_y();
			if ((OUT == 'R') && (t3 > 0)) {
				output_r();
				t3--;
			}
			output_b();
			last = 'B';
			if ((OUT == 'Y') && (t3 > 0)) {
				output_y();
				t3--;
				last = 'Y';
			}
		}

		for (long long i = 0; i < t2; i++) {
			if (last == 'B') {
				output_r();
				output_y();
				output_b();
			} else {
				output_r();
				output_b();
				output_y();
			}
		}

		if ((OUT == 'B') && (t3 > 0)) {
			output_b();
			t3--;
		}
		while (o > 0) output_o();
		if ((OUT == 'R') && (t3 > 0)) {
			output_r();
			t3--;
		}
		while (g > 0) output_g();
		if ((OUT == 'Y') && (t3 > 0)) {
			output_y();
			t3--;
		}
		while (v > 0) output_v();
	} else {
		printf("IMPOSSIBLE");
	}
	printf("\n");
}

int main() {
	scanf("%d\n", &t);

	for (int i = 0; i < t; i++)
		proc(i + 1);

	return 0;
}
