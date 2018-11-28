#include <iostream>
#include <queue>
#include <utility>
#include <vector>
using namespace std;

typedef unsigned long long ll;
typedef pair<ll, ll> pll;

ll h_bit(ll num) {
	if (!num)
		return 0;
	ll ret = 1;
	while(num >>= 1)
		ret <<= 1;
	return ret;
}

ll solve(int N, int K) {
	priority_queue<ll, vector<ll> > pq;
	pq.push(N);
	for (int i = 0; i < K-1; ++i) {
		ll u = pq.top();
		pq.pop();
		if (u == 0)
			return 0;
		else {
			pq.push(u/2);
			pq.push((u-1)/2);
		}
	}
	return pq.top(); 
}

int main() {
	int T;	cin>>T;	
	for (int t = 1; t <= T; ++t) {
		ll N, K;	cin>>N>>K;
		priority_queue<pll, vector<pll> > pq;
		pq.push({N, 1});
		while (K > pq.top().second) {
			pll u = pq.top();	pq.pop();
			K -= u.second;
			if (u.first & 1)
				pq.push({u.first/2, 2*u.second});
			else {
				pq.push({u.first/2, u.second});
				pq.push({(u.first-1)/2, u.second});
			}
		}
		ll u = pq.top().first;
		//cout<<u<<endl;
		if (!u)
			cout<<"Case #"<<t<<": 0 0"<<endl;
		else
			cout<<"Case #"<<t<<": "<<u/2<<" "<<(u-1)/2<<endl;
		/*
		ll u = solve(N, K);
		cout<<"Case #"<<t<<": "<<u/2<<" "<<(u-1)/2<<endl;
		*/
	}
	
	return 0;
}
