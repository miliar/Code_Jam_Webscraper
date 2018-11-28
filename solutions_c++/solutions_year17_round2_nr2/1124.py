#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.o", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		int n, r, o, y, g, b, v;
		scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
		int maxvar = max(max(r, b), y);
		if (2 * maxvar > r + b + y) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		int arr[3];
		arr[0] = r;
		arr[1] = b;
		arr[2] = y;
		sort(arr, arr + 3);
		reverse(arr, arr + 3);
		int fnum = arr[0];
		int snum = arr[1];
		int tnum = arr[2];
		char first, second, third;
		if (r >= b && r >= y) {
			first = 'R';
			if (b >= y) {
				second = 'B';
				third = 'Y'; 
			} else {
				second = 'Y';
				third = 'B';
			}
		} else if (b >= r && b >= y) {
			first = 'B';
			if (r >= y) {
				second = 'R';
				third = 'Y';
			} else {
				second = 'Y';
				third = 'R';
			}
		} else {
			first = 'Y';
			if (b >= r) {
				second = 'B';
				third = 'R';
			} else {
				second = 'R';
				third = 'B';
			}
		}
		while (!(fnum == snum + tnum)) {
			fnum--; snum--; tnum--;
			printf("%c%c%c", first, second, third);
		}
		while (snum != 0) {
			fnum--;
			snum--;
			printf("%c%c", first, second);
		}
		while (fnum != 0 && tnum != 0) {
			fnum--;
			tnum--;
			printf("%c%c", first, third);
		}
		printf("\n");
	}
}