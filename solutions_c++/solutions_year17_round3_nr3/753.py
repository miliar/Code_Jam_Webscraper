#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define PI 3.1415926535897932384626433

ll n, k;

int main() {
	ll T;
	cin >> T;
	for(int TT = 1; TT <= T; TT++) {
		cin >> n >> k;
		ld ans = 0;
		ld u;
		vector<ld> p;
		cin >> u;
		for(int i = 0; i < n; i++) {
			ld x;
			cin >> x;
			p.push_back(x);
		}

		sort(p.begin(), p.end());
//		for(auto i: p) cout << i << endl;
//		cout << endl;

		ld noAtLowest = 1;
		for(int i = 1; i < n && u; i++, noAtLowest++) {
			ld U=u-((p[i]-p[i-1])*noAtLowest);
//			cout << u << " " << noAtLowest << " " << u/noAtLowest << " " <<  p[i-1] << " " << p[i] << endl;
			p[i-1] = min(p[i], p[i-1] + (u/(ld)noAtLowest));
//			cout << p[i-1] << endl << endl;
			u = max((ld)0, U);
			if(u==0) break;
		}
		int i = n;
		if(u) {
			ld U=u-(1-p[i-1])*noAtLowest;
			p[i-1] = min((ld)1, p[i-1]+(u/noAtLowest));
			u = max((ld)0, U);
		}
		for(int i = noAtLowest-1; i >= 0; i--) {
			p[i] = p[noAtLowest-1];
		}

//		cout << noAtLowest << ":\n";
//		for(auto i: p) cout << i << endl;

		cout << setprecision(14);
		ans = p[0];
//		cout << endl;
		for(int i = 1; i < n; i++) {
//			cout << fixed << ans << " ";
			ans*=p[i];
		}
//		cout << endl;
		
		cout << "Case #" << TT << ": " << fixed << min((ld)1, ans) << endl;
//		cout << endl;
	}
}