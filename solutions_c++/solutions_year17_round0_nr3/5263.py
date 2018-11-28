#include <cstdio>
#include <iostream>
#include <queue>

typedef long long int ll;

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    for ( int t = 0; t < T; t++ ) {
	ll N;
	ll K;
	scanf("%lld", &N);
	scanf("%lld", &K);
	priority_queue<ll> pq;
	pq.push(N);
	for ( int i = 0; i < K-1; i++ ) {
	    ll x = pq.top();
	    pq.pop();
	    ll a = x >> 1;
	    // 1余るときは、aと同じ
	    ll b = (x % 2) ? a : a - 1;
	    pq.push(a);
	    pq.push(b);
	}

	ll max_stalls = pq.top();
	ll a = max_stalls >> 1;
	// 1余るときは、aと同じ
	ll b = (max_stalls % 2) ? a : a - 1;

	printf("Case #%d: %lld %lld\n", t+1, a, b);
    }
    
    return 0;
}
