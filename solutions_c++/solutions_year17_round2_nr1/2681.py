#include <bits/stdc++.h>

using namespace std;

const int N = 1e3+10;
int T, d, n, k[N], s[N];

bool ok(double v){
	double t = d/v;
	for(int i = 0 ; i < n ; ++i){
		if(k[i]+s[i]*t <= d) return 0;
	}
	return 1;
}

int main(){
	
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin.sync_with_stdio(0);
	
	cin >> T;
	for(int t = 1 ; t <= T ; ++t){
		cin >> d >> n;
		for(int i = 0 ; i < n ; ++i) cin >> k[i] >> s[i];
		
		double lo = 0, hi = 1e30, mid;
		for(int i = 0 ; i < 10000 ; ++i){
			mid = (lo+hi)/2;
			if(ok(mid)){
				lo = mid;
			}else{
				hi = mid;
			}
		}
		printf("Case #%d: %.6f\n", t, mid);
	}
	

	return 0;
}
