#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF (1LL << 55)
#define maxn 5111

typedef long long ll;

const long double PI = 3.14159265359;

pair<ll, ll> p[maxn];
ll n, k;

priority_queue<ll> pq;

long double solve(){
	ll ans = -1;
	cin >> n >> k;
	for(ll i = 1; i <= n; i++)
		cin >> p[i].fi >> p[i].se;


	sort(p + 1, p + 1 + n);
	reverse(p + 1, p + 1 + n);

	for(ll i = 1; i <= n; i++){
		while(!pq.empty())
			pq.pop();

		for(ll j = 1; j <= n; j++){
			if(i == j)
				continue;
			if(p[j].fi <= p[i].fi)
				pq.push({2 * p[j].fi * p[j].se});
		}

		ll cur = p[i].fi * p[i].fi + 2 * p[i].fi * p[i].se;
		ll add = 0, cnt = 1;

		while(!pq.empty() && cnt < k){
			//printf("%d\n", pq.top());
			add += pq.top();
			cnt++;
			pq.pop();
		}
		ans = max(ans, add + cur);
	}

	return (1.0 * ans * PI);
}



int main(){
	ll t;
	cin >> t;
	for(ll ll = 1; ll <= t; ll++){
		cout << fixed << setprecision(10) << "Case #" << ll << ": " << solve() << endl;
	}
	return 0;
}