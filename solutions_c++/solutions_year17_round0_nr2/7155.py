#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cstdio>
using namespace std;

typedef long long ll;
ll n;
int m;
int a[30], b[30];

bool ok() {
	// if b <= a given length equal
	for (int i = m - 1; i >= 0; i --) {
		if (b[i] > a[i]) return false;
		if (b[i] < a[i]) return true;
	}
	return true;
}

void fillrest(int pos, int d) {
	for (int i = 0; i <= pos; i ++) {
		b[i] = d;
	}
}

void out(int *arr) {
	for (int i = m - 1; i >= 0; i --) printf("%d", arr[i]);
	printf("\n");
}

void solve(int testcase) {
	scanf("%lld", &n);
	m = 0;
	while (n > 0) {
		a[m ++] = int(n % 10);
		n /= 10;
	}

	fillrest(m - 1, 1);
	if (!ok()) {
		// 9999 smaller length
		printf("Case #%d: ", testcase);
		for (int i = 0; i < m - 1; i ++) printf("9");
		printf("\n");
	} else {
		for (int digit = m - 1; digit >= 0; digit --) {
			for (int num = 9; num >= 0; num --) {
				fillrest(digit, num);

				if (ok()) {
					break;
				}
			}
		}
		printf("Case #%d: ", testcase);
		for (int i = m - 1; i >= 0; i --) 
			printf("%d", b[i]);
		printf("\n");
	}

}

int main() {
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i ++) {
		solve(i);
	}
	return 0;
}