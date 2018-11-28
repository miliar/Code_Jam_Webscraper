#include <bits/stdc++.h>
using namespace std;
int main() {
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	map<long long, long long> m;
	int nTest;
	long long n, k, result;
	scanf("%d", &nTest);
	for(int t = 1; t <= nTest; t++) {
		scanf("%lld%lld",&n, &k);
		m.clear();
		m[n] = 1;
		while(k > 0) {
			map<long long, long long>::reverse_iterator u = m.rbegin();
			// cout << u->first <<" "<<u->second<<endl;
			if( u->second >= k) 
			{
				result = u->first;
			}
			else
			{
				if( m.count(u->first/2) == 0) m[u->first/2] = 0;
				m[u->first/2] += u->second;
				if( m.count((u->first-1)/2) == 0) m[(u->first-1)/2] = 0;
				m[(u->first-1)/2] += u->second;
			}
			k-= u->second;
			m.erase(u->first);
		}
		printf("Case #%d: %lld %lld\n", t, result/2, (result-1)/2);
	}
	return 0;
}