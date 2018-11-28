#include<iostream>
#include<vector>
#include<algorithm>
#include<iomanip>
using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	
	int T;
	cin >> T;
	
	for(int TCASE = 1; TCASE <= T; TCASE++) {
		int n, k;
		cin >> n >> k;
		
		long double u;
		cin >> u;
		
		vector<long double> p(n);
		for(int i=0;i<n;i++)
			cin >> p[i];
		
		sort(p.begin(), p.end() );
		
		long double csum = p[0];
		
		for(int cnt = 1; cnt <= n; cnt++) {
			long double limit = (cnt == n ? 1.0L : p[cnt]);
			
			if(cnt == n || cnt*limit - csum >= u) {
				long double dest = min(1.0L, (u + csum) / cnt);
				
				long double result = 1.0;
				for(int i=0;i<cnt;i++)
					result *= dest;
				for(int i=cnt; i<n; i++)
					result *= p[i];
				
				cout << fixed << setprecision(7) << "Case #" << TCASE << ": " << result << '\n';
				break;
			}
			csum += p[cnt];
		}
	}
	
	return 0;
}

