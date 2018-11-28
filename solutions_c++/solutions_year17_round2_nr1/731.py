#include <bits/stdc++.h>
using namespace std;
#define int long long
const double INF = 1e13;
main (){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout << fixed;
	cout << std::setprecision(6);
	int z;
	cin >> z;
	for (int casess = 1; casess <= z; ++casess){
		double d;
		cin >> d;
		
		int n;
		cin >> n;
		double odp = 1e18;
		for (int i = 0; i < n; ++i){
			double k, s;
			cin >> k >> s;
			odp = min(odp, (s*d)/(d-k));
		}  
		cout <<"Case #" << casess <<": ";
		cout << odp;
		cout <<'\n';
		 
	}
}

