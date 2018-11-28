#include <bits/stdc++.h>

#define SZ(a) (int)a.size()
#define PB push_back

using namespace std;

typedef long long ll;

int main() {
	
	int T;
	scanf("%d ", &T);
	
	for(int tt = 1; tt <= T; tt++) {
		printf("Case #%d: ", tt);
		
		ll D;
		int N;
		scanf("%lld %d ", &D, &N);
		
		double maxT = 0.0;
		for(int i = 0; i < N; i++) {
			ll K,S;
			scanf("%lld%lld", &K, &S);
			maxT = max(static_cast<double>(D-K)/S, maxT);
		}
		
		printf("%.7lf\n", D/maxT);
	}
	
	return 0;
}
