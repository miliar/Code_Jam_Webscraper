/*
	1. 
*/
#include<cstdio>
#include<string>
#include<iostream>
using namespace std;

int main() {
	int t;
	scanf("%d", &t);

	for (int test = 1;test <= t;++test) {
		int n;
		scanf("%d", &n);
		bool ok = 0;
		while (!ok) {
			int i, j, k;
			i = n / 100;
			j = (n / 10) % 10;
			k = n % 10;
			if (i <= j&&j <= k) ok = 1;
			else --n;
		}
		printf("Case #%d: %d\n", test, n);
	}
}