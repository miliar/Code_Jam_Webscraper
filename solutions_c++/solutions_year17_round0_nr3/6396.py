#include <cstdio>
#include <iostream>
#include <queue>
#include <string>
using namespace std;

long long N, K;
int T;
priority_queue<long long> pq;

int main() {
	scanf("%d", &T);
	for (int it = 1; it <= T; it++) {
		cin >> N >> K;
		while (!pq.empty()) {
			pq.pop();
		}
		pq.push(N);
		long long candidate, L, R;
		while (true) {
			K--;
			candidate = pq.top();
			pq.pop();
			L = candidate/2;
			R = candidate - L;
			if (L == R) {
				L--;
			} else {
				R--;
			}

			if (K == 0) {
				break;
			}
			if (L > 0) {
				pq.push(L);
			}
			if (R > 0) {
				pq.push(R);
			}
		}
		printf("Case #%d: %lld %lld\n", it, R, L);
	}
	return 0;
}