#include <bits/stdc++.h>

using namespace std;

int dig[30], l;

void getdig(long long n) {
	l = 0;
	while(n) {
		dig[l ++] = n % 10;
		n /= 10;
	}
}

bool check(int p, int v, int s) {
	if(s)
		return true;
	for(int i = p - 1; i >= 0; -- i) {
		if(dig[i] > v)
			return true;
		if(dig[i] < v)
			return false;
	}
	return true;
}

void solve(long long n) {
	bool fi = true;
	getdig(n);
	int prev = 0, smaller = 0;
	for(int i = l - 1; i >= 0; -- i) {
		int l = prev, r = dig[i];
		if(smaller)
			r = 9;
		for(int j = r; j >= l; -- j) {
			if(check(i, j, smaller | (j < dig[i]))) {
				if(!fi || j)
					printf("%d", j);
				if(j)
					fi = false;
				prev = j;
				smaller |= j < dig[i];
				break;
			}
		}
	}
	puts("");
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cas = 1; cas <= T; ++ cas) {
		long long n;
		scanf("%I64d", &n);
		printf("Case #%d: ", cas);
		solve(n);		
	}
	return 0;
}