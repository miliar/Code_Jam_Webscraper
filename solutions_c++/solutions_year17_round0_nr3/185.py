#include <bits/stdc++.h>

#define x first
#define y second

using namespace std;

typedef long long ll;
typedef pair<ll,ll> pll;

priority_queue<pll> pq;
ll T,N,K;

int main() {
	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		cin >> N >> K;
		while (!pq.empty()) pq.pop();
		pq.emplace(N,1);
		while (K>1) {
			pll t=pq.top();pq.pop();
			while (!pq.empty() && pq.top().x==t.x) {
				t.y+=pq.top().y;
				pq.pop();
			}
			ll ntake=min(K-1,t.y);
			if (t.x%2) pq.emplace(t.x/2,2*ntake);
			else {
				pq.emplace(t.x/2,ntake);
				pq.emplace(t.x/2-1,ntake);
			}
			if (ntake<t.y) pq.emplace(t.x,t.y-ntake);
			K-=ntake;
		}

		ll len=pq.top().x;
		printf("Case #%d: %lld %lld\n",cas,(len)/2,(len-1)/2);
	}
}
