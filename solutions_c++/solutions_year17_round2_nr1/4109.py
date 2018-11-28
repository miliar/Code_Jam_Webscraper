#include <bits/stdc++.h>

using namespace std; 

typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef long long ll;
#define mp make_pair
#define pb push_back;

const int MAXN = 3000;
const double INF = 1e9;
const double EPS = 1e-8;

int n, d;
pdd ks[MAXN];
void solve() {
	cin >> d >> n;
	for (int i = 0; i < n; i++) {
		cin >> ks[i].first >> ks[i].second;
	}                                   
	sort (ks, ks + n);
	double tmp = 0.0;
	//cerr << fixed << setprecision (8) << ks[0].first << " " << ks[0].second << "\n";
	if (n == 2) {
		if (ks[0].second - ks[1].second > EPS) {
			double tmp1 = (ks[1].first - ks[0].first) / (ks[0].second - ks[1].second);
			double loc = ks[0].first + ks[0].second * tmp1; 
		//	cerr << fixed << setprecision(8) << loc << "\n";
			if (d - loc > EPS) {
      	ks[0] = mp (loc, ks[1].second);				
				tmp += tmp1;
			}
		} 
	}
//	cerr << fixed << setprecision (8) << ks[0].first << " " << ks[0].second << "\n";
	tmp += (d - ks[0].first) / ks[0].second;
	//cerr << fixed << setprecision(8) << tmp << "\n";	
	cout << fixed << setprecision(8) << d / tmp << "\n";
}

int main () {
#ifdef LOCAL
	freopen ("test.in", "r", stdin);
	freopen ("test.out", "w", stdout);
#endif

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
	}
	
	return 0;
}