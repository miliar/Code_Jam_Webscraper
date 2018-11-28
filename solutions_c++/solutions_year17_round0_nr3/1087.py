#include <bits/stdc++.h>

using namespace std;

int main()
{
	int ntc;
	scanf("%d", &ntc);
	for (int itc = 1; itc <= ntc; ++itc) {
		long long N, K;
		scanf("%lld%lld", &N, &K);
		priority_queue<pair<long long, long long> > pq;
		pq.push(make_pair(N, 1));
		while (K) {
			pair<long long, long long> p = pq.top();
			pq.pop();
			while (!pq.empty() && pq.top().first == p.first) {
				p.second += pq.top().second;
				pq.pop();
			}
			if (p.second >= K) {
				printf("Case #%d: %lld %lld\n", itc, (p.first)/2, (p.first-1)/2);
				break;
			}
			K -= p.second;
			if (p.first % 2) pq.push(make_pair(p.first/2, p.second * 2));
			else {
				pq.push(make_pair(p.first/2, p.second));
				pq.push(make_pair((p.first-1)/2, p.second));
			}
		}
	}
	return 0;
}
