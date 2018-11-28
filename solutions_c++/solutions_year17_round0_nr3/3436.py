#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <queue>

using namespace std;

typedef long long ll;

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		priority_queue<ll> PQ;
		ll N, K;
		cin >> N >> K;
		PQ.push(N);
		for (int i=0;i<K;i++) {
			ll cur = PQ.top();
			PQ.pop();
			ll a = cur / 2, b = cur / 2;
			if (cur % 2 == 0) b--;
			PQ.push(a);
			PQ.push(b);
			if (i == K-1) printf("Case #%d: %lld %lld\n", t, a, b);
		}
	}
}