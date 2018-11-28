#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#define int64 long long

using namespace std;

int64 N, K;
int T;

void print(int64 x) {
	int64 a = x / 2;
	int64 b = x - a - 1;
	printf("%lld %lld\n", max(a, b), min(a, b));
}

int main() {
	freopen("c-large.txt", "r", stdin);
	freopen("c-large.out", "w", stdout);

	scanf("%d", &T);
	for (int ii=1;ii<=T;++ii) {
		scanf("%lld %lld", &N, &K);
		printf("Case #%d: ", ii);
		//cerr << "new" << endl;
		int64 a = N - 1, b = N, n_a = 0, n_b = 1;

		for (;;) {
			if (n_b >= K) {
				print(b);
				break;
			}
			else K -= n_b;
			if (n_a >= K) {
				print(a);
				break;
			}
			else K -= n_a;
			//cerr << K << std::endl;
			if (a % 2LL == 1) {
				a = a / 2;
				b = b / 2;
				int64 n_a_new = n_a * 2LL + n_b;
				int64 n_b_new = n_b;
				n_a = n_a_new;
				n_b = n_b_new;
			}
			else {
				a = a / 2 - 1;
				b = b / 2;
				int64 n_a_new = n_a;
				int64 n_b_new = n_a + n_b * 2LL;
				n_a = n_a_new;
				n_b = n_b_new;
			}
		}
	}
}