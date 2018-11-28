#include <iostream>
#include <map>
#include <functional>

using namespace std;

ostream &operator <<(ostream &os, const pair<long long,long long> &p) {
	return os << p.first << ' ' << p.second;
}

pair<long,long> howfar(long long n, long long k) {
	map<long long, long long, greater<long long> > m;
	++m[n];
	long long a = -1, b = -1;
	while (k > 0) {
		auto it = m.begin();
		long long last = it->first;
		long long cnt = it->second;
		m.erase(it);
		k -= cnt;
		b = (last - 1) / 2;
		a = last - 1 - b;
		if (a) m[a] += cnt;
		if (b) m[b] += cnt;
	}
	return make_pair(a, b);
}

int main(void) {
	cout.sync_with_stdio(false);
	int nTests;
	cin >> nTests;
	for (int t = 1; t <= nTests; ++t) {
		long long n, k;
		cin >> n >> k;
		cout << "Case #" << t << ": " << howfar(n, k) << endl;
	}
	return 0;
}
