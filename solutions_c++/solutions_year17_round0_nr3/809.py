#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <map>
using namespace std;

int T;
long long N;
long long K;

map<long long, long long> a;

int main() {

	scanf("%d", &T);

	for(int tn = 0; tn < T; tn++) {

		scanf("%lld %lld", &N, &K);

		a.clear();
		a.insert(make_pair(-N, 1));

		long long rmin = 0;
		long long rmax = 0;

		while (K > 0) {
			long long n = -a.begin()->first;
			long long cap = a.begin()->second;
			a.erase(a.begin());
			if (K <= cap) {
				K = 0;
				if (n % 2 == 1) {
					rmin = n / 2;
					rmax = n / 2;
				}
				else {
					rmin = n / 2 - 1;
					rmax = n / 2;
				}
			}
			else {
				K -= cap;
				if (n % 2 == 1) {
					long long n1 = n / 2;
					a[-n1] = a[-n1] + cap * 2;
				}
				else {
					long long n1 = n / 2;
					long long n2 = n / 2 - 1;
					a[-n1] = a[-n1] + cap;
					a[-n2] = a[-n2] + cap;
				}
			}
		}

		printf("Case #%d: %lld %lld\n", tn+1, rmax, rmin);

	}

	return 0;

}