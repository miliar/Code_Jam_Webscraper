#include <iostream>
#include <algorithm>
#include <queue>
#include <stdio.h>
#include <map>
using namespace std;
#define ll long long
typedef pair<ll,ll> pi;
ll tc, n, k;
priority_queue<ll> pq;
map<ll,ll> m;
int main(){
	freopen("C-large.in", "r", stdin);
	freopen("Cbig.txt", "w", stdout);
	scanf("%lld", &tc);
	for (int i = 0; i < tc; i++){
		scanf("%lld%lld", &n, &k);
		while (!pq.empty()){
			pq.pop();
		}
		m.clear();
		pq.push(n);
		m[n] = 1;
		while (k > m[pq.top()]){
			ll cur = pq.top();
			pq.pop();
			k -= m[cur];
			if (cur % 2 == 1){
				if (m.find((cur - 1)/2) != m.end()){
					m[(cur - 1)/2] += 2*m[cur];
				} else {
					m[(cur - 1)/2] = 2*m[cur];
					pq.push((cur - 1)/2);
				}
			} else {
				if (m.find((cur - 2)/2) != m.end()){
					m[(cur - 2)/2] += m[cur];
				} else {
					m[(cur - 2)/2] = m[cur];
					pq.push((cur - 2)/2);
				}
				if (m.find(cur/2) != m.end()){
					m[cur/2] += m[cur];
				} else {
					m[cur/2] = m[cur];
					pq.push(cur/2);
				}
			}
			m.erase(cur);
		}
		if (pq.top() % 2 == 1){
			printf("Case #%d: %lld %lld\n", i + 1, (pq.top() - 1)/2, (pq.top() - 1)/2);
		} else {
			printf("Case #%d: %lld %lld\n", i + 1, (pq.top())/2, (pq.top() - 2)/2);
		}
	}
}
