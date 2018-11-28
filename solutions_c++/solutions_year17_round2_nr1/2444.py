#include <bits/stdc++.h>
using namespace std;


void solve() {
	double d;
	int n;
	cin >> d >> n;
	vector<double>tm;
	for(int i=0;i<n;i++) {
		double dx, sp;
		cin >> dx >> sp;
		double cur = (d - dx)/sp;
		// cout << cur << endl;
		tm.push_back(cur);
	}
	sort(tm.begin(), tm.end());
	cout << setprecision(12) << fixed << d / tm.back() << "\n";
}


int main() {
	int tc;
	cin >> tc;
	for(int i=1;i<=tc;i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
}