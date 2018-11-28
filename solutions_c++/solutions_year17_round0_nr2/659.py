#include <cstdio>
#include <cstring>
#include <algorithm>

const unsigned long long  MAXD = 20;

unsigned long long  T, answer[MAXD];
unsigned long long  n;

int main() {
	scanf("%lld", &T);
	for (unsigned long long  cs = 1; cs <= T; cs++) {
		static char digits[MAXD];
		scanf("%lld", &n);
		sprintf(digits, "%lld", n);
		unsigned long long  length = strlen(digits);
		for (unsigned long long  i = 1; i <= length; i++) {
			for (unsigned long long  digit = 9; digit >= 0; digit--) {
				unsigned long long  minNumber = 0;
				for (unsigned long long  j = 1; j < i; j++) minNumber = minNumber * 10 + answer[j];
				for (unsigned long long  j = i; j <= length; j++) minNumber = minNumber * 10 + digit;
				if (minNumber <= n) {
					answer[i] = digit;
					break;
				}
			}
		}
		unsigned long long  number = 0;
		for (unsigned long long  i = 1; i <= length; i++) {
			number = number * 10 + answer[i];
		}
		printf("Case #%lld: %lld\n", cs, number);
	}
	return 0;
}
