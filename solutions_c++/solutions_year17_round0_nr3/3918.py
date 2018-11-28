#include <cstdio>
#include <cmath>
#include <map>
#include <functional>

using namespace std;
typedef long long ll;

ll leftWidth(ll n) {
	return (ll)floor((n-1)/2.0);
}

ll rightWidth(ll n) {
	return (ll)ceil((n-1)/2.0);
}

void printCase(int count, ll ans) {
	printf("Case #%d: %lld %lld\n", count, rightWidth(ans), leftWidth(ans));
}

int main() {
	int T; scanf("%d", &T);
	for (int tC = 1; tC <= T; ++tC) {
		ll n, k; scanf("%lld %lld", &n, &k);

		map<ll, ll, greater<ll>> intervals;
		intervals[n] = 1;

		ll cIdx = 0;


		while (!intervals.empty()) {

			//printf("size: %lu\n", intervals.size());

			ll cIntrWidth = intervals.begin()->first;
			ll cIntrCount = intervals.begin()->second;

			//printf("processing interval length %lld * %lld times\n", cIntrWidth, cIntrCount);

			cIdx += cIntrCount;

			if (cIdx >= k) {
				printCase(tC, cIntrWidth);
				break;
			} else if (cIntrWidth > 1) {
				intervals.erase(intervals.begin());
				intervals[leftWidth(cIntrWidth)] += cIntrCount;
				intervals[rightWidth(cIntrWidth)] += cIntrCount;
				//printf("splitting into %lld and %lld\n", leftWidth(cIntrWidth), rightWidth(cIntrWidth));
			}

		}
	}
}