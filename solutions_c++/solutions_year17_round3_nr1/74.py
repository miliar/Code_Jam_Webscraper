#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stdio.h>
#include <set>
using namespace std;
#define ll long long
typedef pair<ll,ll> pi;
ll t, n, k;
pi pan[1005];
long double pii = 3.14159265358979323846264338327950288;
priority_queue<ll> pq;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("Alargeout.txt", "w", stdout);
	scanf("%lld", &t);
	for (int i = 0; i < t; i++){
		scanf("%lld%lld", &n, &k);
		for (int j = 0; j < n; j++){
			scanf("%lld%lld", &pan[j].first, &pan[j].second);
		}
		sort(pan, pan + n, greater<pi>());
		long double maxanswer = 0.0;
		for (int j = 0; j <= n - k; j++){
			long double curanswer = 0.0;
			curanswer += pii*pan[j].first*pan[j].first;
			curanswer += pii*2.0*pan[j].first*pan[j].second;
			while (!pq.empty()){
				pq.pop();
			}
			for (int l = j + 1; l < n; l++){
				pq.push(pan[l].first*pan[l].second);
			}
			for (int l = 0; l < k - 1; l++){
				curanswer += pii*2.0*pq.top();
				pq.pop();
			}
			maxanswer = max(maxanswer, curanswer);
		}
		printf("Case #%d: %.9Lf\n", i + 1, maxanswer);
	}
}
