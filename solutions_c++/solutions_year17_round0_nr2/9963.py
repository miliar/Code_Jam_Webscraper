
#include <bits/stdc++.h>

using namespace std;


int main() {
	// std::ios::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
		freopen("/Users/Ahmed/Downloads/B-large.in", "r", stdin);
		freopen("/Users/Ahmed/Desktop/B-large.out", "w", stdout);
	#endif

	int t;
	cin >> t;
	// cout << t << endl;
	for(int T = 1; T <= t; T++) {
		string n;
		cin >> n;
		while(1) {
			bool done = true;
			for(int i = 0; i < n.size() - 1; i++) {
				if(n[i] > n[i + 1]) {
					n[i] -= 1;
					done = false;
					for(int j = i + 1; j < n.size(); j++) n[j] = '9';
					break;
				}
			}
			if(done) break;
		}
		long long num = stoll(n);
		printf("Case #%d: %lld\n", T, num);
	}
}


