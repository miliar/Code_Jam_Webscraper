#include <cstdio>

long long tidynumber( const long long n ) {
	if( n < 10 ) return n;
	long long result = n;
	long long base = 1, forward = 10;
	while( forward <= result ) {
		int r = result % forward / base;
		base *= 10;
		forward *= 10;
		int l = result % forward / base;
		if( r < l ) {
			result = result / base * base - 1;
		}
	}
	return result;	
}

int main() {
	int t; // test_cases
	long long n; // last number counted by Tatiana.
	scanf("%d", &t);
	// output last tidy number counted by Tatiana.
	for( int i = 1; i <= t; i++ ) {
		scanf("%lld", &n);
		printf("Case #%d: %lld\n", i, tidynumber(n));
	}
	return 0;
}
