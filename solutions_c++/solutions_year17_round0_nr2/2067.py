#include <cstdio>
#include <iostream>


using namespace std;

unsigned long long solve(unsigned long long n) {
	unsigned long long divisor = 1000000000000000000ull;
	
	unsigned long long lastDigit = 0ull;
	for(; divisor >= 1ull; divisor /= 10ull) {
		unsigned long long tidyPrefix = n - n % divisor;
		unsigned long long leadDigit = n / divisor % 10ull;
		if(leadDigit < lastDigit)
			return solve (tidyPrefix - 1);
		lastDigit = leadDigit;
	}
	return n;
}

int main () {
	ios_base::sync_with_stdio (false), cin.tie (nullptr);

	freopen ("in.txt", "r", stdin);
	freopen ("out.txt", "w", stdout);

	int t;
	scanf ("%d", &t);
	for (int tc = 0; tc < t; tc++) {
		unsigned long long n;
		scanf ("%llu", &n);
		printf ("Case #%d: %llu\n", tc + 1, solve (n));
	}


	fflush (stdout);
	fclose (stdin);
	fclose (stdout);

	return 0;
}
