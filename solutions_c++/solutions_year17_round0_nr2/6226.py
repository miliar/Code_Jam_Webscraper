#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#define LL long long


int a[20];
void run() {
	LL n;
	int cnt = 0;
	scanf("%lld", &n);
	while(n) {
		a[cnt++] = n % 10;
		n /= 10;
	}
	std::reverse(a, a + cnt);
	int pos = 0;
	for(int i = 0; i < cnt - 1; i++) {
		if(a[i] <= a[i + 1]) pos = i + 1;
		else break;
	}
	if(pos != cnt - 1) {
		int q = pos;
		for(int i = pos; i >= 0; i--)
			if(i == 0 || a[i] - 1 >= a[i - 1]) {
				q = i; 
				break;
			}
		if(q == 0 && a[q] == 1) {
			for(int i = 0; i < cnt - 1; i++) printf("9");
			puts("");
			return;
		}
		a[q]--;
		for(int i = 0; i <= q; i++) 
			printf("%d", a[i]);
		for(int i = q + 1; i < cnt; i++)
			printf("9");
		puts("");
	}
	else {
		for(int i = 0; i < cnt; i++)
			printf("%d", a[i]);
		puts("");
	}
}


int main() {
	int T;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		run();
	}
	return 0;
}