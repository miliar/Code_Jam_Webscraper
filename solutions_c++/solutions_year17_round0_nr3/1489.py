#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int T;
ll N, K;

int main() {
	int t=1;
	ll hi, cthi, ctlo, ctsum, res;
	scanf("%d", &T);
	while (T--) {
		scanf("%lld %lld", &N, &K);
		hi = N;
		cthi = 1;
		ctlo = 0;
		while (K) {
			if (K - cthi <= 0) {
				res = hi / 2;
				printf("Case #%d: %lld %lld\n", t++, res, hi-1-res);
				break;
			}
			K -= cthi;
			if (K - ctlo <= 0) {
				res = (hi - 1) / 2;
				printf("Case #%d: %lld %lld\n", t++, res, hi-2-res);
				break;
			}
			K -= ctlo;
			ctsum = cthi + ctlo;
			cthi = (hi % 2 != 0 ? cthi * 2 + ctlo: cthi);
			ctlo = ctsum*2 - cthi;
			hi = hi / 2;
		}
	}
	return 0;
}