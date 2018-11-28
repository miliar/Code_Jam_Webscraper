#include <bits/stdc++.h>
#define pb push_back
using namespace std;
typedef long long ll;
const int N = 1005;
int t, n, d, nc=1;
pair<int, int> P[N];

bool p(long double v){
	long double time = d/v;
	long double pos = d;
	for(int i = 0; i < n; ++i)
		pos = min(pos, P[i].first + time*P[i].second);

	return abs(pos - d) < 1e-9; 
}


int main(){

	scanf("%d", &t);
	while(t--){
		scanf("%d %d", &d, &n);
		for(int i = 0; i < n; ++i)
			scanf("%d %d", &P[i].first, &P[i].second);

		sort(P, P+n, greater<pair<int, int> >());
		
		long double lo = 0.000001, hi = 500000000000000.0;
		for(int i = 1; i <= 200; ++i){
			long double mid = lo + (hi-lo)/2.0;
			if(p(mid)) lo = mid;
			else hi = mid;
		}
		
		printf("Case #%d: %Lf\n", nc++, lo);
	}

	return 0;
}
