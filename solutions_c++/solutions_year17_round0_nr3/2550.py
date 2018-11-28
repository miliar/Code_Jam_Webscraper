#include <bits/stdc++.h>
using namespace std;

void main2() {
	long long n, k;
	cin >> n >> k;
	set<long long, greater<long long> > s;
	map<long long, long long> mp;
	s.insert(n);
	mp[n] = 1;
	while (k > 0) {
		long long x = *s.begin();
		s.erase(x);
		if (k <= mp[x]) {
			cout << x/2 << ' ' << (x-1)/2 << endl;
			return;
		} else {
			k-= mp[x];
			s.insert(x/2);
			mp[x/2] += mp[x];
			s.insert((x-1)/2);
			mp[(x-1)/2] += mp[x];
		}
	}	
}

int main() {
	int t;
	cin >> t;
	for (int o = 1; o <= t; o++) {
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
