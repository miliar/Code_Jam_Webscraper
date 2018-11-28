#include <cstdio>
#include <cstring>
#include <iostream>
#include <queue>
using namespace std;
int T;
long long N, K;
int main() {
	scanf("%d", &T);
	for (int TT = 1; TT <= T; TT++) {
		scanf("%lld%lld", &N, &K);
		priority_queue<long long> q;
		q.push(N);
		long long last;
		while (K --) {
			last = q.top();
			q.pop();
			q.push(last / 2);
			q.push((last - 1) / 2);
		}
		printf("Case #%d: %lld %lld\n", TT, last / 2, (last - 1) / 2);		
	}
	return 0;
}	