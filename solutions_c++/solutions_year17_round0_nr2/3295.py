#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

typedef long long Int64;

int a[99], b[99];

bool check(int x, int d) {
	if (x < 0) return true;
	if (a[x] > d) return true;
	if (a[x] == d) return check(x - 1, d);
	return false;
}

int main() {
	int Test;
	scanf("%d", &Test);
	for (int test = 1; test <= Test; test++) {
		Int64 N;
		scanf("%I64d", &N);
		int L = 0;
		while (N > 0) {
			a[L++] = N % 10;
			N /= 10;
		}
		bool nine = false;
		for (int i = L - 1; i >= 0; --i) {
			if (nine) {
				b[i] = 9;
				continue;
			}
			if (check(i, a[i])) {
				b[i] = a[i];
				continue;
			}
			if (a[i] > 0 && check(i, a[i] - 1)) {
				b[i] = a[i] - 1;
				nine = true;
			}
		}
		Int64 R = 0;
		for (int i = L - 1; i >= 0; i--) R = R * 10 + b[i];
		printf("Case #%d: %I64d\n", test, R);
	}
	return 0;
}