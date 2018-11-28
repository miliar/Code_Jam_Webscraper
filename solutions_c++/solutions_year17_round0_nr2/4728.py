#include <bits/stdc++.h>

using namespace std;

int t, k, ans;
long long int n;

bool check(long long int a) {
	int beg = a % 10;
	while (a > 0) {
		if (a % 10 > beg) {
			return false;
		}
		beg = a % 10;
		a /= 10;
	}
	return true;
}

long long int power(int p) {
	if (p == 0) {
		return 1;
	} else {
		return 10 * power(p - 1);
	}
}

void modify(long long int b) {
	int counter = 0;
	while (b % 10 == 9) {
		counter++;
		b /= 10;
	}
	long long int dif = 9 - (b % 10);
	n += dif * power(counter);
	n -= power(counter + 1);
}

int main() {
	freopen ("inn","r",stdin);
	freopen ("myfile.txt","w",stdout);
	scanf("%d", &t);
	for (int kk = 1; kk <= t; kk++) {
		cin >> n;
		while (!check(n)) {
			modify(n);
		}
		printf("Case #%d: %lld\n", kk, n);
	}
	return 0;
}
