#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
#include <assert.h>
using namespace std;
typedef long long i64;

i64 msb(i64 a)
{
	for (i64 i = 0; i < 64; ++i) {
		a >>= 1;
		if (a == 0) {
			return 1LL << i;
		}
	}
	assert(0);
	return -1;
}

int main() {
	int T; scanf("%d", &T);
	for (int Ti = 1; Ti <= T; ++Ti) {
		fprintf(stderr, "Case #%d of %d...\n", Ti, T);

		i64 N, K;
		scanf("%lld %lld", &N, &K);

		i64 a = msb(K);
		i64 i = (N-K)/a;
		
		printf("Case #%d: %lld %lld\n", Ti, i-(i/2), i/2);

	}
	return 0;
}
