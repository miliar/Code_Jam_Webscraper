#include <cstdio>
#include <map>
#include <queue>

using namespace std;

int main() {
	int T;
	long long k,n;
	scanf("%d",&T);
	for (int tc = 1; tc <= T; tc++) {
		scanf("%lld %lld",&n,&k);

		priority_queue<long long> pq;
		pq.push(n);

		map<long long, long long> count;
		count[n] = 1;

		long long resMax=0ll, resMin=0ll;
		while (!pq.empty()) {
			long long now = pq.top();
			long long countNow = count[now];
			pq.pop();

			k -= countNow;

			long long half = now / 2ll;
			bool isOdd = (now % 2ll) == 1ll;

			if (k <= 0ll) {
				if (isOdd) {
					resMax = half;
					resMin = half;
				} else {
					resMax = half;
					resMin = half-1ll;
				}

				break;
			}

			if (isOdd) {
				if (count.find(half) == count.end()) {
					count[half] = countNow * 2ll;
					pq.push(half);
				} else {
					count[half] += (countNow * 2ll);
				}
			} else {
				if (count.find(half) == count.end()) {
					count[half] = countNow;
					pq.push(half);
				} else {
					count[half] += countNow;
				}

				if (count.find(half-1ll) == count.end()) {
					count[half-1ll] = countNow;
					pq.push(half-1ll);
				} else {
					count[half-1ll] += countNow;
				}
			}
		}

		printf("Case #%d: %lld %lld\n", tc, resMax, resMin);
	}
	return 0;
}