#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
const double EPS = 1e-50;

int cmp(double a, double b = 0.0){
	if(fabs(a-b) < EPS) return 0;
	return a > b ? 1 : -1;
}

int main(){
	ios::sync_with_stdio(false);
	int t, n;
	double d, a, b;
	cin >> t;

	for(int w = 1; w <= t; w++){
		cin >> d >> n;
		vector < pair < double, double > > vet;
		for(int i  = 0; i < n; i++){
			cin >> a >> b;
			vet.push_back(make_pair(a,b));
		}
		double lo = 0., hi = 100000000000001, mid, ans = 0.;
		int z = 0;
		while((cmp(lo, hi) <= 0) && z < 10000){
			z++;
			mid = (lo + hi)/2.;
			bool ok = true;
			double tempo = d/mid;
			for(int i = 0; i < n; i++){
				if( cmp((d-vet[i].first)/vet[i].second,tempo) >= 0 ){
					ok = false;
					break;
				}
			}
			if( ok ){
				ans = max(ans, mid);
				lo = mid+0.000001;
			}
			else{
				hi = mid-0.000001;
			}
		}

		cout << "Case #" << w << ": " <<  fixed << setprecision(6) << ans << endl;
		
	}

	return 0;
}