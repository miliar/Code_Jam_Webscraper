#include <bits/stdc++.h>
using namespace std;

int TC;

int main() {
	cin >> TC;
	for(int tc = 1; tc <= TC; ++tc) {
		long long k, n;
		cin >> n >> k;
		map<long long, long long> m;
		m.insert(make_pair(n, 1));
		for(; k > 1; --k) {
			int ma = m.rbegin()->first;
			if(--(m.rbegin()->second) == 0) m.erase(ma);
			long long s1 = (ma-1)/2 + (ma-1)%2;
			long long s2 = (ma-1)/2;
			if(m.count(s1)) {
				++m[s1];
			}
			else {
				m.insert(make_pair(s1, 1));
			}
			if(m.count(s2)) {
				++m[s2];
			}
			else {
				m.insert(make_pair(s2, 1));
			}
		}
		long long x = (m.rbegin()->first)-1;
		cout << "Case #" << tc << ": " << (x/2+x%2) << " " << (x/2) << endl;
	}
	return 0;
} 