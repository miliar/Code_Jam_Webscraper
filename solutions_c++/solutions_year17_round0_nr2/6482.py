#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

unsigned long long solve(unsigned long long n)
{
	char nstr[20];
	sprintf(nstr, "%llu", n);
	int i = strlen(nstr) - 1;
	while (i > 0) {
		if (nstr[i] < nstr[i-1]) {
			for (int j = i; j < strlen(nstr); j++) {
				nstr[j] = '9';
			}
			nstr[i-1]--;
		}
		i--;
	}
	return atoll(nstr);
}

int main() {
	int t;
	unsigned long long n;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		scanf("%llu", &n);
		unsigned long long m = solve(n);
		printf("Case #%d: %llu\n", i, m);
	}
	return 0;
}
