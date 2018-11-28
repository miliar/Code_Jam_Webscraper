#include <bits/stdc++.h>
using namespace std;

long long N, K;
int nc;
map <long long, long long> f;
map <long long, int> out;

void bfs() {
	queue <long long> q; f[N] = 1; q.push(N);
	while(!q.empty()) {
		long long x = q.front(); q.pop();
		if (x < 1 || out.count(x)) continue; 
		out[x] = 1;
		if (x % 2 == 0) {
			if (x / 2 - 1 > 0) f[x / 2 - 1] += f[x], q.push(x / 2 - 1);
			if (x / 2 > 0) f[x / 2] += f[x], q.push(x / 2);
		}
		else {
			if (x / 2 > 0) f[x / 2] += f[x] * 2, q.push(x / 2);
		}
	}
}

void solve() {
	cin >> N >> K;
	f.clear(); out.clear();
	bfs();

	vector<long long> vec;
	for (map<long long, long long>:: iterator it = f.begin(); it != f.end(); ++it) vec.push_back(it -> first);
	reverse(vec.begin(), vec.end());
	
	for (long long x: vec) {
		K -= f[x];
		if (K <= 0) { 
			printf("Case #%d: %lld %lld\n", ++nc, x / 2, x / 2 - (x % 2 == 0)); 
			return; 
		}
	}
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C.out", "w", stdout);
	ios_base::sync_with_stdio(false); cin.tie(0);
	int T; cin >> T;
	while(T--) {
		solve();
	}
}