#include <bits/stdc++.h>

using namespace std;

#define debug(x) cerr << "  - " << #x << ": " << x << endl;
#define debugs(x, y) cerr << "  - " << #x << ": " << x << "         " << #y << ": " << y << endl;

typedef long long ll;



int main(){
	int t;
	cin >> t;
	int tst = 0;
	while(t--){
		double d;
		int n;
		double minT = 0;
		cin >> d >> n;
		//cerr << fixed << setprecision(6);
		double k, si;
		for(int i = 0; i < n; i++){
			cin >> k >> si;
			minT = max(minT, (double) (d - k) / si);
			//debug((d - k) / si);
		}
		double res = d / minT;
		cout << "Case #" << ++tst << ": ";
		cout << fixed << setprecision(6) << res << endl;
	}
	return 0;
}