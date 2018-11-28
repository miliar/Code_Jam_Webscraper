#include <bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
#define all(x) begin(x),end(x)
#define sz(x) ((int)(x).size())
#define F(i,n) for (int i = 0; i < n; ++i)
#define pb push_back
#define int long long
using namespace std;
typedef vector<int> vi;
typedef pair<int, int> pii;

template<typename T>
ostream& operator <<(ostream &s, const vector<T> &c) {
  s<<"[ "; for (auto it : c) s << it << " "; s<<"\b]\n";
  return s;
}

main () {
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t, a, b; cin >> t;
	for (int tt = 1; tt <= t; ++tt) {
		cin >> a >> b;
		priority_queue<int> pq;
		map<int, int> add;
		pq.push(a);
		add[a] = 1;
		int cur;
		while (b > 0) {
			cur = pq.top(); pq.pop();
			b -= add[cur];
			if (!add.count((cur - 1) / 2)) {
				pq.push((cur - 1) / 2);
				add[(cur - 1) / 2] = add[cur];
			} else add[(cur - 1) / 2] += add[cur];
			
			if (!add.count(cur / 2)) {
				pq.push(cur / 2);
				add[cur / 2] = add[cur];
			} else add[cur / 2] += add[cur];
		}
		cout << "Case #" << tt << ": " << cur / 2 << ' ' << (cur - 1) / 2 << '\n';
	}
	return 0;
}

