#include <bits/stdc++.h>

using namespace std;

#define LL long long

pair<LL, LL> F(LL n){
	if (n % 2 == 1){
		return make_pair(n / 2, n / 2);
	} else {
		return make_pair(n / 2, n / 2 - 1);
	}
}

LL n, k;

priority_queue<pair<LL, LL> > V;

void solve(){
	cin >> n >> k;
	if (n == k){puts("0 0"); return;}
	
    while (V.size()) V.pop();
	V.push(make_pair(n, 1));
	
	while (V.size() && V.top().second < k){
		k -= V.top().second;
		LL cnt = V.top().second;
		LL s = V.top().first;
		if (s % 2 == 1){
			s /= 2;
			cnt *= 2;
			V.push(make_pair(s, cnt));
		} else {
			s /= 2;
			V.push(make_pair(s, cnt));
			V.push(make_pair(s - 1, cnt));
		}
		V.pop();
	}

	pair<LL, LL> U = F(V.top().first);
	
	printf("%lld %lld\n", U.first, U.second);
}

int main(){
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		solve();
	}

}
