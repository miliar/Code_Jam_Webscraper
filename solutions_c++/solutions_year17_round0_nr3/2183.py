#include <cstdio>

using namespace std;

struct range {
	long long n, cnt;
};

void proc(int cseno) {
	long long int k, n;
	range r1, r2;

	scanf("%lld %lld", &n, &k);
	r1.n = n;
	r1.cnt = 1;
	r2.n = 0;
	r2.cnt = 0;

	// r1.n > r2.n
	while (k > r1.cnt + r2.cnt) {
		//printf("At %lld (%d %d), (%d %d)\n", k, r1.n, r1.cnt, r2.n, r2.cnt);
		range nr1, nr2;
		nr1.n = r1.n / 2;
		nr2.n = r1.n / 2 - 1;
		if (r1.n % 2) {
			nr1.cnt = r1.cnt * 2;
			nr2.cnt = 0;
		} else {
			nr1.cnt = r1.cnt;
			nr2.cnt = r1.cnt;
		}

		if (r2.n % 2) {
			nr2.cnt += 2 * r2.cnt;
		} else {
			nr2.cnt += r2.cnt;
			nr1.cnt += r2.cnt;
		}

		k -= (r1.cnt + r2.cnt);
		r1 = nr1;
		r2 = nr2;
	}
    
	//	printf("At %lld (%d %d), (%d %d)\n", k, r1.n, r1.cnt, r2.n, r2.cnt);

	range fin = r1.cnt >= k ? r1 : r2;
	long long int mx =  fin.n / 2;
	long long int mn = fin.n % 2 || mx == 0 ? mx : (mx - 1);

	printf("Case #%d: %lld %lld\n", cseno, mx, mn);
	
}

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 0; i < n; i++)
		proc(i + 1);

	return 0;
}
