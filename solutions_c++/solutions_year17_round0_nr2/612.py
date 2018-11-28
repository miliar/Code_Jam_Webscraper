#include <bits/stdc++.h>

using namespace std;

int t;
char str[100],h[100];

long long tolong(char* str) {
	long long n = 0;
	while (*str != 0)
		n = n * (long long) 10 + (long long) (*(str++) - '0');
	return n;
}

int main() {
	scanf("%d", &t);
	for (int tc = 1; tc <= t; tc++) {
		scanf("%s", str);
		int n = strlen(str);
		for (int i = n-2; i >= 0; i--)
			if (str[i] > str[i+1]) {
				str[i] -= 1;
				for (int j = i + 1; j < n; j++)
					str[j] = '9';
			}
		printf("Case #%d: %lld\n", tc, tolong(str));
	}
	return 0;
}