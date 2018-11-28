#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
using namespace std;

typedef long long ll;

ll n, m, x, a, b;

inline void solve() {
	map<ll, ll> mp;
	set<ll> st;
	mp[n] = 1;
	st.insert(n >> 1); st.insert((n - 1) >> 1);

	if (--m == 0) {
		a = (n - 1) >> 1;
		b = n >> 1;
		return;
	}
	
	while (!st.empty()) {
		x = *st.rbegin();
		st.erase(x);

		a = 0;

		auto it = mp.find(x << 1);	if (it != mp.end()) a += it->second;
		it = mp.find((x << 1) + 2);	if (it != mp.end()) a += it->second;
		it = mp.find((x << 1) + 1);	if (it != mp.end()) a += it->second << 1;

		mp[x] = a;
		m -= a;
		a = (x - 1) >> 1;
		b = x >> 1;

		if (m <= 0) return;
		if (a && !mp.count(a)) st.insert(a);
		if (b && !mp.count(b)) st.insert(b);
	}

	a = b = 0;
}

int main() {
	ifstream cin("C-large.in");
	ofstream cout("output.txt");

	int T, k;
	cin >> T;
	
	for (k = 1; k <= T; ++k) {
		cin >> n >> m;
		solve();
		cout << "Case #" << k << ": " << b << " " << a << endl;
	}

	cin.close();
	cout.close();
	return 0;
}