#include <bits/stdc++.h>

using namespace std;

vector<pair<double, double> > v;
double d, n;
double tme = -1;

void solve() {
	v.clear();
	tme = -1;
	cin >> d >> n;
	for(int i=0; i<n; i++ ) {
		double a, b;
		cin >> a >> b;
		v.push_back(make_pair(a, b));
	}
	sort(v.rbegin(), v.rend());
	for(int i=0; i<n; i++ ) {
		double nt = (d - v[i].first) / v[i].second;
		if(nt < tme) {
			v[i].second = (d - v[i].first) / tme;
		}
		tme = max(tme, nt);
	}
	double res = numeric_limits<double>::max();
	for(int i=0; i<n; i++ ) {
		res = min(res, (v[i].first / tme) + v[i].second);
	}
	printf("%.6lf\n", res);
}

int main() {
    int ite;
    cin >> ite;
    for(int TT = 1; TT <= ite; TT++) {
        printf("Case #%d: ", TT);
        solve();
    }
    return 0;
}
