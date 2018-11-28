#include <bits/stdc++.h>

#define ll long long

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int test;
	cin >> test;
	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(6);
	for(int ctr=1;ctr<=test;ctr++) {
		ll d,n;
		cin >> d >> n;
		double fres = (double)(1e18);
		double val = d*1.000;
		for(ll i=0;i<n;i++) {
			ll x,y;
			cin >> x >> y;
			double res = (d-x)*1.00/y;
			if(val/res < fres) fres = val/res;
		} 
		cout << "Case #" << ctr << ": " << fres << "\n";
	}
	return 0;
}