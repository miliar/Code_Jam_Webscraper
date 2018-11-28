#if 1 

#include <iomanip>
#include <iostream>
#include <string>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <algorithm>
using namespace std;

#define fill0(x)  memset(x,0, sizeof(x));
#define for0_n(x,n) for (long long x = 0, size = n; x < size; x++)


void prework() {

}
int n, p;
int z[1000];
void solve2() {
	int c = 0;
	for0_n(i, n) {
		if (z[i] > 0) c++;
	}
	cout << n - c / 2;
}
void solve3() {
	int c1 = 0, c2 = 0;
	for0_n(i, n) {
		if (z[i] == 1) c1++;
		if (z[i] == 2) c2++;
	}
	int re = 0;
	int x = min(c1, c2);
	int y = max(c1, c2);
	y -= x;
	int f = y / 3;
	int e = y % 3;
	re = n - x - f * 2;
	if (e > 1) re--;
	cout << re;

}
void solve4() {
	int c1 = 0, c2 = 0, c3 = 0;
	for0_n(i, n) {
		if (z[i] == 1) c1++;
		if (z[i] == 2) c2++;
		if (z[i] == 3) c3++;
	}
	int old = 0;
	int x = min(c1, c3);
	int y = max(c1, c3);
	y -= x;

	old += x;

	int z = min(y / 2, c2);
	old += z * 2;

	if (y / 2 > z) {
		int ss = y - 2 * z;
		int s4 = ss / 4;
		int l4 = ss % 4;
		old += s4 * 3;
		if (l4 > 1) old += l4 - 1;
	}
	else {
		int ss = c2 - z;
		int s2 = ss / 2;
		int l2 = ss % 2;
		old += s2;
		if (l2 > 0 && y % 2 > 0)  old++;
	}

	cout << n - old;
}

void work(int order) {

	cin >> n >> p;
	for (int i = 0; i < n; i++) {
		cin >> z[i];
		z[i] %= p;
	}
	if (p == 2) {
		solve2();
	}
	else if (p == 3) {
		solve3();
	}
	else if (p == 4) {
		solve4();
	}
}

int main(int argc, char *argv[])
{


	if (freopen("..\\temp\\output.txt", "w", stdout) == NULL)
		fprintf(stderr, "error redirecting stdout\n");
	if (freopen("..\\temp\\input.txt", "r", stdin) == NULL)
		fprintf(stderr, "error redirecting stdin\n");
	int t;
	cin >> t;
	prework();
	for0_n(i, t) {
		if (i == 0) {
			int x = 1;
			x = 2;  // debug
		}


		clog << "case begin " << i + 1 << endl;
		cout << "Case #" << i + 1 << ": ";
		work(i + 1);
		cout << endl;
		clog << "case end " << i + 1 << endl;
	}
	clog << "end!" << endl;
	return 0;

}
#endif
