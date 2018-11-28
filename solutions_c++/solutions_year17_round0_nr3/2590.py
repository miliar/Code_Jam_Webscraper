#include <bits/stdc++.h>
using namespace std;
#define pb push_back
#define fst first
#define snd second
#define sz(a) int((a).size())
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;
const int INF = 1000 * 1000 * 1000;
const ll LLINF = 1ll << 53;
template<class T> void relaxmax(T& r, T v) { r = max(r, v); }
template<class T> void relaxmin(T& r, T v) { r = min(r, v); }

void add(map<ll, ll>& m, ll i, ll v) {
	if (m.find(i) == m.end()) m[i] = 0;
	m[i] += v;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		ll N, K;
		scanf("%lld%lld", &N, &K);
		/*
		priority_queue<int> q;
		q.push(N);
		for (int i = 0; i < K - 1; ++i) {
			int x = q.top();
			q.pop();
			q.push(x / 2);
			q.push((x - 1) / 2);
		}
		int x = q.top();
		printf("Case #%d: %d %d\n", t, x / 2, (x - 1) / 2);
		*/
		ll c = 0;				
		map<ll, ll> m;
		m[N] = 1;
		ll last = -1;
		while (c < K) {
			auto it = m.rbegin();
			last = it->first;
			add(m, last / 2, it->second);
			add(m, (last - 1) / 2, it->second);
			c += it->second;
			m.erase(--it.base());
		}
		printf("Case #%d: %lld %lld\n", t, last / 2, (last - 1) / 2);
	}
	return 0;
}
	
