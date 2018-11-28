#include <cstdio>
#include <cmath>

using namespace std;

#define mod(S, N) (S & (N-1))
#define lastPowerOfTwo(S) ((long long int)pow(2.0, (int)(log(double(S)) / log(2.0))))

int main() {
	int t;
	scanf("%d", &t);
	long long int n, k;
	for(int q=1;q<=t;q++) {
		scanf("%lld %lld", &n, &k);
		printf("Case #%d: ", q);
		long long int s;
		
		long long int x = lastPowerOfTwo(k);

		s = (n - k%x)/x;

		printf("%lld %lld\n", s/2, (s-1)/2);
	}
	return 0;
}
