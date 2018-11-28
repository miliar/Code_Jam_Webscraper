#include <bits/stdc++.h>
#include <stdio.h>
#include <cstdio>
#include <unordered_map>

#define SZ(c) int(c.size())
#define ALL(c) c.begin(), c.end()
#define clr(a,b) memset(a,b,sizeof a)
#define fr first
#define sc second
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ios_base::sync_with_stdio(false);

	ll n, k, t;

	cin >> t;
	int c = 0;
	while (t--) {
		cin >> n >> k;
		multiset<ll> m;
		m.insert(n);
		ll num, r, l;

		for (int i = 0; i < k - 1; ++i) {
			auto top = (m.end());
			top--;
			num = *top;
			m.erase(m.find(num));
			num--;
			r = num / 2 + (num % 2 != 0 ? 1 : 0);
			l = num / 2;
			if (r != 0)
				m.insert(r);
			if (l != 0)
				m.insert(l);
		}

		auto it = m.end();
		it--;
		num = *it - 1;
		cout << "Case #" << ++c << ": ";
		cout << num / 2 + (num % 2 != 0 ? 1 : 0) << " " << num / 2 << endl;

	}

	return 0;
}
